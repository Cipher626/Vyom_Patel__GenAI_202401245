color_of_fruit = input("What is the color of fruit?").strip().lower()

memory = {'green':'Unripe', 'yellow':'ripe', 'brown':'Overripe'}

if (color_of_fruit in memory):
    print(memory[color_of_fruit])
else:
    print("Give valid input")