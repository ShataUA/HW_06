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


# images_list = []
# documents_list = []
# audio_list = []
# video_list = []
# archives_list = []
# unknown_extension_files_list = []
# known_extensions_list = []
# unknown_extensions_list = []


extensions_dict = {
    'images': ['.jpeg', '.jpg', '.png', '.bmp', '.svg'],
    'documents': ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.xls', '.pptx'],
    'audio': ['.mp3', '.ogg', '.wav', '.amr'],
    'video': ['.mp4', '.avi', '.mov', '.mpg', '.mpeg', '.wmv', '.mkv'],
    'archives': ['.zip', '.gz', '.tar'],
    'unknown': []
}

result_dict = {}

ignore_folders_list = [i for i in extensions_dict.keys()]


# def extensions_append(extension):  # update known extensions list
#     global known_extensions_list
#     if extension not in known_extensions_list:
#         known_extensions_list.append(extension)


def add_to_result(path:Path, category=None):
    if category:
        if result_dict.get(category):
            result_dict[category].add(path.name,)
        else:
            result_dict[category] = {path.name}
    else:
        if result_dict.get('unknown_file_list'):
            result_dict['unknown_file_list'].add(path.name,)
        else:
            result_dict['unknown_file_list'] = {path.name}


def get_category(path: Path):
    for cat, exts in extensions_dict.items():
        if path.suffix.lower() in exts:
            add_to_result(path, cat)
            return cat
    add_to_result(path)
    return 'unknown'


def move_file(file:Path, root_dir:Path, category: str):
    target_dir = root_dir / category
    if not target_dir.exists():
        target_dir.mkdir()
    print(file.replace(target_dir / file.name))


def sort_files(path:Path, root_path:Path):
    for item in path.glob('*.*'):
        category = get_category(item)
        move_file(item, root_path, category)
        

def sort(folder):
    path = Path(folder)
    for item in [p for p in path.glob("**") if  p.name not in ignore_folders_list][::-1]:
        
        sort_files(item, path)
    
        try:
            item.rmdir()
        except Exception as e:
            print(f"{item} not empty {e}")


if __name__ == '__main__':
    folder = sys.argv[1]
    folder_path = Path(folder)
    
    sort(folder)
    
    for category, items in result_dict.items():
        print(f"{category} - {items}")
