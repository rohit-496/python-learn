def fact(num):
    if (num == 0 or num == 1):
        return 1
    else:
        return num*fact(num-1)
    
while True: 
    try:
        num = int(input("Enter any number"))
        print("The factorial of %d is %d"%(num,fact(num))) 
        break
    except:
        print("Invalid input")