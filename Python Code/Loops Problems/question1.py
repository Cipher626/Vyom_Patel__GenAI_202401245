sample = [1, 2, 3, 4, 5, 6, -7, -8, -9, -10, -11]
count = 0

for num in sample:
    if num > 0:
        count += 1
        print(type(num))

print(count)