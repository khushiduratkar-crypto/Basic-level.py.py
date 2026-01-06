# Basic Level Python Programs Collection
# This file contains various basic Python programs for beginners

# Program 1: Simple Calculator
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculator():
    print("=== Simple Calculator ===")
    print("Operations: +, -, *, /")

    try:
        num1 = float(input("Enter first number: "))
        operation = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        else:
            result = "Invalid operation"

        print(f"Result: {result}")
    except ValueError:
        print("Please enter valid numbers")

# Program 2: Number Guessing Game
import random

def number_guessing_game():
    print("\n=== Number Guessing Game ===")
    print("I'm thinking of a number between 1 and 100")
    print("You have 7 attempts to guess it!")

    secret_number = random.randint(1, 100)
    attempts = 7

    while attempts > 0:
        try:
            guess = int(input(f"Enter your guess ({attempts} attempts left): "))

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed it in {8-attempts} attempts!")
                return

            attempts -= 1

        except ValueError:
            print("Please enter a valid number.")

    print(f"Sorry! The number was {secret_number}. Better luck next time!")

# Program 3: Temperature Converter
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    print("\n=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Choose conversion (1 or 2): ")

    try:
        if choice == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C = {fahrenheit:.2f}°F")
        elif choice == '2':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F = {celsius:.2f}°C")
        else:
            print("Invalid choice")
    except ValueError:
        print("Please enter a valid number")

# Program 4: BMI Calculator
def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def bmi_calculator():
    print("\n=== BMI Calculator ===")

    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Please enter positive values")
            return

        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError:
        print("Please enter valid numbers")

# Program 5: Simple Interest Calculator
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def simple_interest_calculator():
    print("\n=== Simple Interest Calculator ===")

    try:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter interest rate (%): "))
        time = float(input("Enter time period (years): "))

        if principal < 0 or rate < 0 or time < 0:
            print("Please enter positive values")
            return

        interest = calculate_simple_interest(principal, rate, time)
        total_amount = principal + interest

        print(f"Principal: ${principal:.2f}")
        print(f"Interest Rate: {rate}%")
        print(f"Time: {time} years")
        print(f"Simple Interest: ${interest:.2f}")
        print(f"Total Amount: ${total_amount:.2f}")

    except ValueError:
        print("Please enter valid numbers")

# Program 6: Area Calculator for Different Shapes
import math

def rectangle_area(length, width):
    return length * width

def circle_area(radius):
    return math.pi * radius ** 2

def triangle_area(base, height):
    return 0.5 * base * height

def area_calculator():
    print("\n=== Area Calculator ===")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")

    choice = input("Choose shape (1-3): ")

    try:
        if choice == '1':
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            if length > 0 and width > 0:
                area = rectangle_area(length, width)
                print(f"Area of rectangle: {area:.2f}")
            else:
                print("Please enter positive values")
        elif choice == '2':
            radius = float(input("Enter radius: "))
            if radius > 0:
                area = circle_area(radius)
                print(f"Area of circle: {area:.2f}")
            else:
                print("Please enter positive radius")
        elif choice == '3':
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            if base > 0 and height > 0:
                area = triangle_area(base, height)
                print(f"Area of triangle: {area:.2f}")
            else:
                print("Please enter positive values")
        else:
            print("Invalid choice")
    except ValueError:
        print("Please enter valid numbers")

# Program 7: Grade Calculator
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

def grade_calculator():
    print("\n=== Grade Calculator ===")

    try:
        subjects = int(input("Enter number of subjects: "))

        if subjects <= 0:
            print("Please enter a positive number of subjects")
            return

        total_marks = 0
        for i in range(subjects):
            marks = float(input(f"Enter marks for subject {i+1}: "))
            if marks < 0:
                print("Marks cannot be negative")
                return
            total_marks += marks

        max_marks = subjects * 100
        percentage = (total_marks / max_marks) * 100
        grade = calculate_grade(percentage)

        print(f"\nTotal Marks: {total_marks}/{max_marks}")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Grade: {grade}")

    except ValueError:
        print("Please enter valid numbers")

# Program 8: Password Generator
def generate_password(length):
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("\n=== Password Generator ===")

    try:
        length = int(input("Enter password length (minimum 4): "))

        if length < 4:
            print("Password length should be at least 4 characters")
            return

        password = generate_password(length)
        print(f"Generated password: {password}")
        print("Note: Save this password securely!")

    except ValueError:
        print("Please enter a valid number")

