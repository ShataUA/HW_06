import shutil


def sanitize_folder(path, ignore_folders_list):
    for item in path.iterdir():  # iteration on target path
        if item.is_dir():
            if item.name not in ignore_folders_list:  # ignore folders
                shutil.rmtree(item, ignore_errors=True)  # remove directory with all tree
                continue
        continue
