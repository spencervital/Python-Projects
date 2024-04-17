import re


def search_numbers(filename):
    # Regex patterns for phone numbers, SSNs, and zip codes
    phone_pattern = r'\d{3}-\d{3}-\d{4}'
    ssn_pattern = r'\d{3}-\d{2}-\d{4}'
    zip_pattern = r'\d{5}'

    # Open the file for reading
    with open(filename, 'r') as file:
        content = file.read()

    # Search for phone numbers, SSNs, and zip codes using regex
    phone_numbers = re.findall(phone_pattern, content)
    ssn_numbers = re.findall(ssn_pattern, content)
    zip_codes = re.findall(zip_pattern, content)

    # Return the results
    return phone_numbers, ssn_numbers, zip_codes


# Specify the filename
filename = '/Users/spencerpenpenvital/PycharmProjects/IT280/numbers sample 2.txt'  # Replace with your file name

# Search for numbers in the file
phone_numbers, ssn_numbers, zip_codes = search_numbers(filename)

# Find the maximum length of each list
max_length = max(len(phone_numbers), len(ssn_numbers), len(zip_codes))

# Print the results in three columns
print("Phone Numbers\t\tSocial Security Numbers\tZip Codes")
print("---------------------------------------------------------------")

for i in range(max_length):
    phone = phone_numbers[i] if i < len(phone_numbers) else ""
    ssn = ssn_numbers[i] if i < len(ssn_numbers) else ""
    zip_code = zip_codes[i] if i < len(zip_codes) else ""

    print(f"{phone}\t\t\t{ssn}\t\t\t{zip_code}")
