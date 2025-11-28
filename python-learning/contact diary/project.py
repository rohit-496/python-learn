'''
create contact
view contact
update contact
delete contact
search contact
count contact
exit
'''

contacts = {}
while True:
    print('\nContact Book App')
    print('1. Create contact')
    print('2. View contact')
    print('3. Update contact')
    print('4. Search contact')
    print('5. Delete contact')
    print('6. Count contact')
    print('7. Exit')
    
    choice = int(input ("Enter your choice: "))

    if choice == 1:
        name = input ("Enter your name")
        if name in contacts:
            print(f"Contact name {name} already exists.")
        else:
            age = input("Enter age: " )
            email = input("enter email: ")
            mobile = input("enter your mobile number:")
            contacts[name] = {"Age": int(age), "email" :email, 'mobile': mobile}

            print(f"Contact name {name} has been created successfully")
    elif choice == 2:
        naam = input("Enter the name you want to view the contact of: ")
        if naam in contacts:
            print(contacts[naam])
        else:
            print("Contact not in the list")
    elif choice == 3:
        name = input("Enter the name of contact you want to update the information:")
        if name in contacts:
            age = input("Enter updated age: " )
            email = input("enter updated email: ")
            mobile = input("enter updated mobile number:")
            contacts[name]= {"Age":int(age) , "email": email, "mobile" : mobile}
            print("Contact was updated successfully...")
        else:
            print("Contact doesn't exist")

    elif choice == 4:
        name = input("Enter the name of the contact you want to search: ")
        if (name in contacts):
            print(contacts[name])
        else:
            print("Contact wasn't found")
    
    elif choice ==5:
           name = input("Enter the name of the contact you want to delete from the contact list: ")
           if(name in contacts):
                 contacts.pop(name)
                 print(f"Contact {name} was deleted successfully...")
           else:
               print("Contact wasn't found")
    
    elif choice ==  6:
        count = 0
        for naam in contacts:
            count += 1
        print(f"{count} contacts")


    elif choice == 7:
        print("Exiting the program")

    else:
        print("invalid choice")

