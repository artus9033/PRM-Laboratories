#!/bin/bash

if hash growpart 2>/dev/null; then
    echo "Growpart odnaleziony"
else
    echo "Instalacja narzędzi..."

    sudo apt install -y cloud-guest-utils
fi

sudo growpart /dev/sda 3
sudo resize2fs /dev/sda3
