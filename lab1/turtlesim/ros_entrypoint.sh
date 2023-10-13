#!/bin/bash

source /opt/ros/melodic/setup.bash

roscore &

rosrun turtlesim turtlesim_node
