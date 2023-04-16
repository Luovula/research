import json
import os

def read_file(file_path):
    with open(file_path) as user_file:
        content = user_file.read()
    return content

def convert_to_json(content):
    # Replace this line with the logic to convert the content into a Python object
    python_object = content.splitlines()
    json_data = json.dumps(python_object)
    return json_data

def write_json_file(json_data, output_file):
    with open(output_file, 'w') as file:
        file.write(json_data)

def main():
    file_count = 40

    for i in range(2, file_count + 1):
        input_file = f'game_{i}'
        output_file = f'game_{i}.json'

        content = read_file(input_file)
        json_data = convert_to_json(content)
        write_json_file(json_data, output_file)
        print(f"Converted '{input_file}' to '{output_file}'")

if __name__ == '__main__':
    main()
