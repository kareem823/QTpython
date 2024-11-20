#create one variable to store 1 number
num1 = 0
#create a 2nd var to store a 2nd number.
num2 = 0

#get user input with type checking
try:
    num1 = int(input("enter the first number: "))
    num2 = int(input("enter the second number: "))
except ValueError:
    print("Error: Please enter valid numbers only!")
    exit()

#add the two numbers and store the result in a 3rd variable.
result = num1+num2

#display the addition operation in the console.
print(f"{num1} + {num2} = {result}")
#print the result.

