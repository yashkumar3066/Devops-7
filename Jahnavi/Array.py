# Importing the array module
import array as arr

# Creating an array of integers
numbers = arr.array('i', [100, 200, 300, 400, 500])

# Adding an element to the array
numbers.append(600)

# Removing an element from the array
numbers.remove(300)

# Accessing and modifying an element
numbers[2] = 35

# Performing a simple operation on the array elements (e.g., incrementing all by 5)
for i in range(len(numbers)):
    numbers[i] += 5
