def triangle_printer(rows):
    for i in range(0, rows):
        pointer = ""
        for j in range(0,i+1):
            pointer = pointer + "*"
            j = j + 1
        print(pointer)
    i = i + 1

rows= int(input("Enter the number of rows in the triangle: "))
print(triangle_printer(rows))

