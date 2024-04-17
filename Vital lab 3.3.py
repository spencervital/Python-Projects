def sort_and_remove_duplicates(input_list):
    """Sort and remove duplicates from an input list of integers."""
    # Check if the input list is empty
    if len(input_list) == 0:
        return "This list is empty."

    # Sort and remove duplicates from the input list
    sorted_list = sorted(input_list)
    unique_list = []
    for num in sorted_list:
        if num not in unique_list:
            unique_list.append(num)

    return unique_list


# Get the input list from the user
input_list = input("Enter a list of integers, separated by commas: ").split(",")

# Convert the input string to a list of integers
input_list = [int(num.strip()) for num in input_list]

# Sort and remove duplicates from the input list
unique_list = sort_and_remove_duplicates(input_list)

# Print the sorted and unique list
print("Sorted and unique list:", unique_list)
