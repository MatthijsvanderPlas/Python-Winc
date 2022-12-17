__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from zipfile import ZipFile


def clean_cache():

    folder = os.path.abspath("./files/cache")  # Path for our directory
    if os.path.exists(folder):  # If the folder exits we remove all its files
        for file in os.listdir(folder):
            path_to_file = os.path.join(folder, file)
            os.remove(path_to_file)
    else:  # Otherwise we create a new folder
        os.mkdir(folder)


def cache_zip(zip_file, cache_path):
    clean_cache()
    folder = cache_path
    with ZipFile(zip_file) as zObject:
        zObject.extractall(folder)


def cached_files():
    folder = os.path.abspath("./files/cache")
    file_list = []
    for file in os.listdir(folder):
        file_list.append(folder + "/" + file)
    return file_list


def find_password(files_list):
    for file in files_list:
        with open(file) as f:
            for line in f.readlines():
                if "password" in line:
                    return line.replace("\n", "").replace("password: ", "")
