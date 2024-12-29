Function & OPPS Assignment

1.	 Explain the importance of function.
Answer - Functions in Python promote code reuse, modularity, readability, and easier debugging. They encapsulate logic, reduce duplication, improve scalability, and enable abstraction, making programs efficient, maintainable, and organized.

3.	 What is the difference between print and return statements?
Answer - Print: Outputs information to the console, primarily for user interaction or debugging. It doesn’t affect program logic or flow, as its result cannot be reused.
Return: Ends a function’s execution and sends a value back to the caller, enabling further computation or reuse in the program.

4.	What are *args and **kwargs?
Answer – *args: Allows functions to accept any number of positional arguments, accessible as a tuple.
**kwargs: Allows functions to accept any number of keyword arguments, accessible as a dictionary for key-value pairs.

5.	Explain the iterator function
Answer - An iterator function creates an iterator, an object implementing __iter__() and __next__(). It enables sequential access to elements in a collection, supporting efficient, lazy evaluation for looping without loading all elements into memory.

27. What is encapsulation in OOP?
Answer - Encapsulation in OOP is the practice of bundling data and methods into a single unit (class) and restricting access to some internal components. It ensures data protection, controlled access, and allows changes without affecting external code.

28 . Explain the use of access modifiers in Python classes.
Answer - Access modifiers in Python classes control the accessibility of class members (attributes and methods) from outside the class. They help enforce encapsulation, ensuring that certain parts of a class are exposed only as needed while others remain hidden

29. What is inheritance in OOP?
Answer - Inheritance in OOP enables a subclass to acquire properties and methods of a parent class, promoting code reuse and hierarchical relationships. Subclasses can extend or override parent behavior. Types include single, multiple, multilevel, and hierarchical inheritance. It simplifies maintenance, supports polymorphism, but requires careful use to avoid complexity.

30. Define polymorphism in OOP.
Answer - Polymorphism in OOP allows objects of different classes to be treated as objects of a common superclass, enabling a single interface to represent different underlying forms (methods or behaviors). It supports method overriding and overloading, enhancing flexibility and extensibility in code by enabling dynamic method resolution during runtime.

31. Explain method overriding in Python.
Answer -  Method overriding in Python occurs when a subclass provides a specific implementation for a method that is already defined in its parent class. The subclass method overrides the parent class method, and the overridden version is called when invoked on an object of the subclass. This enables polymorphism and allows the subclass to modify or extend the behavior of the parent class method.

37. What is abstraction in Python? How is it implemented?
Answer - Abstraction in Python is a concept that hides the complex implementation details and only exposes the essential features of an object. It simplifies the interface by allowing users to interact with objects through abstract methods. Abstraction is implemented using abstract classes and methods, typically through the (abc) module.

38. Explain the importance of abstraction in object-oriented programming.
Answer - Abstraction in object-oriented programming simplifies complexity by hiding implementation details and exposing only essential features. It enhances code readability, reusability, and maintainability, while promoting encapsulation and supporting polymorphism. By focusing on what an object does rather than how it works, abstraction allows for flexible, scalable designs, enabling developers to build modular, robust systems that are easier to understand and manage.

39. How are abstract methods different from regular methods in Python?
Answer - Abstract methods, defined with @abstractmethod in abstract classes, lack implementation and must be overridden in subclasses. Regular methods have implementations, can exist in any class, and are optional to override, allowing the class to be instantiated directly.


40. How can you achieve abstraction using interfaces in Python?
Answer - In Python, abstraction can be achieved using interfaces, which are implemented as abstract base classes (ABC) with only abstract methods. ABC are defined using the abc module. Subclasses must implement all the abstract methods to provide specific functionality.

42. How does Python achieve polymorphism through method overriding?
Answer - Python achieves polymorphism through method overriding by allowing subclasses to redefine methods from their superclass. At runtime, the appropriate method is called based on the object type, enabling consistent interfaces while allowing class-specific behavior.

45. How does polymorphism improve code readability and reusability?
Answer - Polymorphism improves code readability by providing a consistent interface, allowing methods to be called without knowing the object type. It enhances reusability by enabling generic functions to work with various objects, promoting flexibility and reducing the need for repetitive code.

46. Describe how Python supports polymorphism with duck typing.
Answer - Python supports polymorphism through duck typing, where an object's suitability is determined by its methods, not its class. If an object implements the required methods (e.g., speak()), it can be used interchangeably with other objects, enabling polymorphism without explicit inheritance, fostering flexibility and simplicity in code.

45. How does polymorphism improve code readability and reusability?
Answer - Polymorphism improves code readability by allowing a unified interface for diverse object types, reducing conditionals, and enhancing abstraction. It boosts reusability by enabling flexible code that works with different objects, adhering to the Open/Closed Principle. This dynamic behavior allows seamless extensions without altering existing code, ensuring modularity and maintainability.


