# class Employee:
#     def __init__(self):
#         print("A init")
#     def info(self, name):
#         self.name = name
#     def salary(self,salary):
#         self.salary = salary

# class Staff(Employee):
#     def __init__(self):
#         print("B init")
#         super().__init__()
        
#     #staff is inheriting the features of Employee
#     def id(self):
#         print("this is id function")

# # class C(A,B)  multiple inheritance
# # emp1 = Employee()
# # emp1.info("rohit")
# # emp1.salary(60000)
# # st1 = Staff()
# # st1.info("Sittal")
# # st1.id()

# a1 = Staff()

class Animal:
    def __init__(self):
        print("animal speaks")
class Dog(Animal):
    def __init__(self):
        print('Dog barks')
class Puppy(Dog):
    def __init__(self):
        super().__init__()
        print("Puppy barks") 
    def access_super(self):
        s
pup_1 = Puppy()