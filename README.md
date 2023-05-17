# linbox-qt5

A manager for 86Box written in Python using the PySide framework.

Aims to be simple and easy to use, might increase its scope in the future.

![Screenshot 1.](./resources/ss.png)

Supports 86Box installed from a package manager or Flatpak. AppImage versions will work if under ~/Portable.

## Usage

**Do not use the included setup.py, stick to running directly from python.**

```
git clone https://github.com/Dungeonseeker/linbox-qt5
cd linbox-qt5
$ pip install -r requirements.txt
$ python linbox.py
```

## Ubuntu

sudo apt-get install '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev

## Know issues, ToDos & Misc

See [CHANGELOG](./CHANGELOG) for details

# License

1. This software is provided as is under the MIT Open Source License. See [LICENSE.md](./LICENSE.md) for details.
2. This software uses Google material icons.
