import sys
import argparse
import ast
import random


# Author : Nancy Yadav 21bcs071
def calculate_factorial(n):
    """Calculate the factorial of a number."""
    if n < 0:
        return "Factorial not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


# Author : Chaytali Jawalekar 21bcs026
def fibonacci(n):
    """Generate a Fibonacci sequence up to n terms."""
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence


# Author : Ashish Higgins 21bcs014
def find_max(lst):
    if not lst:
        return None
    return max(lst)


#Author: Ashish Lal 21bcs017
def string_length(s):
    """Calculate the length of a string."""
    return len(s)


#Author: Adi jain 21bcs003
def sort_list(lst):
    """Sort a list in ascending order."""
    return sorted(lst)


#Author: Enduri Jahnavi 21bds019
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Author : Sadikh Shaik 21BDS059
def generate_random_number(start=1, end=100):
    """Generate a random number between start and end."""
    return random.randint(start,end)


# Author : C Sai Rithwik Reddy, 21BCS028
def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return (c * 9/5) + 32


# Author : Palash Bhasme, 21BCS076
def count_vowels(s):
    """Count the number of vowels in a string."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)


#Author : Yash Kumar 21bec059
def main():
    parser = argparse.ArgumentParser(description="Run various utility functions.")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # func1: Calculate Factorial
    parser_factorial = subparsers.add_parser('factorial', help='Calculate factorial of a number')
    parser_factorial.add_argument('number', type=int, nargs='?', default=5, help='Integer to calculate factorial')

    # func2: Reverse a String
    parser_reverse = subparsers.add_parser('reverse', help='Reverse a string')
    parser_reverse.add_argument('string', type=str, nargs='?', default="Hello World", help='String to reverse')

    # func3: Check Prime Number
    parser_prime = subparsers.add_parser('is_prime', help='Check if a number is prime')
    parser_prime.add_argument('number', type=int, nargs='?', default=17, help='Integer to check for primality')

    # func4: Generate Fibonacci Sequence
    parser_fibonacci = subparsers.add_parser('fibonacci', help='Generate Fibonacci sequence')
    parser_fibonacci.add_argument('terms', type=int, nargs='?', default=10, help='Number of terms in Fibonacci sequence')

    # func5: Convert Celsius to Fahrenheit
    parser_celsius = subparsers.add_parser('celsius_to_fahrenheit', help='Convert Celsius to Fahrenheit')
    parser_celsius.add_argument('celsius', type=float, nargs='?', default=25.0, help='Temperature in Celsius')

    # func6: Find Maximum in a List
    parser_max = subparsers.add_parser('find_max', help='Find maximum number in a list')
    parser_max.add_argument('list', type=str, nargs='?', default="[3, 1, 4, 1, 5, 9, 2]", help='List of numbers (e.g., "[1, 2, 3]")')

    # func7: Count Vowels in a String
    parser_vowels = subparsers.add_parser('count_vowels', help='Count vowels in a string')
    parser_vowels.add_argument('string', type=str, nargs='?', default="ChatGPT is awesome!", help='String to count vowels in')

    # func8: Sort a List
    parser_sort = subparsers.add_parser('sort_list', help='Sort a list in ascending order')
    parser_sort.add_argument('list', type=str, nargs='?', default="[5, 2, 9, 1, 5, 6]", help='List of numbers to sort (e.g., "[3, 1, 4]")')

    # func9: Generate a Random Number
    parser_random = subparsers.add_parser('generate_random', help='Generate a random number between start and end')
    parser_random.add_argument('start', type=int, nargs='?', default=1, help='Start of range')
    parser_random.add_argument('end', type=int, nargs='?', default=100, help='End of range')

    # func10: Calculate the Length of a String
    parser_length = subparsers.add_parser('string_length', help='Calculate the length of a string')
    parser_length.add_argument('string', type=str, nargs='?', default="Hello, World!", help='String to calculate length')

    args = parser.parse_args()

    if args.command == 'factorial':
        result = calculate_factorial(args.number)
        print(f"Factorial of {args.number} is {result}")

    elif args.command == 'reverse':
        result = reverse_string(args.string)
        print(f"Reversed string: {result}")

    elif args.command == 'is_prime':
        result = is_prime(args.number)
        print(f"{args.number} is {'a prime' if result else 'not a prime'} number.")

    elif args.command == 'fibonacci':
        result = fibonacci(args.terms)
        print(f"Fibonacci sequence up to {args.terms} terms: {result}")

    elif args.command == 'celsius_to_fahrenheit':
        result = celsius_to_fahrenheit(args.celsius)
        print(f"{args.celsius}°C is {result}°F")

    elif args.command == 'find_max':
        try:
            input_list = ast.literal_eval(args.list)
            if not isinstance(input_list, list):
                raise ValueError
            result = find_max(input_list)
            print(f"The maximum number in {input_list} is {result}")
        except (ValueError, SyntaxError):
            print("Please provide a valid list, e.g., \"[1, 2, 3]\"")

    elif args.command == 'count_vowels':
        result = count_vowels(args.string)
        print(f"The number of vowels in \"{args.string}\" is {result}")

    elif args.command == 'sort_list':
        try:
            input_list = ast.literal_eval(args.list)
            if not isinstance(input_list, list):
                raise ValueError
            result = sort_list(input_list)
            print(f"Sorted list: {result}")
        except (ValueError, SyntaxError):
            print("Please provide a valid list, e.g., \"[3, 1, 4]\"")

    elif args.command == 'generate_random':
        result = generate_random_number(args.start, args.end)
        print(f"Random number between {args.start} and {args.end}: {result}")

    elif args.command == 'string_length':
        result = string_length(args.string)
        print(f"The length of \"{args.string}\" is {result} characters.")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()