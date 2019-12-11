# VS Code extension for Nautilus
This extension adds 'Open VS Code' item to right click context menu in Nautilus. Requires `nautilus-python`.

To install on Fedora run:

    dnf copr enable lbrabec/vscode-nautilus
    dnf install vscode-nautilus

To install from source, clone this repo and run:

    cd vscode-nautilus
    sudo cp open-vscode.py /usr/share/nautilus-python/extensions/