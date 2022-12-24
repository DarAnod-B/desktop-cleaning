import os
from filter_directory import filtering_folder_and_file_names
from work_in_directory import moving_files_and_folders
from config import DESKTOP_PATH


def main():
    object_names = os.listdir(DESKTOP_PATH)
    all_name = filtering_folder_and_file_names(object_names)
    moving_files_and_folders(all_name)


if __name__ == "__main__":
    main()
