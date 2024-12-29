#2. Write a basic function to greet students

def greet_student(name):
    print(f"Hello, {name}! Welcome to the class.")


greet_student("Rahul")
greet_student("Rohit")


#6. Write a code that generates the squares of numbers from 1 to n using a generator

def square_generator(n):
    for i in range(1, n + 1):
        yield i ** 2


n = 5
squares = square_generator(n)

for square in squares:
    print(square)


#7. Write a code that generates palindromic numbers up to n using a generator.

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def palindrome_generator(n):
    for i in range(1, n + 1):
        if is_palindrome(i):
            yield i

n = 100
palindromes = palindrome_generator(n)

for palindrome in palindromes:
    print(palindrome)


#8. Write a code that generates even numbers from 2 to n using a generator.

def even_number_generator(n):
    for i in range(2, n + 1, 2):
        yield i


n = 20

evens = even_number_generator(n)

for even in evens:
    print(even)


#9. Write a code that generates powers of two up to n using a generator.

def power_of_two_generator(n):
    power = 1
    while power <= n:
        yield power
        power *= 2


n = 100
powers_of_two = power_of_two_generator(n)

for power in powers_of_two:
    print(power)


#10. Write a code that generates prime numbers up to n using a generator.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator(n):
    for i in range(2, n + 1):
        if is_prime(i):
            yield i


n = 30
primes = prime_generator(n)

for prime in primes:
    print(prime)


#11. Write a code that uses a lambda function to calculate the sum of two numbers.

sum_numbers = lambda a, b: a + b


result = sum_numbers(5, 3)
print(result)


#12. Write a code that uses a lambda function to calculate the square of a given number.

square = lambda x: x ** 2
result = square(5)
print(result)

#13. Write a code that uses a lambda function to check whether a given number is even or odd.

even_or_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
result = even_or_odd(7)
print(result) 

result = even_or_odd(4)
print(result) 


#15. Write a code that uses a lambda function to concatenate two strings.

concatenate = lambda str1, str2: str1 + str2
result = concatenate("Hello, ", "World!")
print(result)


#16. Write a code that uses a lambda function to find the maximum of three given numbers.

max_of_three = lambda a, b, c: max(a, b, c)
result = max_of_three(5, 9, 3)
print(result)


#17. Write a code that generates the squares of even numbers from a given list.

def square_of_even_numbers(lst):
    for num in lst:
        if num % 2 == 0:
            yield num ** 2

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
squares_of_evens = square_of_even_numbers(numbers)

for square in squares_of_evens:
    print(square)


#18. Write a code that calculates the product of positive numbers from a given list.

from functools import reduce
def product_of_positive_numbers(lst):
    
    positive_numbers = filter(lambda x: x > 0, lst)
    return reduce(lambda x, y: x * y, positive_numbers, 1)


numbers = [1, -2, 3, 4, -5, 6]
product = product_of_positive_numbers(numbers)
print(product)

#19. Write a code that doubles the values of odd numbers from a given list.
def double_odd_numbers(lst):
    for num in lst:
        if num % 2 != 0:
            yield num * 2
        else:
            yield num

numbers = [1, 2, 3, 4, 5, 6]
doubled_odds = double_odd_numbers(numbers)

for number in doubled_odds:
    print(number)


#20. Write a code that calculates the sum of cubes of numbers from a given list.

def sum_of_cubes(lst):
    return sum(x ** 3 for x in lst)


numbers = [1, 2, 3, 4]
result = sum_of_cubes(numbers)
print(result)


#21. Write a code that filters out prime numbers from a given list.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_primes(lst):
    return [num for num in lst if is_prime(num)]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primes = filter_primes(numbers)
print(primes)


#22. Write a code that uses a lambda function to calculate the sum of two numbers.

sum_numbers = lambda a, b: a + b
result = sum_numbers(5, 3)
print(result)



#23. Write a code that uses a lambda function to calculate the square of a given number.

square = lambda x: x ** 2

result = square(4)
print(result)



#24. Write a code that uses a lambda function to check whether a given number is even or odd.

even_or_odd = lambda x: "Even" if x % 2 == 0 else "Odd"

result = even_or_odd(7)
print(result) 

result = even_or_odd(4)
print(result)


