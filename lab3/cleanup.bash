#!/bin/bash

read -p "Czy na pewno chcesz przywrócić stan początkowy laboratorium? To usunie wszystkie pliki. [Y/N] " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1
fi

cd ~/Desktop/PRM-Laboratories/lab3
sudo rm -rf ../lab2/container_fs/ # clear container volume contents
git restore . # restore original lab contents
docker stop $(docker ps -a -q) # stop all running containers
docker container prune -f # remove all stopped containers
history -c && history -w # clear terminal history
