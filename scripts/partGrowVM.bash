#!/bin/bash

if hash growpart 2>/dev/null; then
    echo "Growpart odnaleziony"
else
    echo "Instalacja narzędzi..."

    sudo apt install -y cloud-guest-utils
fi

growpart /dev/sda 3
resize2fs /dev/sda3
