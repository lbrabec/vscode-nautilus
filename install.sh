#!/usr/bin/bash

set -e

EXTENSION_DIR=/usr/share/nautilus-python/extensions

echo "Installing VS Code / VS Codium extension for Nautilus..."

read -p "Binary name (code or codium): " BINARY

if [ $BINARY == "code" ]; then
    cp open-vscode.py $EXTENSION_DIR/open-vscode.py
elif [ $BINARY == "codium" ]; then
    cp open-vscode.py $EXTENSION_DIR/open-vscodium.py
    sed -i "s/BINARY = 'code'/BINARY = '$BINARY'/g" $EXTENSION_DIR/open-vscodium.py
    sed -i "s/NAME = 'VS Code'/NAME = 'VS Codium'/g" $EXTENSION_DIR/open-vscodium.py
    sed -i "s/class OpenVSCodeExtension/class OpenVSCodiumExtension/g" $EXTENSION_DIR/open-vscodium.py
else
    echo "Unsupported binary, please edit open-vscode.py manually and copy to $EXTENSION_DIR/"
    exit 1
fi

echo "Installation done."

