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
    parser_sort = subparsers.add_parser('sort_list', help='Sort a list in ascending order')
    parser_sort.add_argument('list', type=str, nargs='?', default="[5, 2, 9, 1, 5, 6]", help='List of numbers to sort (e.g., "[3, 1, 4]")')
