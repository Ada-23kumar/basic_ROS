<head>basic_ROS
Step 1 — Creating custom talker_listener package
Remember when we started learning ROS1 and made a custom package with a publisher and subscriber pair? One node publishes and the other constantly listens over a topic. Let’s do that again!

Create our workspace called “ros2_ws”
<div>
<code>mkdir -p ~/ros2_ws/src</code>
</div>

2. Build the workspace

ROS1 uses catkin, but ROS2 uses colcon to build packages

<code>cd ros2_ws
colcon build
</code>

At this point, you will see “0 packages finished” in the terminal (because there are no packages yet). Additionally, you will now have build, install and logs folders in the ros2_ws.

3. Create a new talker package (we use python)
   
<code>cd ros2_ws/src
ros2 pkg create --build-type ament_python talker_listener
</code>

Similarly, we can also make a cpp package. Please look at ROS2 official guide.
