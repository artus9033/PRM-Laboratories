#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import rospy
from datetime import datetime
import socket
import threading
import numpy as np
import matplotlib.pyplot as plt
...  # TODO-PRM: 5b) zaimportowanie PRMImageStamped

SUB_TOPIC_NAME = "prm_tpc"


# TODO-PRM: 5b) anotacja typu odpowiedniej klasy wiadomości
def subscriberCallback(msg: ...):
    ...  # TODO-PRM: 5b) przetwarzanie wiadomości


if __name__ == '__main__':
    plt.ion()
    plt.show()

    rospy.init_node("prm_subscriber_node")

    rospy.Subscriber(name=SUB_TOPIC_NAME, data_class=...,  # TODO-PRM: 5b) inicjalizacja Subscribera z odpowiednią klasą wiadomości
                     callback=subscriberCallback)

    rospy.spin()  # run forever
