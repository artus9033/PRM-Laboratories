#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String  # import wiadomości String z pakietu std_msgs
from datetime import datetime
import socket
from time import sleep

if __name__ == '__main__':
    rospy.init_node("prm_publisher_node")

    rospy.loginfo(
        f"[prm_publisher_node] przestrzeń nazw tego węzła: {rospy.get_namespace()}")

    hostname, _, ipAddresses = socket.gethostbyname_ex(socket.getfqdn())
    rospy.loginfo(
        f"[prm_publisher_node] nazwa hosta: {hostname}, adres{'y' if len(ipAddresses) > 1 else ''} IP środowiska węzła: {', '.join(ipAddresses)}")

    # TODO-PRM: 2a) inicjalizacja Publishera
    pub = rospy.Publisher(name=..., data_class=..., queue_size=10)
    # jedna instancja dla uniknięcia tworzenia nowego wystąpienia co iterację
    msg = String()

    while not rospy.is_shutdown():
        # TODO-PRM: 2a) aktualizacja danych poniżej
        ...
        # TODO-PRM: 2a) opublikowanie wiadomości
        ...

        sleep(2)
