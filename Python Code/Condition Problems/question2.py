# Get user input
no_adult = int(input("Give me the number of Adults: "))
no_kid = int(input("Give me the number of Kids: "))
day = input("What day is today? ").strip().lower()  # Normalize input

# Calculate cost based on the day
if day == "wednesday":
    ans = no_adult * 10 + no_kid * 6
else:
    ans = no_adult * 12 + no_kid * 8

# Print the result
print("Total cost:", ans)