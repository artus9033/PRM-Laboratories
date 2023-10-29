#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import cv2
import numpy as np
import rospy
from datetime import datetime
import socket
...  # TODO-PRM: 5b) zaimportowanie PRMImageStamped

if __name__ == '__main__':
    rospy.init_node("prm_publisher_node")

    # TODO-PRM: 5b) inicjalizacja Publishera
    pub = rospy.Publisher(name="prm_tpc", data_class=..., queue_size=10)
    # jedna instancja dla uniknięcia tworzenia nowego wystąpienia co iterację
    msg = ...  # TODO-PRM: 5b) utworzenie instancji wiadomości PRMImageStamped

    r = rospy.Rate(1)
    while not rospy.is_shutdown():
        # TODO-PRM: 5b) aktualizacja danych poniżej
        ...
        # TODO-PRM: 5b) opublikowanie wiadomości
        ...

        r.sleep()
