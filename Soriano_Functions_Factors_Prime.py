# Function to find the smallest factor of a number
def smallest_factor(n):
    if n < 2:
        return None  # No smallest factor for numbers less than 2
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return n  # If n is a prime number, its smallest factor is itself

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to find prime numbers in a given range
def display_primes_in_range(start, end):
    if start < 0:
        print("Please enter a non-negative number.")
        return

    if end <= start:
        print(f"Enter a number greater than {start}.")
        return

    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")

# The Main Program
while True:
    print("Select an option:")
    print("1. Find the smallest factor of a number")
    print("2. Find prime numbers in a range")
    print("0. Terminate the program")

    choice = int(input("Enter your choice: "))

    if choice == 0:
        print("The Program has been terminated.")
        break
    elif choice == 1:
        number = int(input("Enter the number: "))
        factor = smallest_factor(number)
        if factor is None:
            print(f"{number} has no smallest factor.")
        else:
            print(f"The smallest factor of {number} is: {factor}")
    elif choice == 2:
        start = int(input("Enter the start number: "))
        end = int(input("Enter the end number: "))
        display_primes_in_range(start, end)
        print("\n")
    else:
        print("Invalid choice. Please enter 0, 1, or 2.")
