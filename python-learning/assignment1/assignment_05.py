def positive_number(my_list):
    new_list  = []
    for item in my_list:
      if item > 0:
       new_list.append(item)
    return new_list

my_list = []
number_of_items = int(input("Enter the number of items in the list: "))

for i in range(0,number_of_items):
    item = float(input(f"Enter the number{i+1}: "))
    my_list.append(item)
print("The new list with positive number :%s "%(positive_number(my_list)))



