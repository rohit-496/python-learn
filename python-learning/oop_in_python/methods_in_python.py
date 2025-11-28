class Student:
    section = 12
    def __init__(self,m1=0,m2=0,m3=0):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        print("Object created")
    def avg(self):
         return  (self.m1+self.m2+self.m3)/3
    
    @classmethod
    def section(cls): 
        return cls.section
    
    @staticmethod
    def info():
        print('this is a static function')

       
s1 = Student(45,55,65)
print("Average is: ",round(s1.avg(),2))
print(Student.section())

#two types of instance methods 
# acccessor methods and mutator methods