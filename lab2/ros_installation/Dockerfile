# TODO-PRM: 1a) ustaw obraz bazowy na odpowiednią wersję ubuntu kompatybilną z ROS w wersji ze skryptu
FROM ...:...

# przygotowanie konfiguracji strefy czasowej dla pakietu tzdata, aby uniknąć konfiguracji interaktywnej
RUN echo 'Etc/UTC' > /etc/timezone && \
    ln -s /usr/share/zoneinfo/Etc/UTC /etc/localtime

RUN apt update
# TODO-PRM: 1a) zainstaluj narzędzia wskazane w skrypcie
...

# instalacja narzędzia rosdep
RUN pip install -U rosdep

# konfiguracja narzędzia rosdep
RUN rosdep init
RUN rosdep update

# TODO-PRM: 1a) zainstaluj ROS (wiele komend)
...
...
...
...

# TODO-PRM: 1a) skonfiguruj ROS w .bashrc (wiele komend)
...
...

# poniżej: entrypoint uruchamiający proces rosmastera
COPY ros_entrypoint.sh /ros_entrypoint.sh
RUN chmod a+x /ros_entrypoint.sh

VOLUME /root/prm

ENTRYPOINT [ "/ros_entrypoint.sh" ]
