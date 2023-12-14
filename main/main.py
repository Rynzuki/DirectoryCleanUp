import os
import pathlib
import shutil

sorting_path = input("Input directory path to clean up: ")
print()

file_types = []

def main():
    for file in os.scandir(sorting_path):
        if file.is_file():
            type = pathlib.Path(file).suffix.replace(".","")

            print(type)
            if not type in os.listdir(sorting_path):
                os.mkdir(sorting_path + "/" + type)

            shutil.move(file.path, sorting_path + "/" + type)

if (__name__ == "__main__"):
    main()