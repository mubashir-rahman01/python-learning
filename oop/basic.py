# Python is an object oriented programming language. Object oriented programming language revolve around the concept of classes and objects
# A class is a template or a blueprint for creating an object. For example Human is class for each humans.
# An object is an instance or small piece that contain all properties of a class. e.g Ali is an object of class "Human"

class Person:
    
    default_color = "red" # class level attribute
    
    def __init__(self,name, age): # init method automatically calls when someone invoke it
        self.name = name
        self.age = age
    
    # self paramter is a reference to current object of the class. If self is not there, class would not know which instance it has too associate
        
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} and my education is {self.education}")
        
person = Person("Ali", 25);
person.education = "Masters"
print(person.default_color);
print(Person.default_color)


person.introduce() # it will print same values
        
