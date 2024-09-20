

#@yashkumar3066
def sum_of_two_numbers(a, b):
    """
    Function to return the sum of two numbers.

    Parameters:
    a (int/float): First number.
    b (int/float): Second number.

    Returns:
    int/float: Sum of a and b.
    """
    return a + b

# changes made by ashishH

def addTwoNum(a, b):
    return a+b


# Changes by Adi

print ('Hello Adi')
=======
#changes by ashishlal
def to_print(text):
    print(text)

print('hello, hi bye')


def quick_sort(arr):
    # Base case: if the array is empty or has one element, it's already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Choose a pivot element (typically the middle element)
        pivot = arr[len(arr) // 2]
        
        # Partition the array into elements less than, equal to, and greater than the pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        # Recursively sort the left and right partitions and combine them with the middle
        return quick_sort(left) + middle + quick_sort(right)

# Example usage
arr = [12, 4, 5, 6, 7, 3, 1, 15]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
