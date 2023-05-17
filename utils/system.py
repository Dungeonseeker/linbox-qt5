import os
import glob


def find_portable_path():
    search_paths = [os.path.expanduser(os.path.join('~', 'Portable'))]
    for search_path in search_paths:
        for inner_path in glob.glob(os.path.join(search_path, '*', '86Box*.AppImage')):
            return inner_path
