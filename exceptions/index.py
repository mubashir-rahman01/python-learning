# exceptions are used to control or handle an unexpected errors which blocks the further executions of program.
# try:
#     file = open("sample.txt")
try:
    x = input("Enter value of x:");
    
    # to raise an exception, we will use raise keyword
    if int(x) <= -1:
        raise ValueError("x cannot be negative")
    
    y = 10;
    print("ans of y/x:", y/int(x))
    # file.write("Lorem ipsum")
    
except ValueError as error:
    print(error)
    
except (NameError, ZeroDivisionError):
    print("Please enter correct value for x and y")
    
    
else:
    print("Else block will be executed")

    # finally: 
    #     file.close()

# except:
#     print("The file you want to write is not found")
    