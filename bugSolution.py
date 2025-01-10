def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

#Example usage with error handling
my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}")  # Output: The average is: 0

my_list = [1,2,3,4,5]
result = calculate_average(my_list)
print(f"The average is: {result}") # Output: The average is: 3.0