def sum_even_numbers(numbers):
    even_sum = sum(num for num in numbers if num % 2 == 0)
    return even_sum

# Test the function with a sample list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_even_numbers(numbers)
print("Sum of even numbers in the list:", result)