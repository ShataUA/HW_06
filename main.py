from pathlib import Path
import sys
from manage_file import file_manager
from manage_file import archive_manager
from sanitize import sanitize_folder


"""
    To run the script open terminal and type command: py main.py 'target folder path' 
    Python interpreter needed
    Check U have the following files in the project directory: main.py, manage_file.py, normalise_name.py, sanitize.py
    For more information: 
                        antonshamaida@gmail.com
                        Slack: @Anton.Shamaida
"""


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


def extensions_append(extension):  # update known extensions list
    global known_extensions_list
    if extension not in known_extensions_list:
        known_extensions_list.append(extension)


def sort(folder):
    path = Path(folder)
    for item in path.iterdir():
        if item.is_dir():
            if item.name in ['images', 'documents', 'audio', 'video', 'archives', 'unknown_extension_files']:  # ignore folders
                continue
            sort(item)
        elif item.suffix in extensions_dict['images']:  # file extension checking
            new_folder_path = folder_path / 'images'  # images folder path
            normalised_file_name = file_manager(item,
                                                new_folder_path)  # normalised and replaced file with new file name return
            global images_list
            images_list.append(normalised_file_name)  # update list of images
            extensions_append(item.suffix)  # update list of known extensions
        elif item.suffix in extensions_dict['documents']:  # file extension checking
            new_folder_path = folder_path / 'documents'  # documents folder path
            normalised_file_name = file_manager(item,
                                                new_folder_path)  # normalised and replaced file with new file name return
            global documents_list
            documents_list.append(normalised_file_name)  # update list of documents
            extensions_append(item.suffix)  # update list of known extensions
        elif item.suffix in extensions_dict['audio']:  # file extension checking
            new_folder_path = folder_path / 'audio'  # audio folder path
            normalised_file_name = file_manager(item,
                                                new_folder_path)  # normalised and replaced file with new file name return
            global audio_list
            audio_list.append(normalised_file_name)  # update list of audio files
            extensions_append(item.suffix)  # update list of known extensions
        elif item.suffix in extensions_dict['video']:  # file extension checking
            new_folder_path = folder_path / 'video'  # video folder path
            normalised_file_name = file_manager(item,
                                                new_folder_path)  # normalised and replaced file with new file name return
            global video_list
            video_list.append(normalised_file_name)  # update list of video files
            extensions_append(item.suffix)  # update list of known extensions
        elif item.suffix in extensions_dict['archives']:  # file extension checking
            new_folder_path = folder_path / 'archives'  # archives folder path
            normalised_archive_name = archive_manager(item,
                                                      new_folder_path)  # normalised and replaced file with new file name return
            global archives_list
            archives_list.append(normalised_archive_name)  # update archives list
            extensions_append(item.suffix)  # update list of known extensions
        else:
            new_folder_path = folder_path / 'unknown_extension_files'  # unknown extension files folder path
            try:
                new_folder_path.mkdir(parents=True, exist_ok=False)  # create unknown extension files folder
                item.replace(new_folder_path / item.name)  # replace unknown extension files
            except FileExistsError:
                item.replace(new_folder_path / item.name)  # replace unknown extension files
            global unknown_extension_files_list
            unknown_extension_files_list.append(item.name)  # update unknown extension files list
            global unknown_extensions_list
            unknown_extensions_list.append(item.suffix)  # update unknown extensions list


if __name__ == '__main__':
    folder = sys.argv[1]
    folder_path = Path(folder)
    sort(folder)
    sanitize_folder(folder_path)
    print(f'images:\n{images_list}\n')
    print(f'documents:\n{documents_list}\n')
    print(f'audio:\n{audio_list}\n')
    print(f'video:\n{video_list}\n')
    print(f'archives:\n{archives_list}\n')
    print(f'unknown_extension_files:\n{unknown_extension_files_list}\n')
    print(f'known_extensions:\n{known_extensions_list}\n')
    print(f'unknown_extensions:\n{unknown_extensions_list}\n')
