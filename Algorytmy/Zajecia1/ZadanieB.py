#Zadanie 1
def odd_count(n):
    counter = 0
    for x in range(n):
        if x%2 == 1:
            counter = counter + 1
    return counter

print(odd_count(7))

#Zadanie 2
def correct_polish_letters(st): 
    d = { 'ą':'a', 'ć':'c', 'ę':'e', 'ł':'l', 'ń':'n', 'ó':'o', 'ś':'s', 'ź':'z', 'ż':'z' }
    newString = ""
    for x in st:
        if x in d:
            newString = newString + d[x]
        else:
            newString = newString + x
    return newString
    pass

print(correct_polish_letters("Jakub Kałuża"))

#Zadanie 3
def replace_exclamation(st):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    newString = ""
    for x in st:
        if x in vowels:
            newString = newString + "!"
        else:
            newString = newString + x
    return newString
print(replace_exclamation("Jakub"))

#Zadanie 4
def get_size(w,h,d):
    return [2*w*h + 2*w*d + 2*h*d, w*h*d]
print(get_size(1,2,3))

#Zadanie 5
def whatday(num):
    weekday = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4:"Wednesday", 5:"Thursday", 6:"Friday", 7:"Saturday"}
    if 0 < num < 8:
        return weekday[num]
    else:
        return "Wrong, please enter a number between 1 and 7"
print(whatday(3))
