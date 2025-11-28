'''
Assignments:

Write a program that checks if a number is prime.

Build a simple temperature converter (Celsius to Fahrenheit).

Print a multiplication table for any given number.

Find all numbers divisible by 7 but not a multiple of 5, between 1000–3000.

Pattern Printing Challenge (pyramid, diamond, Pascal’s triangle).

 Challenge Project: Create a mini student grading system (input marks, calculate average, assign grades).
'''

#Write a program that checks if a number is prime
'''
flag = 0
def prime(num, flag):
     if(num <= 1):
         print(f"{num} is Not prime")
     else:
         for i in range(1,num+1):
            if(num % i == 0):
             flag = flag + 1
         if(flag == 2):
          print(f"{num} is prime number") 
         else:
          print(f"{num} is not prime number")

num = int(input("Enter any number: "))
prime(num, flag)
'''


#Temperature converter
'''
def converter(inp):
    fah = (inp * 9/5) + 32
    return fah

inp = float(input("Enter the temperature: "))
res = converter(inp)
print (f"The temperature in fahrenheit is: {res}")
'''


#Print a multiplication table for any given number.

'''
inp = int(input("Enter the number you want to get the multiplication table of: "))
print(f"Multiplication table of {inp}")
for i in range (1,11):
    print(f"{inp}*{i} = {inp*i}")
'''

# Find all numbers divisible by 7 but not a multiple of 5, between 1000–3000.

'''
count = 0
print("The number divisible by 7 and not by 5 between 1000-3000 are:\n")
for i in range (1001,3000):
    if (i % 7 == 0 and i%5 != 0):
      count = count + 1
      print(i)
print(f"There are total {count} numbers which are divisible by 5 not by 7 between 1000-3000")
'''

#Pattern Printing Challenge (pyramid, diamond, Pascal’s triangle).
#pyramid
'''
inp = int (input('Input the number of rows'))
for i in range(1, inp):
    print (" " * (inp-i-1) + "*" * (2 * i - 1) )
 
'''
#diamond

'''
inp = int (input('Input the number of rows: '))
for i in range(1, inp+1):
    print (" " * (inp-i) + "*" * (2 * i - 1) )

for  i in range (inp-1, 0 , -1):
    print(" "*(inp-i) + "*" * (2 * i - 1))

'''



