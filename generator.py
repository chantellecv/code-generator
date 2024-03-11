def sum_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

# Test the function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = sum_even_numbers(numbers)
print("Sum of even numbers:", result)