#25. Write a code that uses a lambda function to concatenate two strings.


concatenate = lambda str1, str2: str1 + str2

result = concatenate("Hello, ", "World!")
print(result)


#26. Write a code that uses a lambda function to find the maximum of three given numbers.

max_of_three = lambda a, b, c: max(a, b, c)

result = max_of_three(5, 9, 3)
print(result)



#32. Define a parent class Animal with a method make_sound that prints "Generic animal sound". Create a child class Dog inheriting from Animal with a method make_sound that prints "Woof!".
class Animal:
    def make_sound(self):
        print("Generic animal sound")


class Dog(Animal):
    def make_sound(self):
        print("Woof!")


animal = Animal()
animal.make_sound()  

dog = Dog()
dog.make_sound()    



#33. Define a method move in the Animal class that prints "Animal moves". Override the move method in the Dog class to print "Dog runs."

class Animal:
    def move(self):
        print("Animal moves")


class Dog(Animal):
    def move(self):
        print("Dog runs")


animal = Animal()
animal.move()  

dog = Dog()
dog.move() 


#34. Create a class Mammal with a method reproduce that prints "Giving birth to live young." Create a class DogMammal inheriting from both Dog and Mammal.


class Animal:
    def move(self):
        print("Animal moves")


class Dog(Animal):
    def move(self):
        print("Dog runs")


class Mammal:
    def reproduce(self):
        print("Giving birth to live young")


class DogMammal(Dog, Mammal):
    pass

dog_mammal = DogMammal()
dog_mammal.move()      
dog_mammal.reproduce()  


#35. Create a class German Shepherd inheriting from Dog and override the make_sound method to print "Bark!"


class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")


class GermanShepherd(Dog):
    def make_sound(self):
        print("Bark!")


dog = Dog()
dog.make_sound()  

german_shepherd = GermanShepherd()
german_shepherd.make_sound()  


#36. Define constructors in both the Animal and Dog classes with different initialization parameters.

class Animal:
    def __init__(self, species):
        self.species = species
        print(f"Animal constructor called. Species: {self.species}")


class Dog(Animal):
    def __init__(self, species, breed):

        super().__init__(species)
        self.breed = breed
        print(f"Dog constructor called. Breed: {self.breed}")


animal = Animal("Generic Animal")


dog = Dog("Dog", "German Shepherd")


#41 . Can you provide an example of how abstraction can be utilized to create a common interface for a group of related classes in Python?

'''Abstraction can define a common interface for a group of related classes by using an abstract base class (ABC). 
Each subclass implements the interface differently while maintaining a consistent way to interact with them.
'''
from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass 


class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of rupess{amount:500}")


class PhonepayProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing Phonepay payment of rupess{amount:600}")


class BankTransferProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing bank transfer payment of rupess{amount:700}")


def make_payment(processor: PaymentProcessor, amount: float):
    processor.process_payment(amount)


credit_card = CreditCardProcessor()
Phonepay = PhonepayProcessor()
bank_transfer = BankTransferProcessor()

make_payment(credit_card, 500.0)  
make_payment(Phonepay, 600.0)      
make_payment(bank_transfer, 700.0) 


#43. Define a base class with a method and a subclass that overrides the method.
'''
example demonstrating a base class with a method and a subclass that overrides it
'''

class Vehicle:
    def start(self):
        return "Starting the vehicle"

class Car(Vehicle):
    def start(self):
        return "Starting the car"


vehicle = Vehicle()
car = Car()

print(vehicle.start())  
print(car.start())    


#44. Define a base class and multiple subclasses with overridden methods.
'''example demonstrating a base class and multiple subclasses, each overriding a method
'''

class Animal:
    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

class Cow(Animal):
    def sound(self):
        return "Moo!"


dog = Dog()
cat = Cat()
cow = Cow()


print(dog.sound())  
print(cat.sound())  
print(cow.sound())  


#49. Implement a class BankAccount with a private balance attribute. Include methods to deposit, withdraw, and check the balance.

class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def check_balance(self):
        print(f"Current balance: ${self.__balance}")

# Example
account = BankAccount(100)
account.deposit(50)      
account.withdraw(30)     
account.check_balance()  
account.withdraw(150)    




