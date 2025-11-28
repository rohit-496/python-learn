list_items = []
elements = int(input("Enter the no of list numbers: "))
for i in range(0, elements):
    item = int(input(f"Enter the number {i+1}: "))
    list_items.append(item)

def sum_of_list(list_items, elements):
    sum = 0  
    for i in range(0,elements):
        sum = sum + list_items[i] ;
    return sum

print(f"The sum is : {sum_of_list(list_items,elements)}")


