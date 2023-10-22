#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy

if __name__ == '__main__':
    rospy.init_node("prm_test_node")

    rospy.loginfo(
        f"[prm_test_node] przestrzeń nazw tego węzła: {rospy.get_namespace()}")

    rospy.spin()  # run forever
