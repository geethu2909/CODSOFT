import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Main program
def main():
    # Prompt the user to specify the length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Password length must be at least 1.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Generate and display the password
    password = generate_password(length)
    print("Generated password:", password)

# Run the main program
if __name__ == "__main__":
    main()

