# Question 1

def add(a, b):
    return a + b

def subtract(a, b):
    return (a - b)

def multiply(a, b):
    return (a * b)

def division(a, b):
    if b != 0:
        return (a / b) 


num1 = int(input(f"Enter first number: "))
num2 = int(input(f"Enter second number: "))

print(num1)
print(num1)

print("choose Arithmetic Operation (choose operation +, -, *, /) or \'exit\' to quit: ")

while True:
    choice = input(f"Select choice 1/2/3/4")
    if choice == '1':
        print("Result: ", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid Choice")
    break





# # Question 2
# while True:
#     user_input = input("Enter a number (or type 'exit' to quit): ")
#     if user_input == "exit":
#         print("Goodbye!")
#         break 
    
#     num = int(user_input)  
    
#     if num % 2 == 0:
#         print("The number is even")
#     else:
#         print("The number is odd")






# # Question 3
# while True:
#     age = input("Enter your age (or type exit to quit): ")
#     if age == 'exit': 
#         print("Goodbye!")
#         break
    
#     try:
#         age_int = int(age)
#         if age_int >= 18:
#             print("You can vote")
#         else:
#             print("You cannot vote")
#     except ValueError:
#         print("Invalid input")



