from pathlib import Path

folder = r'D:\GoIT\New_F'
path = Path(folder)


def sanitize_folder(path):
    for item in path.iterdir():
        if item.is_dir():
            if item.name in ['images', 'documents', 'audio', 'video', 'archives']:
                continue
            if not any(item.iterdir()):
                item.rmdir()
            sanitize_folder(item)


print(sanitize_folder(path))
