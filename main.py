import os
from filter_directory import path_to_filtering_folder_and_file
from directory_interaction import moving_files_and_folders
from setting.get_config import DESKTOP_PATH

   
def main():
    object_names = os.listdir(DESKTOP_PATH)
    all_name = path_to_filtering_folder_and_file(object_names)
    moving_files_and_folders(all_name)


if __name__ == "__main__":
    main()
