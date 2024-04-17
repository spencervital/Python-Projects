import random


def generate_file(file_path, num_rows):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Change this if you want a different character set
    with open(file_path, 'w') as file:
        for _ in range(num_rows):
            char1 = random.choice(characters)
            integer = random.randint(0, 999)
            char2 = random.choice(characters)
            float_num = round(random.uniform(0, 10000), 2)

            line = f"{char1 * 5} {integer:4d} {char2 * 3} {float_num:8.2f}\n"
            file.write(line)


# Usage example
file_path = "output.txt"  # Change this to your desired file path
num_rows = 20  # Change this to the number of rows you want in the file

generate_file(file_path, num_rows)
print(f"File '{file_path}' has been generated.")