#50. Develop a Person class with private attributes name and email, and methods to set and get the email.
class Person:
    def __init__(self, name, email):
        self.__name = name        
        self.__email = email      

    
    def get_email(self):
        return self.__email

    
    def set_email(self, email):
        
        if "@" in email:
            self.__email = email
            print(f"Email updated to: {self.__email}")
        else:
            print("Invalid email address.")

    
    def get_name(self):
        return self.__name


person = Person("John Doe", "raju.123@gmail.com")
print(person.get_name())  
print(person.get_email()) 


person.set_email("raju.123@gmail.com")  
print(person.get_email()) 


#52. Create a decorator in Python that adds functionality to a simple function by printing a message before and after the function execution.
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Starting function execution...")
        result = func(*args, **kwargs)
        print("Function execution completed.")
        return result
    return wrapper


@simple_decorator
def example_function():
    print("This is the main function body.")


example_function()





#53. Modify the decorator to accept arguments and print the function name along with the message.
def message_decorator_with_args(before_message, after_message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{before_message} - Function: {func.__name__}")
            result = func(*args, **kwargs)
            print(f"{after_message} - Function: {func.__name__}")
            return result
        return wrapper
    return decorator


@message_decorator_with_args("Starting execution", "Finished execution")
def sample_function():
    print("This is the function body.")




#54. Create two decorators, and apply them to a single function. Ensure that they execute in the order they are applied.

def decorator_one(func):
    def wrapper(*args, **kwargs):
        print("Decorator One: Before function execution")
        result = func(*args, **kwargs)
        print("Decorator One: After function execution")
        return result
    return wrapper

def decorator_two(func):
    def wrapper(*args, **kwargs):
        print("Decorator Two: Before function execution")
        result = func(*args, **kwargs)
        print("Decorator Two: After function execution")
        return result
    return wrapper


@decorator_one
@decorator_two
def my_function():
    print("This is the main function.")



#55. Modify the decorator to accept and pass function arguments to the wrapped function
def decorator_one(func):
    def wrapper(*args, **kwargs):
        print("Decorator One: Before function execution")
        result = func(*args, **kwargs)
        print("Decorator One: After function execution")
        return result
    return wrapper

def decorator_two(func):
    def wrapper(*args, **kwargs):
        print("Decorator Two: Before function execution")
        result = func(*args, **kwargs)
        print("Decorator Two: After function execution")
        return result
    return wrapper


@decorator_one
@decorator_two
def my_function(a, b):
    print(f"This is the main function. Arguments: a={a}, b={b}")
    return a + b


result = my_function(3, 5)
print(f"Result: {result}")




#56. Create a decorator that preserves the metadata of the original function.
import functools

def metadata_preserving_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Before function execution")
        result = func(*args, **kwargs)
        print("After function execution")
        return result
    return wrapper


@metadata_preserving_decorator
def my_function(a, b):
    
    return a + b


print(f"Function name: {my_function.__name__}")
print(f"Function docstring: {my_function.__doc__}")


result = my_function(3, 5)
print(f"Result: {result}")



#57. Create a Python class 'Calculator with a static method 'add' that takes in two numbers and returns their sum.
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

result = Calculator.add(10, 20)
print(f"The sum is: {result}")




#58. Create a Python class Employee' with a class 'method get_employee_count that returns the total number of employees created.
class Employee:
    employee_count = 0  

    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1

    @classmethod
    def get_employee_count(cls):
        return cls.employee_count


e1 = Employee("Rahul")
e2 = Employee("Nayan")
e3 = Employee("Rohit")


print(f"Total employees: {Employee.get_employee_count()}")




#59. Create a Python class 'StringFormatter with a static method 'reverse_string that takes a string as input and returns its reverse.
class StringFormatter:
    @staticmethod
    def reverse_string(input_string):
        return input_string[::-1]


result = StringFormatter.reverse_string("hello")
print(f"Reversed string: {result}")




#60. Create a Python class 'Circle` with a class method 'calculate_area that calculates the area of a circle given its radius.
import math

class Circle:
    @classmethod
    def calculate_area(cls, radius):
        return math.pi * radius**2


radius = 5
area = Circle.calculate_area(radius)
print(f"The area of the circle with radius {radius} is: {area:.2f}")




#61. Create a Python class Temperature Converter with a static method celsius_to_fahrenheit that converts Celsius to Fahrenheit.
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32


celsius_temp = 25
fahrenheit_temp = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is equal to {fahrenheit_temp:.2f}°F")




#62 Example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age})"


person1 = Person("Alice", 30)


print(person1)



#63 Example
class BookCollection:
    def __init__(self, books):
        self.books = books
    
    def __len__(self):
        return len(self.books)  


my_books = BookCollection(["Book1", "Book2", "Book3"])


print(f"The number of books in the collection is: {len(my_books)}")



#64 Example
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        raise TypeError("Unsupported operand type for +: 'Point' and '{}'".format(type(other).__name__))
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"


p1 = Point(2, 3)
p2 = Point(4, 5)


result = p1 + p2
print(result)


#65 Example
class CustomList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]


