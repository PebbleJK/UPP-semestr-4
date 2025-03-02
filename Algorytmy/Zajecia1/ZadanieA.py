#Link 1
print("Hello World")

#Link 2
#Ten link o interpreterze taki do przejrzenia widzę. Składni się nauczę pracując z nastepnymi linkami

#Link 3
#Tutaj też przejrzane o virutal environment

#Link 4
if True:
    print("True")
else:
    print("False")
#Tu jest moment o wzrokowym ogarnięciu kodu bez rozumienia co jest napisane więc nie będę go przepisywał
#total = item_one +\
#        item_two +\
#        item_three

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

word = 'word'
print (word)

sentence = "This is a sentence."
print (sentence)

paragraph = """This is a paragraph. It is
 made up of multiple lines and sentences."""
print (paragraph)

'''
Kilkuliniowy
komentarz
'''

#input("\n\nPress the enter key to exit.")

#import sys; x = 'foo'; sys.stdout.write(x + '\n')

#Link 5
counter = 100          # Creates an integer variable
miles   = 1000.0       # Creates a floating point variable
name    = "Zara Ali"   # Creates a string variable
print (counter)
print (miles)
print (name)

counter = 100
print (counter)

#del counter
#print (counter)
print(type(counter))
print(float(counter))
a = b = c = 3
a,b,c = 10,20,30
d = c * b
print("d = ", d, " = d")

#zmienne lokalne i globalne
def sum(x,y):
   sum = x + y
   return sum
print(sum(5, 10))

#Link 6
#if
age=17
print ("age: ", age)
if age >=18:
   print ("eligible to vote")
else:
   print ("not eligible to vote")
#elif
amount = 2500
print('Amount = ',amount)
if amount > 10000:
   discount = amount * 20 / 100
else:
   if amount > 5000:
      discount = amount * 10 / 100
   else:
      if amount > 1000:
         discount = amount * 5 / 100
      else:
         discount = 0

print('Payable amount = ',amount - discount)

#Link 7
zen = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''
for char in zen:
   if char not in 'aeiou':
      print (char, end='')

numbers = (34,54,67,21,78,97,45,44,80,19)
total = 0
for num in numbers:
   total += num
print ("Total =", total)

numbers = [34,54,67,21,78,97,45,44,80,19]
total = 0
for num in numbers:
   if num%2 == 0:
      print (num)

for num in range(5):
   print (num, end=' ')
print()
for num in range(10, 20):
   print (num, end=' ')
print()
for num in range(1, 10, 2):
   print (num, end=' ')

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers:
   print (x)
for x in numbers:
   print (x,":",numbers[x])
for x in numbers.items():
   print (x)

for num in range(10, 20):  
   #For loop to iterate on the factors 
   for i in range(2,num): 
      #If statement to determine the first factor
      if num%i == 0:      
         #To calculate the second factor
         j=num/i          
         print ("%d equals %d * %d" % (num,i,j))
         #To move to the next number
         break 
      else:                  
         print (num, "is a prime number")
         break

#Link 8
count=0
while count<5:
   count+=1
   print ("Iteration no. {}".format(count))

print ("End of while loop")

var = '0'
while var.isnumeric() == True:
   var = "test"
   if var.isnumeric() == True:
      print ("Your input", var)
print ("End of while loop")

count=0
while count<5:
   count+=1
   print ("Iteration no. {}".format(count))
else:
   print ("While loop over. Now in else block")
print ("End of while loop")

flag = 0
while (flag): print ("Given flag is really true!")
print ("Good bye!")

#Link 9
