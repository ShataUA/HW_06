from pathlib import Path
import sys
# import shutil
# from normalise_name import normalize
from manage_file import file_manager
from manage_file import archive_manager

# folder = r'D:\GoIT\D:\GoIT\New_F'
# folder_path = Path(folder)

images_list = []
documents_list = []
audio_list = []
video_list = []
archives_list = []
unknown_extension_files_list = []
known_extensions_list = []
unknown_extensions_list = []

extensions_dict = {
    'images': ['.jpeg', '.jpg', '.png', '.bmp', '.svg'],
    'documents': ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.xls', '.pptx'],
    'audio': ['.mp3', '.ogg', '.wav', '.amr'],
    'video': ['.mp4', '.avi', '.mov', '.mpg', '.mpeg', '.wmv', '.mkv'],
    'archives': ['.zip', '.gz', '.tar']
}


# def sanitize(folder_path):
#     for item in folder_path.iterdir():
#         if item.is_dir():
#             if item.name in ['images', 'documents', 'audio', 'video', 'archives']:
#                 continue
#             if not any(item.iterdir()):
#                 item.rmdir()
#             sanitize(item)


def sort(folder):
    path = Path(folder)
    for item in path.iterdir():
        if item.is_dir():
            if item.name in ['images', 'documents', 'audio', 'video', 'archives']:
                continue
            sort(item)
        elif item.suffix in extensions_dict['images']:
            new_folder_path = folder_path / 'images'
            normalised_file_name = file_manager(item,
                                                new_folder_path)  # normalised and replaced file with new file name return
            global images_list
            images_list.append(normalised_file_name)
        elif item.suffix in extensions_dict['documents']:
            new_folder_path = folder_path / 'documents'
            normalised_file_name = file_manager(item,
                                                new_folder_path)  # normalised and replaced file with new file name return
            global documents_list
            documents_list.append(normalised_file_name)
        elif item.suffix in extensions_dict['audio']:
            new_folder_path = folder_path / 'audio'
            normalised_file_name = file_manager(item,
                                                new_folder_path)  # normalised and replaced file with new file name return
            global audio_list
            audio_list.append(normalised_file_name)
        elif item.suffix in extensions_dict['video']:
            new_folder_path = folder_path / 'video'
            normalised_file_name = file_manager(item,
                                                new_folder_path)  # normalised and replaced file with new file name return
            global video_list
            video_list.append(normalised_file_name)
        elif item.suffix in extensions_dict['archives']:
            new_folder_path = folder_path / 'archives'
            normalised_archive_name = archive_manager(item,
                                                      new_folder_path)  # normalised and replaced file with new file name return
            global archives_list
            archives_list.append(normalised_archive_name)
        else:
            new_folder_path = folder_path / 'unknown_extension_files'
            try:
                new_folder_path.mkdir(parents=True, exist_ok=False)
                new_file_target = item.replace(new_folder_path / item.name)
            except FileExistsError:
                new_file_target = item.replace(new_folder_path / item.name)
            global unknown_extension_files_list
            unknown_extension_files_list.append(item.name)


# def sanitize_folder(folder):
#     path = Path(folder)
#     for item in path.iterdir():
#         if item.is_dir():
#             if item.name in ['images', 'documents', 'audio', 'video', 'archives']:
#                 continue
#             if not any(item.iterdir()):
#                 item.rmdir()
#             sanitize_folder(item)
# sanitize_folder(folder_path)




if __name__ == '__main__':
    folder = sys.argv[1]
    folder_path = Path(folder)
    sort(folder)
    print(f'images: {images_list}')
    print(f'documents: {documents_list}')
    print(f'audio: {audio_list}')
    print(f'video: {video_list}')
    print(f'archives: {archives_list}')
    print(f'unknown_extension_files: {unknown_extension_files_list}')
