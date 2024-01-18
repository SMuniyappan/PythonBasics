"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""
import os

def read_files_and_write_result(directory_path="./files", output_file="result.txt"):

    file_list = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    values = []

    for file_name in file_list:
        file_path = os.path.join(directory_path, file_name)
        with open(file_path, "r") as file:
            try:
                value = int(file.read().strip())
                values.append(str(value))
            except ValueError:
                print(f"Ignoring non-numeric content in {file_name}")

    result_path = os.path.join(directory_path, output_file)
    with open(result_path, "w") as result_file:
        result_file.write(", ".join(values))

# Call the function
read_files_and_write_result()