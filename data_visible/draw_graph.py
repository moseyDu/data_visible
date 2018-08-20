# 使用matplotlib制作简单的图表：


# 绘制折线图：
# import matplotlib.pyplot as plt
#
# squares = [1, 4, 9, 16, 25]
# # plot()尝试根据这些数字绘出有意义的图形
# plt.plot(squares)
# plt.show()


# # 修改设置：
# import matplotlib.pyplot as plt
#
# # plot默认第一个x为0，对应的第一个y为1，为改变这种默认方式，可以同时提供输入值和输出值：
# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
# # linewidth表示绘制的线条的粗细：
# plt.plot(input_values, squares, linewidth=5)
#
# # 设置标题，并给坐标轴加上标签：
# plt.title("Squares Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of value", fontsize=14)
#
# # 设置刻度标记的大小(tick_params设置刻度的样式，指定的实参axis影响刻度)：
# plt.tick_params(axis='both', labelsize=14)
#
# plt.show()




# # 使用scatter()函数绘制散点图：
# import matplotlib.pyplot as plt
#
# # # 绘制一个点，s设置了使用的点的尺寸：
# # plt.scatter(2, 4, s=200)
#
# # 绘制一系列点，可像scatter传递两个分别包含x值和y值的列表：
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# plt.scatter(x_values, y_values, s=100)
#
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of value", fontsize=14)
#
# plt.tick_params(axis='both', which='major', labelsize=14)
#
# plt.show()


# 自动计算数据(数据点过多时，可使用Python循环来完成)：
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

# # matplotlib绘制时默认为蓝色点黑色轮廓，要删除数据点的轮廓，可传递实参edgecolors;要修改数据点的颜色，可使用参数c:
# plt.scatter(x_values, y_values, c='red', edgecolors='none', s=10)

# 颜色映射：从起始颜色渐变到结束颜色：
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=10)

plt.title("Squares Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

# 函数axis()指定了每个坐标轴的取值范围(x和y坐标轴的最小值和最大值)：
plt.axis([0, 1100, 0, 1100000])

# 展示图表：
# plt.show()

# 保存图表(第一个实参表示以什么文件名保存，第二个实参指定将图表多余的空白区域裁剪掉，如果想保留，则省略)：
plt.savefig('squares_plot.png', bbox_inches='tight')




