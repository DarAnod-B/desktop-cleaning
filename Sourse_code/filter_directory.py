from setting.get_config import STORAGE_FOLDER, ALLOWED_EXTENSIONS, TRANSFER_FOLDERS, EXCLUDED_NAMES
from desktop_interaction import path_from_desktop
import os


def separating_files_and_folders(all_names):
    all_path = map(path_from_desktop, all_names)

    file_paths = []
    folder_paths = []

    for path in all_path:
        if os.path.isfile(path):
            file_paths.append(path)
        elif os.path.isdir(path):
            folder_paths.append(path)

    file_names = [os.path.basename(path) for path in file_paths]
    folder_names = [os.path.basename(path) for path in folder_paths]
    return [file_names, folder_names]


def filter_extension(file_name):
    extension = f'{file_name}'.rsplit('.', 1)[1]
    return extension not in ALLOWED_EXTENSIONS


def filter_object_names(object_names):
    object_name_without_extension = f'{object_names}'.rsplit('.', 1)[0]
    return object_name_without_extension not in EXCLUDED_NAMES


def filtering_folder_and_file_name(object_names):
    non_excluded_object_names = list(filter(filter_object_names, object_names))

    file_path, folder_path = separating_files_and_folders(
        non_excluded_object_names)
    filtered_file_path = list(filter(filter_extension, file_path))
    
    
    try:
        folder_path.remove(STORAGE_FOLDER)
    except ValueError:
        os.mkdir(path_from_desktop(STORAGE_FOLDER))

    if TRANSFER_FOLDERS == False:
        folder_path = []

    filtered_files_and_folders = filtered_file_path + folder_path
    return filtered_files_and_folders


if __name__ == "__main__":
    from setting.get_config import DESKTOP_PATH
    object_names = os.listdir(DESKTOP_PATH)
    print(filtering_folder_and_file_name(object_names))
    print(EXCLUDED_NAMES, ALLOWED_EXTENSIONS)