my_list = CustomList([10, 20, 30, 40, 50])


print(my_list[0]) 
print(my_list[2]) 




#66 example
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self  

    def __next__(self):
        if self.current > self.end:
            raise StopIteration  
        else:
            self.current += 1
            return self.current - 1


counter = Counter(1, 5)

for number in counter:
    print(number)



#67 example
class Circle:
    def __init__(self, radius):
        self._radius = radius  

    @property
    def radius(self):
        
        return self._radius

    @radius.setter
    def radius(self, value):
        
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def area(self):
        
        return 3.14159 * self._radius**2


circle = Circle(5)
print(f"Radius: {circle.radius}")  
print(f"Area: {circle.area}")      


circle.radius = 10
print(f"New Radius: {circle.radius}")
print(f"New Area: {circle.area}")




# 68 Example
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  

    @property
    def celsius(self):
        
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        self._celsius = value

    @property
    def fahrenheit(self):
        
        return (self._celsius * 9/5) + 32


temp = Temperature(25)  # Initialize with 25°C
print(f"Temperature in Celsius: {temp.celsius}")
print(f"Temperature in Fahrenheit: {temp.fahrenheit}")


temp.celsius = 30
print(f"Updated Temperature in Celsius: {temp.celsius}")
print(f"Updated Temperature in Fahrenheit: {temp.fahrenheit}")


try:
    temp.celsius = -300
except ValueError as e:
    print(e)


#69 Example
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        
        return self._width

    @width.setter
    def width(self, value):
        
        if value <= 0:
            raise ValueError("Width must be positive.")
        self._width = value

    @property
    def height(self):
        
        return self._height

    @height.setter
    def height(self, value):
        
        if value <= 0:
            raise ValueError("Height must be positive.")
        self._height = value

    @property
    def area(self):
        
        return self._width * self._height


rect = Rectangle(10, 20)
print(f"Width: {rect.width}, Height: {rect.height}, Area: {rect.area}")


rect.width = 15
rect.height = 25
print(f"Updated Width: {rect.width}, Updated Height: {rect.height}, Updated Area: {rect.area}")


try:
    rect.width = -5
except ValueError as e:
    print(e)


#70 Example
class Person:
    def __init__(self, name):
        self._name = name  

    @property
    def name(self):
        
        return self._name

    @name.setter
    def name(self, value):
        
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value

    @name.deleter
    def name(self):
       
        print(f"Deleting name: {self._name}")
        self._name = None  # Clear the name


person = Person("Rahul")
print(f"Name: {person.name}")


person.name = "Nayan"
print(f"Updated Name: {person.name}")


del person.name
print(f"Name after deletion: {person.name}")



#71 Example
class BankAccount:
    def __init__(self, account_holder, balance):
        self._account_holder = account_holder 
        self._balance = balance 

    @property
    def balance(self):
        
        return self._balance

    @balance.setter
    def balance(self, amount):
       
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = amount

    @property
    def account_holder(self):
        """Getter for account_holder."""
        return self._account_holder




account = BankAccount("Rahul", 1000)


print(f"Account Holder: {account.account_holder}")
print(f"Balance: {account.balance}")


account.balance = 1500
print(f"Updated Balance: {account.balance}")


try:
    account.balance = -500
except ValueError as e:
    print(e)


try:
    account.account_holder = "Nayan"
except AttributeError as e:
    print(e)
