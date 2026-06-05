# Q1: Banking Application - Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("Withdrawn:", amount)

acc = BankAccount(5000)
acc.deposit(1000)
acc.withdraw(500)
print()

# Q2: Student Management - Encapsulation
class Student:
    def __init__(self, name, reg_no):
        self.name = name
        self.reg_no = reg_no
    
    def update_name(self, new_name):
        self.name = new_name

s = Student("Raj", "123")
print("Reg No:", s.reg_no)
s.update_name("Rajesh")
print("Name:", s.name)
print()

# Q3: Payment System - Abstraction
class UPI:
    def pay(self, amount):
        print("Paid via UPI:", amount)

class CreditCard:
    def pay(self, amount):
        print("Paid via Card:", amount)

class NetBanking:
    def pay(self, amount):
        print("Paid via NetBanking:", amount)

upi = UPI()
upi.pay(500)
print()

# Q4: Car Driver - Abstraction
class Car:
    def accelerate(self):
        print("Car accelerating")
    
    def brake(self):
        print("Car braking")

car = Car()
car.accelerate()
car.brake()
print()

# Q5: Organization - Inheritance
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

m = Manager("Alice", 80000, 5)
d = Developer("Bob", 60000, "Python")
print("Manager:", m.name, m.team_size)
print("Developer:", d.name, d.language)
print()

# Q6: Vehicle - Inheritance
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

class Car2(Vehicle):
    pass

class Bike(Vehicle):
    pass

class Truck(Vehicle):
    pass

c = Car2("Honda", 200)
b = Bike("Harley", 180)
t = Truck("Volvo", 120)
print("Car:", c.brand)
print("Bike:", b.brand)
print("Truck:", t.brand)
print()

# Q7: Notification - Polymorphism
class Email:
    def send_notification(self, msg):
        print("Email:", msg)

class SMS:
    def send_notification(self, msg):
        print("SMS:", msg)

class WhatsApp:
    def send_notification(self, msg):
        print("WhatsApp:", msg)

e = Email()
s = SMS()
w = WhatsApp()
e.send_notification("Hello")
s.send_notification("Hello")
w.send_notification("Hello")
print()

# Q8: Shape - Polymorphism
class Circle:
    def __init__(self, r):
        self.r = r
    
    def calculate_area(self):
        area = 3.14 * self.r * self.r
        print("Circle area:", area)

class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w
    
    def calculate_area(self):
        area = self.l * self.w
        print("Rectangle area:", area)

class Triangle:
    def __init__(self, b, h):
        self.b = b
        self.h = h
    
    def calculate_area(self):
        area = 0.5 * self.b * self.h
        print("Triangle area:", area)

c = Circle(5)
r = Rectangle(4, 6)
t = Triangle(3, 8)
c.calculate_area()
r.calculate_area()
t.calculate_area()
print()

# Q9: Food Delivery App - Mixed
class Customer:
    def __init__(self, name):
        self.name = name

class PremiumCustomer(Customer):
    def __init__(self, name, points):
        super().__init__(name)
        self.points = points

class CardPayment:
    def process(self, amount):
        print("Paid via Card:", amount)

class WalletPayment:
    def process(self, amount):
        print("Paid via Wallet:", amount)

class BikeDelivery:
    def charge(self, distance):
        total = distance * 5
        print("Bike charge:", total)

class CarDelivery:
    def charge(self, distance):
        total = distance * 10
        print("Car charge:", total)

cust = PremiumCustomer("John", 500)
card = CardPayment()
bike = BikeDelivery()
card.process(100)
bike.charge(5)
print()

# Q10: Hospital Management - All 4 Pillars
class Patient:
    def __init__(self, name):
        self.name = name
        self.records = []

class Doctor:
    def __init__(self, name):
        self.name = name
    
    def calculate_salary(self, base):
        total = base + (base * 0.2)
        print("Doctor salary:", total)

class Nurse:
    def __init__(self, name):
        self.name = name
    
    def calculate_salary(self, base):
        total = base + (base * 0.1)
        print("Nurse salary:", total)

p = Patient("Emma")
doc = Doctor("Dr. Smith")
nurse = Nurse("Nurse Johnson")
doc.calculate_salary(5000)
nurse.calculate_salary(3000)