'''class Computer:
    def __init__(self,cpu="1 6",ram="16"):
       self.cpu = cpu #instance variable
       self.ram = ram
        
    def config(self):
        print(self.cpu,self.ram)

com2 = Computer("17",8)
com1 = Computer()
com1.config()
com2.config()'''

#id is used to find the address of the object or the variable  
 

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        return (f"Name: {self.name}\nAge: {self.age}")

s1 = Student("rohit", 18)
print(s1.show())

#when we write print (obj) the __str__ magic method is called automatically we dont have to call it it returns string as it used for printing at last