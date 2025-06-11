n = int(input("Print table for which number? "))  # Get user input

for i in range(1, 11):  # Iterate through numbers 0 to 10
    if i == 5:  # Skip printing the 5th iteration
        continue
    else:
        print(f"{i} x {n} = {i * n}")  # Corrected print statement with f-string formatting