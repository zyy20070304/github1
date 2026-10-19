#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
controller.py —— 发布者（Publisher）节点
功能：周期性向 /turtle1/cmd_vel 发布速度指令，让小龟画圆
话题：/turtle1/cmd_vel     消息类型：geometry_msgs/msg/Twist
      linear.x  = 线速度 (m/s)
      angular.z = 角速度 (rad/s)
转弯半径 R = v / ω
"""
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TurtleCircle(Node):
    """一个最简单的发布者节点"""

    def __init__(self):
        super().__init__('turtle_circle')          # ① 节点名：ros2 node list 能看到
        # ② 创建发布者：话题名 + 消息类型 + 队列长度
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        # ③ 定时器：每 0.1 秒执行一次 tick（10 Hz）
        self.timer = self.create_timer(0.1, self.tick)
        self.count = 0
        self.get_logger().info('turtle_circle 已启动，开始画圆（Ctrl+C 停止）')

    def tick(self):
        msg = Twist()                # 每周期新建一条消息
        msg.linear.x = 2.0           # 前进 2 m/s
        msg.angular.z = 1.0          # 左转 1 rad/s → 半径 2 m
        self.pub.publish(msg)        # ④ 发布出去
        self.count += 1
        if self.count % 10 == 0:     # 每秒打印一次，避免刷屏
            self.get_logger().info(f'已发布 {self.count} 条速度指令')


def main():
    rclpy.init()                     # 初始化 ROS2
    node = TurtleCircle()
    try:
        rclpy.spin(node)             # 一直运行，直到 Ctrl+C
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
