'''
BankAccount class (deposit/withdraw)
• Student class (marks → average → grade)
• Shape hierarchy (Circle, Rectangle, Triangle)
• Library system with borrow/return
• Operator overloading

'''

#bank  account

'''class Bank_account:
    def __init__(self, name ,total_balance = 0):
        self.name = name
        self.total_balance = total_balance
    
    def deposit(self,amount):
        if (amount <= 0 ):
            print("Please enter a valid amount to deposit")
        else:
            self.total_balance +=amount
            print(f"The amount {amount} has been deposited and new balance is: {self.total_balance}")
    
    def withdraw(self, amount):
        if amount <= 0:
           print("Withdrawal amount must be positive")
        if amount > self.total_balance:
            print("Insufficient funds")
        self.total_balance -= amount
        print(f"{self.name}: Withdrew {amount}. New balance = {self.total_balance}")

    def showinfo(self):
        print(f"Name: {self.name}\nTotal Balance:{self.total_balance} ")

b1 =  Bank_account("Rohit", 15000)
b1.withdraw(4000)
b1.deposit(10000)
b1.showinfo()
'''

#student marks->avg->grade

'''class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        sum = 0
        for marks in self.marks:
            sum += marks
        return sum/len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

    def showinfo(self):
        print(f"Name: {self.name}\nAverage:{round(self.average(),2)} \nGrade: {self.grade()}")

s1 = Student("Bob", [88, 76, 90, 85])
s1.showinfo()'''

#shape Hierarchy 
'''import math

class Shape:
    def area(self):
        print("This method should be overridden")

    def perimeter(self):
       print("This method should be overridden")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def show(self):
        return f"Circle(radius={self.radius})"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def show(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Triangle(Shape):
    def __init__(self, a, b, c):
        # a, b, c are lengths of sides
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def show(self):
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"




shapes = [
        Circle(5),
        Rectangle(4, 6),
        Triangle(3, 4, 5)
    ]

for shape in shapes:
        print(shape.show(), "area =", shape.area(), "perimeter =", shape.perimeter())
'''

#library system with borrow  and return
'''class Student:
    def __init__(self,name,s_id):
        self.name=name
        self.s_id=s_id
        self.borrowed_books=[]
        print(f"Account for {self.name} ({self.s_id}) successfully created \n")
    def borrow(self,b_id):
        self.b_id=b_id
        self.borrowed_books.append(self.b_id)
        print(f"{self.b_id} is borrowed by {self.s_id,self.name}")
    def returned(self,b_id):
        # self.b_id=b_id
        self.borrowed_books.remove(b_id)
        print(f"{b_id} is returned by {self.s_id, self.name}\n")
    def view_books(self):
        print("Borrowed books: ")
        for books in self.borrowed_books:
            print(books)
        print("\n")
s1=Student("Sittal",1011450)
s1.borrow(45778)
s1.borrow(47894)
s1.borrow(47112)
s1.returned(45778)
s1.view_books()'''

#operator overloading
'''import math
class feet:
    def __init__(self,f,i):
        self.f = f
        self.i = i
    
    def __str__(self):
        return f"Feet: {self.f} Inches:{self.i}"
    
    def __add__(self,obj):
        self.f = self.f + obj.f +(self.i + obj.i) //12
        self.i = (self.i + obj.i) % 12
        return self.f, self.i


f1 = feet(3,4)
f2 = feet(7,11)
f3 =  f1 + f2
print(f3)'''

class book:
    def __init__(self,title,author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_borrow = False

    def borrow_book(self):
        if self.is_borrow == False:
            self.is_borrow == True
            print(f"Book id {self.book_id} - {self.title} is borrowed")
        else:
            print("The book isn't available")

        
    def return_book(self):
        if self.is_borrow == True:
            self.is_borrow = False
            print(f"Book id {self.book_id} -{self.title} is returned")

class Library:

    def  __init__(self):
       self.books = []

    def add_book(self,book):
        self.books.append(book)        
        print("Book added to library")

    def show_books(self):
        print("Library books:")
        for book in self.books:
            status ="Available" if book.is_borrow == False else "Borrowed"
            print(f"ID: {book.book_id} Title: {book.title} Status: {status}")



library = Library()
book1 = book("Harry Potter","JK rowling",101)
library.add_book(book1)
library.show_books()
book1.borrow_book()
library.show_books()
book1.return_book()
library.show_books()
