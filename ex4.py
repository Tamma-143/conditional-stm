# Function to check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return f"{num} is Even"
    else:
        return f"{num} is Odd"

# Function to check if a number is positive, negative, or zero
def check_number_sign(num):
    if num > 0:
        return f"{num} is Positive"
    elif num < 0:
        return f"{num} is Negative"
    else:
        return f"{num} is Zero"

# Function to determine the largest of three numbers
def find_largest(a, b, c):
    if a > b and a > c:
        return f"{a} is the largest"
    elif b > a and b > c:
        return f"{b} is the largest"
    else:
        return f"{c} is the largest"

# Function to determine voting eligibility
def check_voting_eligibility(age):
    if age >= 18:
        return "You are eligible to vote!"
    else:
        return "You are not eligible to vote."

# Function to determine grade based on marks
def calculate_grade(marks):
    if marks >= 90:
        return "Grade: A"
    elif marks >= 80:
        return "Grade: B"
    elif marks >= 70:
        return "Grade: C"
    elif marks >= 60:
        return "Grade: D"
    else:
        return "Grade: F"

# Function to check if a number is within a range
def check_in_range(num, low, high):
    if low <= num <= high:
        return f"{num} is within the range {low} - {high}"
    else:
        return f"{num} is out of range"

# Function to check if a character is a vowel or consonant
def check_vowel_consonant(char):
    vowels = "aeiouAEIOU"
    if char in vowels:
        return f"{char} is a vowel"
    else:
        return f"{char} is a consonant"

# Function using match-case (Python 3.10+)
def check_day_of_week(day):
    match day.lower():
        case "monday":
            return "Start of the workweek!"
        case "friday":
            return "Weekend is coming!"
        case "saturday" | "sunday":
            return "It’s the weekend!"
        case _:
            return "A regular weekday!"

# Function to check leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"{year} is a Leap Year"
    else:
        return f"{year} is not a Leap Year"

# Function to check divisibility
def is_divisible(num, divisor):
    if num % divisor == 0:
        return f"{num} is divisible by {divisor}"
    else:
        return f"{num} is not divisible by {divisor}"

# Function to print even numbers in a range
def print_even_numbers(start, end):
    evens = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            evens.append(num)
    return evens

# Main Function
def main():
    print(check_even_odd(7))
    print(check_number_sign(-5))
    print(find_largest(10, 25, 5))
    print(check_voting_eligibility(17))
    print(calculate_grade(85))
    print(check_in_range(15, 10, 20))
    print(check_vowel_consonant('e'))
    print(check_day_of_week("Friday"))
    print(is_leap_year(2024))
    print(is_divisible(15, 3))
    print("Even numbers from 1 to 10:", print_even_numbers(1, 10))

# Call the main function
if __name__ == "__main__":
    main()
