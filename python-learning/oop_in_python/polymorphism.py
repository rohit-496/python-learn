#duck typing
# class PyCharm:
#  def execute(self):
#   print("Compiling")
#   print("Running")


# class MyEditor:
#  def execute(self):
#   print("Compiling")
#   print("Running")
#   print('Convention Check')

# class Laptop:
#  def code(self,ide):
#   ide.execute()

# ide = PyCharm()
# lap1 = Laptop()
# lap1.code(ide)

'''
class Student:
    def info(self, subject):
        subject.study()

class Physics:
    def study(self):
        print("I am subject...")

class Chemistry:
    def study(self):
        print("I am also subject..")

s1 = Student()
subject = Physics()
s1.info(subject)'''
'''
You can write functions or classes that accept any object that has a certain method, regardless of its class. 

For example, you can write a function that only expects an object to have fly() or quack() — doesn’t matter what class it is, as long as it has those methods.
'''
#operator overloading