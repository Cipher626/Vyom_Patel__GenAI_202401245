n = int(input("Calculate sum until? "))  # Get user input
sum = 0  # Initialize sum variable

print(type(sum))  # Print type of sum (for verification)

for i in range(0, n + 1):  # Iterate through numbers up to n
    if i % 2 == 0:  # Check if the number is even
        sum += i  # Add even number to sum

print(sum)  # Print the final sum