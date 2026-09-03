# inheritance allow user to inherit mehtods and properties from parent class to use in child class
class Person:
  def __init__(self, fname, lname):
    self.first_name = fname
    self.last_name = lname

  def print_name(self):
    print(self.first_name, self.last_name)
    

class Student(Person):
    # pass  # remove it to override functions

    def __init__(self, fname, lname, age, year):
        super().__init__(fname, lname) # super method inherit all the properties and methods from parent
        self.age = age
        self.year = year
        
        # this pattern is called method overriding, which is a function can have different implementation in the subclass
    
    def welcome(self):
        print(f"Welcome {self.first_name} {self.last_name} to the class of {self.year} ")
   
x = Person("John", "Doe");
# x.print_name()
         
s = Student("Ali", "Ahmad", 25, 2019)
s.print_name()
s.welcome()