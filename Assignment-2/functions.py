def toggle_switches(operations):
    # Find the maximum index we need to handle from the operations
    max_index = max(max(op) for op in operations)
    
    # Initialize a difference array of size (max_index + 2)
    switches = [0] * (max_index + 2)
    
    # Process each operation
    for left, right in operations:
        switches[left] += 1
        switches[right + 1] -= 1
    
    # Apply the difference array to get the final states of switches
    on_indices_sum = 0
    current_state = 0
    for i in range(1, max_index + 1):
        current_state += switches[i]
        if current_state % 2 == 1:
            on_indices_sum += i
    
    return on_indices_sum

# Example usage
operations = [[4, 5], [1, 4], [2, 6],[1,5]]
result = toggle_switches(operations)
print(result)  # Output the sum of indices where switches are on