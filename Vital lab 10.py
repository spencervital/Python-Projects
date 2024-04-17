import zipfile
import os

# Paths to the files created in Lab 8 and Lab 9
file1_path = "/Users/spencerpenpenvital/PycharmProjects/IT280/output.txt"  # Replace by your file path
file2_path = "/Users/spencerpenpenvital/PycharmProjects/IT280/modified.txt"  # Replace by your file path

# Create a new ZIP archive
zip_filename = "archive.zip"
zip_path = os.path.join("Zip", zip_filename)

# Create the 'Zip' directory if it doesn't exist
if not os.path.exists("Zip"):
    os.makedirs("Zip")

# Compress file1
with zipfile.ZipFile(zip_path, "w") as archive:
    archive.write(file1_path, os.path.basename(file1_path))

# Compress file2 and add it to the existing archive
with zipfile.ZipFile(zip_path, "a") as archive:
    archive.write(file2_path, os.path.basename(file2_path))

print(f"The ZIP file '{zip_filename}' has been created in the 'Zip' directory.")
