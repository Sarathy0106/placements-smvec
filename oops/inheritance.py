# ===== 1. SINGLE INHERITANCE =====

# Question 1: Person and Student
print("=" * 50)
print("Question 1: Single Inheritance - Person & Student")
print("=" * 50)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_person(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no
    
    def display_student(self):
        self.display_person()
        print(f"Roll No: {self.roll_no}")

student1 = Student("Alice", 20, 101)
student1.display_student()

# Question 2: Vehicle and Car
print("\n" + "=" * 50)
print("Question 2: Single Inheritance - Vehicle & Car")
print("=" * 50)

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def show_brand(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    
    def show_model(self):
        print(f"Model: {self.model}")

car1 = Car("Toyota", "Camry")
car1.show_brand()
car1.show_model()

# ===== 2. MULTILEVEL INHERITANCE =====

# Question 3: Animal -> Dog -> Puppy
print("\n" + "=" * 50)
print("Question 3: Multilevel Inheritance - Animal->Dog->Puppy")
print("=" * 50)

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Puppy(Dog):
    def weep(self):
        print("Puppy is weeping")

puppy1 = Puppy()
puppy1.eat()
puppy1.bark()
puppy1.weep()

# Question 4: Person -> Employee -> Manager
print("\n" + "=" * 50)
print("Question 4: Multilevel Inheritance - Person->Employee->Manager")
print("=" * 50)

class Person2:
    def __init__(self, name):
        self.name = name

class Employee(Person2):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def display_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")

manager1 = Manager("Bob", 50000, "IT")
manager1.display_details()

# ===== 3. MULTIPLE INHERITANCE =====

# Question 5: Father and Mother -> Child
print("\n" + "=" * 50)
print("Question 5: Multiple Inheritance - Father & Mother -> Child")
print("=" * 50)

class Father:
    def bike(self):
        print("Father rides a bike")

class Mother:
    def jewellery(self):
        print("Mother wears jewellery")

class Child(Father, Mother):
    pass

child1 = Child()
child1.bike()
child1.jewellery()

# Question 6: Teacher and Researcher -> Professor
print("\n" + "=" * 50)
print("Question 6: Multiple Inheritance - Teacher & Researcher -> Professor")
print("=" * 50)

class Teacher:
    def teach(self):
        print("Professor is teaching")

class Researcher:
    def research(self):
        print("Professor is researching")

class Professor(Teacher, Researcher):
    pass

prof1 = Professor()
prof1.teach()
prof1.research()

# ===== 4. HIERARCHICAL INHERITANCE =====

# Question 7: Shape -> Circle, Rectangle, Triangle
print("\n" + "=" * 50)
print("Question 7: Hierarchical Inheritance - Shape with multiple children")
print("=" * 50)

class Shape:
    pass

class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a Rectangle")

class Triangle(Shape):
    def draw(self):
        print("Drawing a Triangle")

circle1 = Circle()
rect1 = Rectangle()
tri1 = Triangle()

circle1.draw()
rect1.draw()
tri1.draw()

# Question 8: Employee -> Developer, Tester
print("\n" + "=" * 50)
print("Question 8: Hierarchical Inheritance - Employee->Developer, Tester")
print("=" * 50)

class Employee2:
    def work(self):
        print("Employee is working")

class Developer(Employee2):
    def work(self):
        print("Developer is coding")

class Tester(Employee2):
    def work(self):
        print("Tester is testing")

dev1 = Developer()
test1 = Tester()

dev1.work()
test1.work()

# ===== 5. HYBRID INHERITANCE =====

# Question 9: A -> B, C -> D
print("\n" + "=" * 50)
print("Question 9: Hybrid Inheritance - Diamond Pattern A->B,C->D")
print("=" * 50)

class A:
    def methodA(self):
        print("Method A called")

class B(A):
    def methodB(self):
        print("Method B called")

class C(A):
    def methodC(self):
        print("Method C called")

class D(B, C):
    def methodD(self):
        print("Method D called")

d1 = D()
d1.methodA()
d1.methodB()
d1.methodC()
d1.methodD()

# Question 10: Employee -> Manager, Developer -> TeamLead
print("\n" + "=" * 50)
print("Question 10: Hybrid Inheritance - Company Structure")
print("=" * 50)

class Employee3:
    def __init__(self, name):
        self.name = name
    
    def manage(self):
        print(f"{self.name} is managing")

class Manager2(Employee3):
    def manage(self):
        print(f"{self.name} is managing team")

class Developer2(Employee3):
    def develop(self):
        print(f"{self.name} is developing code")

class TeamLead(Manager2, Developer2):
    pass

lead1 = TeamLead("Charlie")
lead1.manage()
lead1.develop()

# ===== 6. CONSTRUCTOR-BASED QUESTIONS =====

# Question 11: Person -> Student with constructors
print("\n" + "=" * 50)
print("Question 11: Constructor Inheritance - Person->Student")
print("=" * 50)

class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student2(Person3):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}")

student2 = Student2("Diana", 21, 201)
student2.display()

# Question 12: Vehicle -> Car with constructors
print("\n" + "=" * 50)
print("Question 12: Constructor Inheritance - Vehicle->Car")
print("=" * 50)

class Vehicle2:
    def __init__(self, brand):
        self.brand = brand

class Car2(Vehicle2):
    def __init__(self, brand, model, price):
        super().__init__(brand)
        self.model = model
        self.price = price
    
    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}")

car2 = Car2("Honda", "Civic", 25000)
car2.display()

# ===== 7. REAL-TIME QUESTIONS =====

# Question 13: Banking System - Account -> SavingsAccount
print("\n" + "=" * 50)
print("Question 13: Banking System - Account->SavingsAccount")
print("=" * 50)

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    
    def display_info(self):
        print(f"Account No: {self.account_number}, Balance: ${self.balance}, Interest Rate: {self.interest_rate}%")

savings1 = SavingsAccount("ACC123", 10000, 4.5)
savings1.display_info()

# Question 14: School Management - Person -> Teacher
print("\n" + "=" * 50)
print("Question 14: School Management - Person->Teacher")
print("=" * 50)

class Person4:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher2(Person4):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Subject: {self.subject}")

teacher1 = Teacher2("Mr. Smith", 35, "Mathematics")
teacher1.display_details()

# Question 15: Online Shopping - Product -> Electronics
print("\n" + "=" * 50)
print("Question 15: Online Shopping - Product->Electronics")
print("=" * 50)

class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

class Electronics(Product):
    def __init__(self, product_name, price, warranty):
        super().__init__(product_name, price)
        self.warranty = warranty
    
    def display_info(self):
        print(f"Product: {self.product_name}, Price: ${self.price}, Warranty: {self.warranty} years")

electronics1 = Electronics("Laptop", 999, 2)
electronics1.display_info()

print("\n" + "=" * 50)
print("All 15 OOP Inheritance Questions Completed!")
print("=" * 50)