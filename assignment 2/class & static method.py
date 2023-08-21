# Class Methods:
#
# A class method is a method that belongs to the class and is bound to it rather than to an instance of the class.
# It can access and modify the class-level variables and attributes.
# Class methods are defined using the @classmethod decorator and accept the class itself as the first parameter conventionally named cls.
# Class methods are often used to create alternative constructors or perform operations that involve the class itself rather than an instance of the class.
# They can be called on both the class and the instances of the class.
#
# Static Methods:
#
# A static method is a method that belongs to the class, but it doesn't have access to the class or instance-specific data.
# It doesn't receive any implicit first parameter like self or cls.
# Static methods are defined using the @staticmethod decorator.
# They are typically used to define utility or helper methods that don't require access to instance-specific or class-specific data.
# Static methods can be called on both the class and the instances of the class, but they are more commonly invoked using the class name.


class MyClass:
    class_variable = "Hello, I'm a class variable."

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def class_method(cls):
        print("This is a class method.")
        print("Accessing class variable:", cls.class_variable)

    @staticmethod
    def static_method():
        print("This is a static method.")

# Calling the class method
MyClass.class_method()

# Creating an instance
obj = MyClass("I'm an instance.")

# Calling the class method using the instance
obj.class_method()

# Calling the static method
MyClass.static_method()

# Calling the static method using the instance
obj.static_method()