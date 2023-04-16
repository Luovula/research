import os

def get_file_extension(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension

def main():
    input_file = 'C:\Users\Elphie\Desktop\Luna\research\game_2'

    file_extension = get_file_extension(input_file)
    print(f"The file type of '{input_file}' is '{file_extension}'")

if __name__ == '__main__':
    main()
