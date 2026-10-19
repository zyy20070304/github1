# ROS2 第2周作业：Publisher → Subscriber 控制仿真机器人

## 环境

- Ubuntu 26.04 LTS（WSL2）
- ROS 2 **Lyrical Luth**

## 功能

用自己编写的发布者节点向 `/turtle1/cmd_vel` 发布速度指令，让 turtlesim 仿真小龟画圆；
再用自己编写的订阅者节点订阅 `/turtle1/pose`，实时打印小龟的位置与朝向。

```
turtle_circle --(/turtle1/cmd_vel, Twist)--> turtlesim --(/turtle1/pose, Pose)--> pose_listener
```

## 运行

```bash
# 终端 1：仿真环境
source /opt/ros/lyrical/setup.bash
ros2 run turtlesim turtlesim_node

# 终端 2：发布速度指令（小龟画圆）
cd ros2_hw && python3 controller.py

# 终端 3：订阅位置并打印
cd ros2_hw && python3 listener.py
```

## 文件说明

| 文件 | 说明 |
|---|---|
| `controller.py` | 发布者节点：向 `/turtle1/cmd_vel` 发布 `geometry_msgs/msg/Twist` |
| `listener.py` | 订阅者节点：订阅 `/turtle1/pose`（`turtlesim_msgs/msg/Pose`） |
| `说明.md` | 节点关系表、运行步骤、验证命令 |

## 备注

ROS 2 Lyrical 中 turtlesim 的消息包已由 `turtlesim.msg` 改为 `turtlesim_msgs.msg`，
旧教程里的 `from turtlesim.msg import Pose` 需要改成 `from turtlesim_msgs.msg import Pose`。
