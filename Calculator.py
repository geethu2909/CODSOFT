# Simple Calculator

# Function to perform the calculation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

# Main program
def main():
    # Prompt user to input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Prompt user to input the operation
    print("Choose the operation:")
    print("+ for addition")
    print("- for subtraction")
    print("* for multiplication")
    print("/ for division")
    operation = input("Enter the operation: ")
    
    # Perform the calculation and display the result
    result = calculate(num1, num2, operation)
    print("The result is:", result)

# Run the main program
if __name__ == "__main__":
    main()

