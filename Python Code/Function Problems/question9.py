# def generate_numbers():
#     for i in range(3):
#         yield i  # Pauses and returns i

# gen = generate_numbers()  # Generator object
# print(next(gen))  # Output: 0
# print(next(gen))  # Output: 1
# print(next(gen))  # Output: 2

def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i

for num in even_generator(10):
    print(num)