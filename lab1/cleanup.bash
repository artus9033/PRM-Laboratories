#!/bin/bash

read -p "Czy na pewno chcesz przywrócić stan początkowy laboratorium? To usunie wszystkie pliki. [Y/N] " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1
fi

cd ~/Desktop/PRM-Laboratories/lab1
git restore . # restore original lab contents
docker stop $(docker ps -a -q) # stop all running containers
docker container prune -f # remove all stopped containers
docker image rm http-server ros-turtle # remove result images built by students during the lab
history -c && history -w # clear terminal history
