def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1/num2

while True:
    try:
        number1 = float(input("Enter the number: "))
        number2 = float(input("Enter the number: "))
        print("The additon of %f and %f is %f" %(number1, number2, add(number1, number2))) 
        print("The subtraction of %f and %f is %f" %(number1, number2, sub(number1, number2))) 
        print("The product of %f and %f is %f" %(number1, number2, mul(number1, number2)))
        while True:
         if number2 == 0:
          number2 = int(input("Enter a number greater than zero for division: "))
         else: 
          print("The division of %f and %f is %f" %(number1, number2, div(number1, number2))) 
         break
    except:
        print("Invalid input")
