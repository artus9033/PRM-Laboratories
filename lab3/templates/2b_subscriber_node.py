#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String  # import wiadomości String z pakietu std_msgs
from datetime import datetime
import socket
import threading

SUB_TOPIC_NAME = ...  # TODO-PRM: 2b) inicjalizacja Subscribera - nazwa tematu


def subscriberCallback(msg: String):
    # TODO-PRM: 2b) wypisanie danych otrzymanych we wiadomości
    rospy.loginfo(
        f"[prm_subscriber_node] [{datetime.now().strftime('%H:%M:%S')}] węzeł {rospy.get_caller_id()} przetwarza w wątku {threading.get_ident()} dane z tematu {SUB_TOPIC_NAME}: '{...}'")


if __name__ == '__main__':
    rospy.init_node("prm_subscriber_node")

    rospy.loginfo(
        f"[prm_subscriber_node] przestrzeń nazw tego węzła: {rospy.get_namespace()}")

    hostname, _, ipAddresses = socket.gethostbyname_ex(socket.getfqdn())
    rospy.loginfo(
        f"[prm_publisher_node] nazwa hosta: {hostname}, adres{'y' if len(ipAddresses) > 1 else ''} IP środowiska węzła: {', '.join(ipAddresses)}")

    rospy.loginfo(
        f"[prm_subscriber_node] główny wątek węzła: {threading.get_ident()}")

    # TODO-PRM: 2b) inicjalizacja Subscribera
    rospy.Subscriber(name=SUB_TOPIC_NAME, data_class=...,
                     callback=subscriberCallback)

    rospy.spin()  # run forever
