#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
listener.py —— 订阅者（Subscriber）节点
功能：订阅 /turtle1/pose，打印小龟的位置和朝向
话题：/turtle1/pose        消息类型：turtlesim_msgs/msg/Pose
      （注意：ROS2 Lyrical 里已从 turtlesim.msg 改成 turtlesim_msgs.msg，
        视频里写的 from turtlesim.msg import Pose 在新版本会报 ModuleNotFoundError）
      x, y   位置
      theta  朝向（弧度）
      linear_velocity / angular_velocity  当前速度
"""
import rclpy
from rclpy.node import Node
from turtlesim_msgs.msg import Pose


class PoseListener(Node):
    """一个最简单的订阅者节点"""

    def __init__(self):
        super().__init__('pose_listener')          # ① 节点名
        # ② 创建订阅者：消息类型 + 话题名 + 回调函数 + 队列长度
        self.sub = self.create_subscription(
            Pose, '/turtle1/pose', self.on_pose, 10)
        self.n = 0
        self.get_logger().info('pose_listener 已启动，等待 /turtle1/pose ...')

    def on_pose(self, msg):
        """每收到一条消息就调用一次（回调）"""
        self.n += 1
        if self.n % 10 == 0:       # 每 10 条打印一次（turtlesim 默认约 62 Hz）
            self.get_logger().info(
                f'x={msg.x:5.2f}  y={msg.y:5.2f}  θ={msg.theta:6.2f} rad  '
                f'v={msg.linear_velocity:4.2f}  ω={msg.angular_velocity:4.2f}')


def main():
    rclpy.init()
    node = PoseListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
