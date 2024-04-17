import re


def search_patterns(file_path):
    # Open the file and read its contents
    with open(file_path, 'r') as file:
        content = file.read()

    # Define regular expressions for phone numbers, social security numbers, and zip codes
    phone_pattern = r'\b(?:\+?\d{1,3}[-.●]?)?\(?\d{3}\)?[-.●]?\d{3}[-.●]?\d{4}\b'
    ssn_pattern = r'\b\d{3}-\d{2}-\d{4}\b'
    zip_pattern = r'\b\d{5}(?:-\d{4})?\b'

    # Search for patterns in the content
    phone_numbers = re.findall(phone_pattern, content)
    social_security_numbers = re.findall(ssn_pattern, content)
    zip_codes = re.findall(zip_pattern, content)

    # Print the results
    print("Phone Numbers:")
    print(phone_numbers)
    print("\nSocial Security Numbers:")
    print(social_security_numbers)
    print("\nZip Codes:")
    print(zip_codes)


# Example usage
file_path = "/Users/spencerpenpenvital/PycharmProjects/IT280/numbers sample 1.txt"  # Replace with the path to your file
search_patterns(file_path)
