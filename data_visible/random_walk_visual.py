# 绘制随机漫步图：

# import matplotlib.pyplot as plt
# from random_walk import Randomwalk
#
# # 创建一个实例：
# rw = Randomwalk()
# rw.fill_walk()
#
# # 绘制图形(函数scatter()绘制一系列的点)：
# plt.scatter(rw.x_values, rw.y_values, s=5)
#
# plt.show()



# 给点着色：
import matplotlib.pyplot as plt
from random_walk import Randomwalk

rw = Randomwalk()
rw.fill_walk()

# 调整绘图窗口的尺寸(函数figure()指定图表的宽高、分辨率、背景色)：
# plt.figure(dpi=80, figsize=(10, 6))

# 使用颜色映射来指出漫步中个各点的先后顺序：
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds, edgecolors='none', s=1)

# 突出起点和终点：
plt.scatter(0, 0, c='Blue', edgecolors='none', s=50)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='Blue', edgecolors='none', s=50)

# 隐藏坐标轴：
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()


























