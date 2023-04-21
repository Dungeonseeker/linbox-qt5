# linbox-qt5
A manager for 86Box written in Python using the PySide framework.

Aims to be simple and easy to use, might increase its scope in the future.

![Screenshot 1.](./resources/ss.png)

Currently only supports 86Box installed from a package manager, Flatpak/AppImage versions will not work.

## Usage
Do not use the included setup.py, stick to running directly from python.
```
git clone https://github.com/Dungeonseeker/linbox-qt5
cd linbox-qt5
$ python linbox.py
You need to install Pyside6, xdgenvpy & show-in-file-manager from pip
```

## Know issues
~~Using spaces or slashes in the name of a virtual machine will crash linbox.~~ Fixed

## ToDo
1. ~~Make name entry widget refuse spaces and slashes.~~
2. ~~Fix the weird labels that mirror the buttons with some icons.~~ Done
3. ~~Add a button to open the linbox storage folder.~~ <--- Done

## If I can goals
1. Settings manager. 
2. Interactive status bar.

# License
1. This software is provided as is under the MIT Open Source License. See [LICENSE.md](./LICENSE.md) for details.
2. This software uses Google material icons.
