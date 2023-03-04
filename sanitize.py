import shutil


def sanitize_folder(path):
    for item in path.iterdir():  # iteration on target path
        if item.is_dir():
            if item.name not in ['images', 'documents', 'audio', 'video', 'archives', 'unknown_extension_files']:  # ignore folders
                shutil.rmtree(item, ignore_errors=True)  # remove directory with all tree
                continue
        continue
