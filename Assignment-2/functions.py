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

# func10: Calculate the Length of a String
#Author: Ashish Lal 21bcs017
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

