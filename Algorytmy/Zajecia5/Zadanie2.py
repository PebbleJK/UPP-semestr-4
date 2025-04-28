class Node:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []      # lista wyników
        self.values = []    # lista list nicków (jeśli liść) lub dzieci (jeśli nie liść)
        self.next = None    # wskaźnik na następny liść (dla szybkich zapytań o zakres)

class BPlusTree:
    def __init__(self, order=3):
        self.root = Node(leaf=True)
        self.order = order
        self.nick_to_score = {}  # nick -> wynik
        self.comparisons = 0

    def _find_leaf(self, score):
        node = self.root
        while not node.leaf:
            i = 0
            while i < len(node.keys) and score >= node.keys[i]:
                self.comparisons += 1
                i += 1
            node = node.values[i]
        return node

    def insert(self, nick, score):
        self.nick_to_score[nick] = score
        leaf = self._find_leaf(score)

        i = 0
        while i < len(leaf.keys) and score > leaf.keys[i]:
            self.comparisons += 1
            i += 1
        
        if i < len(leaf.keys) and leaf.keys[i] == score:
            self.comparisons += 1
            leaf.values[i].append(nick)
        else:
            self.comparisons += 1
            leaf.keys.insert(i, score)
            leaf.values.insert(i, [nick])

        if len(leaf.keys) > self.order:
            self._split(leaf)

    def _split(self, node):
        mid = len(node.keys) // 2
        sibling = Node(leaf=node.leaf)

        sibling.keys = node.keys[mid:]
        sibling.values = node.values[mid:]
        node.keys = node.keys[:mid]
        node.values = node.values[:mid]

        if node.leaf:
            sibling.next = node.next
            node.next = sibling

        if node == self.root:
            new_root = Node(leaf=False)
            new_root.keys = [sibling.keys[0]]
            new_root.values = [node, sibling]
            self.root = new_root
        else:
            parent = self._find_parent(self.root, node)
            i = parent.values.index(node)
            parent.keys.insert(i, sibling.keys[0])
            parent.values.insert(i + 1, sibling)
            if len(parent.keys) > self.order:
                self._split(parent)

    def _find_parent(self, node, child):
        if node.leaf:
            return None
        for i in node.values:
            if i == child:
                return node
            res = self._find_parent(i, child)
            if res:
                return res
        return None

    def update_score(self, nick, new_score):
        if nick not in self.nick_to_score:
            return
        self.delete(nick)
        self.insert(nick, new_score)

    def delete(self, nick):
        if nick not in self.nick_to_score:
            return

        score = self.nick_to_score[nick]
        del self.nick_to_score[nick]

        leaf = self._find_leaf(score)

        i = 0
        while i < len(leaf.keys) and leaf.keys[i] != score:
            self.comparisons += 1
            i += 1

        if i == len(leaf.keys):
            return

        leaf.values[i].remove(nick)
        if not leaf.values[i]:
            leaf.keys.pop(i)
            leaf.values.pop(i)

    def find_range(self, low, high):
        result = []
        leaf = self._find_leaf(low)

        while leaf:
            for i, score in enumerate(leaf.keys):
                self.comparisons += 1
                if low <= score <= high:
                    result.extend(leaf.values[i])
                elif score > high:
                    return result
            leaf = leaf.next

        return result

    def find_best(self):
        node = self.root
        while not node.leaf:
            node = node.values[-1]
        return node.values[-1][0], node.keys[-1]

    def find_worst(self):
        node = self.root
        while not node.leaf:
            node = node.values[0]
        return node.values[0][0], node.keys[0]

    def get_score(self, nick):
        return self.nick_to_score.get(nick)

    def reset_comparisons(self):
        self.comparisons = 0

# Przykład użycia
if __name__ == "__main__":
    tree = BPlusTree(order=3)

    tree.insert("alice", 100)
    tree.insert("bob", 200)
    tree.insert("carol", 150)
    tree.insert("dave", 100)
    tree.insert("eve", 250)

    print("Najlepszy gracz:", tree.find_best())   # ('eve', 250)
    print("Najgorszy gracz:", tree.find_worst())   # ('alice', 100) albo 'dave'
    print("Gracze 100-200:", tree.find_range(100, 200))  # ['alice', 'dave', 'carol', 'bob']
    print("Wynik carol:", tree.get_score("carol"))  # 150

    tree.update_score("alice", 300)
    print("Po aktualizacji Alice, najlepszy:", tree.find_best())  # ('alice', 300)

    tree.delete("bob")
    print("Po usunięciu Boba, gracze 100-300:", tree.find_range(100, 300))

    print("Liczba porównań:", tree.comparisons)
