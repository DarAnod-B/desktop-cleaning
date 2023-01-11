import os
import sys
from autorun import autorun_activation
from filter_directory import filtering_folder_and_file_name
from desktop_interaction import moving_files_and_folders, setWallpaper
from interface import launch_interface
from setting.get_config import DESKTOP_PATH


def main():
    autorun_activation()

    if not '--no_interface' in sys.argv[1:]:
        object_names = os.listdir(DESKTOP_PATH)
        filtered_files_and_folders = filtering_folder_and_file_name(
            object_names)
        moving_files_and_folders(filtered_files_and_folders)
        setWallpaper()
    else:
        launch_interface()


if __name__ == "__main__":
    main()
