from pathlib import Path
import sys
from normalise_name import normalize



folder = r'D:\GoIT\New_F\Barber'
def sort(folder):
    images_list = []
    documents_list = []
    audio_list = []
    video_list = []
    archives_list = []
    folder_path = Path(folder)
    for item in folder_path.iterdir():
        if item.is_dir():
            sort(item)
        else:
            if item.suffix == '.jpeg' or item.suffix == '.jpg' or item.suffix == '.png' or item.suffix == '.svg':
                # dot_index = item.name.rfind('.')
                # file_name = item.name[0:dot_index]
                normalised_file_name = f'{normalize(item.stem)}{item.suffix}'
                renamed_item = item.rename(Path(item.parent, normalised_file_name))
                images_list.append(normalised_file_name)
                try:
                    images_folder = Path(folder + r'\images')
                    images_folder.mkdir(parents=True, exist_ok=False)
                    new_place = renamed_item.replace(images_folder)
                except FileExistsError:
                    new_place = renamed_item.replace(images_folder)

    return normalised_file_name


print(sort(folder))



# if __name__ == '__main__':
#     folder = sys.argv[1]
#     sort(folder)


