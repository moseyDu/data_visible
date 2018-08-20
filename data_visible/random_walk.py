# 随机漫步：

from random import choice

class Randomwalk():
    """一个生成随机漫步数据的类"""

    def __init__(self, num_points=50000):
        """初始化随机漫步的属性"""

        # 储存随机漫步的次数：
        self.num_points = num_points

        # 所有随机漫步都始于(0, 0):
        self.x_values = [0]
        self.y_values = [0]


    def fill_walk(self):
        """计算漫步包含的所有的点"""

        # 不断漫步，达到列表指定的长度：
        while len(self.x_values) < self.num_points:

            # 随机决定前进方向和这个方向的前进距离(如果x_step为0表示垂直移动，如果y_step为0表示水平移动)：
            x_direction = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步：
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值：
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            # 将下一个值分别添加到列表的末尾：
            self.x_values.append(next_x)
            self.y_values.append(next_y)















