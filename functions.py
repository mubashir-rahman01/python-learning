def greet():
    print("Hi there");
    print("Welcome aboard")
    
# greet()



# quit using a function and while loop
command = ""
def quit():
    global command
    while command.lower() != "quit":
        command = input("Enter a command (type 'quit' to exit):")
        print("You entered: ", command)

# quit()

# even numbers in a range using keyword aguments
def print_even(start=0, end=10):
    count = 0
    for i in range(start, end):
        if(i %2 == 0):
            count += 1
            print(i)
    
    print("We have " + str(count) + " even numbers in the range of " + str(start) + " to " + str(end));   

#print_even(11, end=20)  # start and end are keyword arguments, they can be passed in any order.
    
# multiply using xargs
def multiply(*args):
    total = 1
    for number in args:
        total *= number
    return total

# print("Start multiply");
# print(multiply(2, 3, 4, 5));

def greet_users(greeting, *names):
    for name in names:
        print(f"{greeting} {name}")
        
# greet_users("Hello", "Alice", "Tobias", "Charlie");


def greet_users_with_kwargs(greeting, **kwargs): 
    for key, value in kwargs.items():
        print(f"{greeting} {value} ({key})")
        
greet_users_with_kwargs("Hello", user1="Alice", user2="Tobias", user3="Charlie");
    
# If a function does not have a return statement, it will return None by default.
    
    