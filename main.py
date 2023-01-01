import os
import sys
from autorun import autorun_activation
from filter_directory import filtering_folder_and_file_name
from directory_interaction import moving_files_and_folders
from interface import launch_interface
from setting.get_config import DESKTOP_PATH


def main():
    autorun_activation()
    if '--no_interface' in sys.argv[1:]:
        object_names = os.listdir(DESKTOP_PATH)
        all_name = filtering_folder_and_file_name(object_names)
        moving_files_and_folders(all_name)
    else:
        launch_interface()


if __name__ == "__main__":
    main()
