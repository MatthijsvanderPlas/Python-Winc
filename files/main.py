__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from zipfile import ZipFile

folder = os.path.join(os.getcwd(), "cache")  # Path for our directory
zip_file = os.path.join(os.path.abspath("data.zip"))


def clean_cache():
    if os.path.exists(folder):  # If the folder exits we remove all its files
        for file in os.listdir(folder):
            path_to_file = os.path.join(folder, file)
            os.remove(path_to_file)
    else:  # Otherwise we create a new folder
        os.mkdir(folder)


def cache_zip(zip_file, cache_path):
    with ZipFile(zip_file) as zObject:
        zObject.extractall(cache_path)


def cached_files():
    file_list = []
    for file in os.listdir(folder):
        file_list.append(os.path.join(folder, file))
    return file_list


def find_password(files_list):
    for file in files_list:
        with open(file, "r") as f:
            for line in f.readlines():
                if "password" in line:
                    return line.replace("\n", "").replace("password: ", "")


if __name__ == "__main__":
    clean_cache()
    cache_zip(zip_file, folder)
    password = find_password(cached_files())
    print(password)
