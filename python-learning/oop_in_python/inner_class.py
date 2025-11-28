# class Student:
#     def __init__(self,name,rollno, brand):
#         self.name =name
#         self.rollno =rollno
#         self.lap =  Student.Laptop(brand)
    
     
#     def print_data(self):
#         print("Name: ", self.name)
#         print("Roll no: ", self.rollno)
#         print("Brand: ", self.lap.brand)

    
#     class Laptop:

#         def __init__(self, brand):
#             self.brand = brand

# s1 = Student("Rohit", 2,"hp")
# s2 = Student("Sittal", 3,"lenovo")
# # print(s1.lap.brand)
# s1.print_data()
# # lap1 = Student.Laptop()

class Student:
    def __init__(self,name,rollno, brand):
        self.name =name
        self.rollno =rollno
    
    def print_data(self):
        print("Name: ", self.name)
        print("Roll no: ", self.rollno)
        print("Brand: ", self.lap.brand)

    
    class Laptop:
        def __init__(self, brand):
            self.brand = brand

s1 = Student("rohit", 32)
lap1 = Student.Laptop("dell")