# Importing the array module
import array as arr

# Creating an array of integers
numbers = arr.array('i', [10, 20, 30, 40, 50])

# Adding an element to the array
numbers.append(60)

# Removing an element from the array
numbers.remove(30)

# Accessing and modifying an element
numbers[2] = 35

# Performing a simple operation on the array elements (e.g., incrementing all by 5)
for i in range(len(numbers)):
    numbers[i] += 5
