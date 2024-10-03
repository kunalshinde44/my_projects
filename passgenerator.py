import random
import string

def generate_password(length):
    # Define the characters to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters from the pool
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Prompt the user to input the desired password length
    while True:
        try:
            length = int(input("Enter the desired length of the password (e.g., 8, 12, 16): "))
            if length < 1:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print(f"Your generated password is: {password}")

# Run the main function
if __name__ == "__main__":
    main()
