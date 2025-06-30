#!/bin/bash
# Install GNOME extensions from list
while read -r extension; do
    echo "Installing extension: $extension"
    # Add installation logic here if needed
done < ~/gnome-extensions-list.txt
