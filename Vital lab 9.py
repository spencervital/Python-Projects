def modify_file(original_file, new_file):
    with open(original_file, 'r') as original, open(new_file, 'w') as new:
        line_number = 1
        for line in original:
            modified_line = f"{line_number}. {line.strip()} Sample\n"
            new.write(modified_line)
            line_number += 1

original_file = "/Users/spencerpenpenvital/PycharmProjects/IT280/output.txt"  # Replace with the path to your original file
new_file = "modified.txt"  # Replace with the desired path for the new file

modify_file(original_file, new_file)
print(f"New file '{new_file}' has been created with the modifications.")
