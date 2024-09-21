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
