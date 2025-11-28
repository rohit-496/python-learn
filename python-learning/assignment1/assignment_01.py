def even_or_odd(num):
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

while True:
    try:
     num1 = int(input("Enter the number: "))
     even_or_odd(num1)
     break
    except:
      print("Not a valid number")




    