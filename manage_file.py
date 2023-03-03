from normalise_name import normalize
import shutil
def file_manager(item, new_folder_path):
    normalised_file_name = f'{normalize(item.stem)}{item.suffix}'
    new_file_path = item.rename(item.parent / normalised_file_name)
    try:
        new_folder_path.mkdir(parents=True, exist_ok=False)
        new_file_target = new_file_path.replace(new_folder_path / new_file_path.name)
    except FileExistsError:
        new_file_target = new_file_path.replace(new_folder_path / new_file_path.name)
    return normalised_file_name

def archive_manager(item, new_folder_path):
    normalised_archive_name = f'{normalize(item.stem)}{item.suffix}'
    try:
        new_folder_path.mkdir(parents=True, exist_ok=False)
        old_archive_new_path = item.replace(new_folder_path / item.name)
        new_name_archive_path = old_archive_new_path.rename(new_folder_path / normalised_archive_name)
        new_archive_path = new_folder_path / new_name_archive_path.stem
        new_archive_path.mkdir(parents=True, exist_ok=False)
        shutil.unpack_archive(new_name_archive_path, new_archive_path)
    except FileExistsError:
        old_archive_new_path = item.replace(new_folder_path / item.name)
        new_name_archive_path = old_archive_new_path.rename(new_folder_path / normalised_archive_name)
        new_archive_path = new_folder_path / new_name_archive_path.stem
        new_archive_path.mkdir(parents=True, exist_ok=False)
        shutil.unpack_archive(new_name_archive_path, new_archive_path)
    return normalised_archive_name