46. Describe how Python supports polymorphism with duck typing.
Answer - Python supports polymorphism with duck typing, focusing on an object's behavior rather than its type. If an object implements the expected methods, it can be used interchangeably. For example, different classes with a speak() method can work with the same function. This dynamic typing enhances flexibility and reduces strict hierarchies but may lead to runtime errors if methods are missing.

47. How do you achieve encapsulation in Python?
Answer - Encapsulation in Python restricts access to a class's attributes and methods using access modifiers. Public members are freely accessible, protected members (prefixed with _) are intended for subclasses, and private members (prefixed with __) use name mangling to limit access. Getters and setters provide controlled access, ensuring data protection, modularity, and maintaining code integrity.

48. Can encapsulation be bypassed in Python? If so, how?
Answer - Yes, encapsulation can be bypassed in Python. Private members (with __) undergo name mangling, allowing access via _ClassName__private. Protected members (with _) are merely a convention and can be accessed directly. Additionally, functions like getattr() and setattr() allow dynamic access to any attribute, including private ones. However, bypassing encapsulation is generally discouraged for code integrity.

51. Why is encapsulation considered a pillar of object-oriented programming (OOP)?
Answer - Encapsulation is a key OOP pillar as it protects an object's internal state by restricting direct access to its attributes. It ensures data integrity through controlled access via methods (getters/setters), promotes modularity by hiding implementation details, and enhances maintainability and reusability. This abstraction reduces complexity, allowing easier updates without affecting external code, improving overall software design.


62. What is the purpose of the __ str__ () method in Python classes? Provide an example.
Answer - The __str__() method in Python is used to define a human-readable string representation of an object. When you print an object or use the str() function on it, the __str__() method is called. If not defined, Python will use the default implementation, which usually returns a string like <__main__.ClassName object at memory_address>. By defining __str__(), you can provide a more meaningful string representation for the object.

63. How does the len__ () method work in Python? Provide an example.
Answer - In Python, the __len__() method is a special (or "magic") method that is used to define the behavior of the built-in len() function for a custom object. When you call len() on an instance of a class, Python internally calls the class's __len__() method to determine the length.
If a class does not define the __len__() method and you call len() on its instance, Python raises a TypeError.


64. Explain the usage of the__add__() method in Python classes. Provide an example.
Answer - The __add__() method in Python is a special method that defines the behavior of the + operator for instances of a class. By implementing __add__(), you can specify how two objects of a class should be added together.
If __add__() is not defined for a class and the + operator is used, Python will raise a TypeError.


65. What is the purpose of the __ getitem__() method in Python? Provide an example.
The __getitem__() method in Python is used to define the behavior of accessing items in an object using square brackets ([]). It allows objects of custom classes to mimic the behavior of built-in data types like lists or dictionaries.
When you use obj[key], Python internally calls obj.__getitem__(key).

66. Explain the usage of the__iter__() and __next__() methods in Python. Provide an example using iterators.
Answer - The __iter__() and __next__() methods define custom iterators in Python. __iter__() returns the iterator object, while __next__() retrieves the next item, raising StopIteration when done. These methods allow objects to be used in loops like for. Iterators are useful for sequentially accessing data.


67. What is the purpose of a getter method in Python? Provide an example demonstrating the use of a getter method using property decorators.
Answer - The purpose of a getter method in Python is to retrieve the value of an attribute while providing an opportunity to include additional logic (e.g., validation or formatting). Using property decorators, getter methods allow for attribute access in an intuitive and Pythonic way, making the object feel like it exposes attributes directly while maintaining control.


68. Explain the role of setter methods in Python. Demonstrate how to use a setter method to modify a class attribute using property decorators.
Answer  - A setter method in Python is used to modify the value of an attribute while allowing additional logic, such as validation, logging, or triggering side effects. When combined with the @property decorator, setter methods enable attribute-like syntax for setting values while maintaining control over the assignment process.

69. What is the purpose of the @property decorator in Python? Provide an example illustrating its usage.
Answer - The @property decorator in Python is used to define a method as a getter, allowing it to be accessed like an attribute. It is part of Python's property management mechanism, enabling controlled access to class attributes while hiding implementation details. It supports attribute-like syntax for reading, writing, and deleting properties, enhancing encapsulation and data validation.



70. Explain the use of the @deleter decorator in Python property decorators. Provide a code example demonstrating its application.
Answer - The @deleter decorator in Python is used with property decorators to define behavior when a property is deleted using the del statement. It allows you to customize the deletion of an attribute while maintaining encapsulation and control.


71. How does encapsulation relate to property decorators in Python? Provide an example showcasing encapsulation using property decorators.
Answer - Encapsulation in Python refers to the practice of restricting direct access to an object's attributes and controlling access through methods. Property decorators (@property, @setter, and @deleter) enhance encapsulation by providing a clean and intuitive way to manage access to private attributes while maintaining control over their behavior (e.g., validation, transformation).



