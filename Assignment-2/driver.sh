#!/bin/bash

# Author : Yash Kumar 21bec059

# Ensure the Python script exists
if [ ! -f functions.py ]; then
    echo "Error: functions.py not found!"
    exit 1
fi

# Function to execute a command and check for errors
execute() {
    echo "Running: $1"
    eval $1
    if [ $? -ne 0 ]; then
        echo "Error executing: $1"
        exit 1
    fi
    echo
}

# func: Calculate Factorial
execute "python3 functions.py factorial 5"

# func: Check Prime Number
execute "python3 functions.py is_prime 17"

# func: Generate Fibonacci Sequence
execute "python3 functions.py fibonacci 10"

# func: Convert Celsius to Fahrenheit
execute "python3 functions.py celsius_to_fahrenheit 25"

# func: Find Maximum in a List
execute "python3 functions.py find_max '[3, 1, 4, 1, 5, 9, 2]'"

# func: Count Vowels in a String
execute "python3 functions.py count_vowels 'ChatGPT is awesome!'"

# func: Sort a List
execute "python3 functions.py sort_list '[5, 2, 9, 1, 5, 6]'"

# func: Generate a Random Number
execute "python3 functions.py generate_random 1 100"

# func: Calculate the Length of a String
execute "python3 functions.py string_length 'Hello, World!'"

echo "All functions have been executed successfully."