# Program 9: Rock Paper Scissors Game
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "user"
    else:
        return "computer"

def rock_paper_scissors():
    print("\n=== Rock Paper Scissors Game ===")
    print("Rules: rock beats scissors, scissors beats paper, paper beats rock")

    user_score = 0
    computer_score = 0
    rounds = 0

    while True:
        user_choice = input("\nEnter your choice (rock/paper/scissors) or 'quit' to exit: ").lower().strip()

        if user_choice == 'quit':
            break

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        rounds += 1

        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score after {rounds} rounds - You: {user_score}, Computer: {computer_score}")

        print("Final Score after {rounds} rounds:")
        print(f"You: {user_score}")
        print(f"Computer: {computer_score}")

    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif computer_score > user_score:
        print("Computer won! Better luck next time!")
    else:
        print("It's a tie game!")

# Program 10: Factorial Calculator
def factorial_iterative(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_calculator():
    print("\n=== Factorial Calculator ===")
    print("1. Iterative method")
    print("2. Recursive method")

    try:
        choice = input("Choose method (1 or 2): ")
        n = int(input("Enter a non-negative integer: "))

        if choice == '1':
            result = factorial_iterative(n)
        elif choice == '2':
            result = factorial_recursive(n)
        else:
            print("Invalid choice")
            return

        print(f"Factorial of {n} is: {result}")

    except ValueError:
        print("Please enter a valid integer")

# Program 11: Prime Number Checker
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_checker():
    print("\n=== Prime Number Checker ===")

    try:
        num = int(input("Enter a number to check: "))

        if is_prime(num):
            print(f"{num} is a prime number!")
        else:
            print(f"{num} is not a prime number.")

    except ValueError:
        print("Please enter a valid integer")

# Program 12: Fibonacci Series Generator
def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_series = [0, 1]
    for i in range(2, n):
        next_num = fib_series[i-1] + fib_series[i-2]
        fib_series.append(next_num)
    return fib_series

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci_recursive(n-1)
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)
        return fib_series

def fibonacci_generator():
    print("\n=== Fibonacci Series Generator ===")
    print("1. Iterative method")
    print("2. Recursive method")

    try:
        choice = input("Choose method (1 or 2): ")
        n = int(input("Enter number of terms: "))

        if n <= 0:
            print("Please enter a positive number")
            return

        if choice == '1':
            series = fibonacci_iterative(n)
        elif choice == '2':
            series = fibonacci_recursive(n)
        else:
            print("Invalid choice")
            return

        print(f"Fibonacci series ({n} terms): {series}")

    except ValueError:
        print("Please enter a valid integer")

# Main Menu
def main_menu():
    while True:
        print("\n" + "="*50)
        print("         BASIC PYTHON PROGRAMS MENU")
        print("="*50)
        print("1.  Simple Calculator")
        print("2.  Number Guessing Game")
        print("3.  Temperature Converter")
        print("4.  BMI Calculator")
        print("5.  Simple Interest Calculator")
        print("6.  Area Calculator")
        print("7.  Grade Calculator")
        print("8.  Password Generator")
        print("9.  Rock Paper Scissors Game")
        print("10. Factorial Calculator")
        print("11. Prime Number Checker")
        print("12. Fibonacci Series Generator")
        print("0.  Exit")
        print("="*50)

        choice = input("Enter your choice (0-12): ").strip()

        if choice == '1':
            calculator()
        elif choice == '2':
            number_guessing_game()
        elif choice == '3':
            temperature_converter()
        elif choice == '4':
            bmi_calculator()
        elif choice == '5':
            simple_interest_calculator()
        elif choice == '6':
            area_calculator()
        elif choice == '7':
            grade_calculator()
        elif choice == '8':
            password_generator()
        elif choice == '9':
            rock_paper_scissors()
        elif choice == '10':
            factorial_calculator()
        elif choice == '11':
            prime_checker()
        elif choice == '12':
            fibonacci_generator()
        elif choice == '0':
            print("Thank you for using Basic Python Programs!")
            break
        else:
            print("Invalid choice. Please try again.")

        input("\nPress Enter to continue...")

# Run the main menu if this file is executed directly
if __name__ == "__main__":
    main_menu()
