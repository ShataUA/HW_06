from normalise_name import normalize
import shutil
def file_manager(item, new_folder_path):
    normalised_file_name = f'{normalize(item.stem)}{item.suffix}'  # normalise file name string
    new_file_path = item.rename(item.parent / normalised_file_name)  # rename file
    try:
        new_folder_path.mkdir(parents=True, exist_ok=False)  # create directory for files will be replaced
        new_file_target = new_file_path.replace(new_folder_path / new_file_path.name)  # replace file
    except FileExistsError:
        new_file_target = new_file_path.replace(new_folder_path / new_file_path.name)  # replace file if target directory is exists
    return normalised_file_name

def archive_manager(item, new_folder_path):
    normalised_archive_name = f'{normalize(item.stem)}{item.suffix}'  # normalize archive name
    try:
        new_folder_path.mkdir(parents=True, exist_ok=False)  # create 'archives' directory if it not already exists
        old_archive_new_path = item.replace(new_folder_path / item.name)  # path to old archive replaced in new folder
        new_name_archive_path = old_archive_new_path.rename(new_folder_path / normalised_archive_name)  # rename archive in new folder
        new_archive_path = new_folder_path / new_name_archive_path.stem  # new name archive path without extension
        new_archive_path.mkdir(parents=True, exist_ok=False)  # create directory to unpack archive
        shutil.unpack_archive(new_name_archive_path, new_archive_path)  # unpack archive
    except FileExistsError:
        old_archive_new_path = item.replace(new_folder_path / item.name)  # path to old archive replaced in new folder
        new_name_archive_path = old_archive_new_path.rename(new_folder_path / normalised_archive_name) # rename archive in new folder
        new_archive_path = new_folder_path / new_name_archive_path.stem  # new name archive path without extension
        new_archive_path.mkdir(parents=True, exist_ok=False)  # create directory to unpack archive
        shutil.unpack_archive(new_name_archive_path, new_archive_path)  # unpack archive
    return normalised_archive_name
