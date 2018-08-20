# 掷骰子：

# from die import Die
# # 创建一个实例(6面的骰子为D6,8面的骰子为D8)：
# D6 = Die()
#
# # 投掷几次骰子，并将结果存在列表中：
# results = []
#
# for roll_num in range(100):
#     result = D6.roll()
#     results.append(result)
#
# print(results)


# # 分析结果,计算每个点出现的次数：
# from die import Die
#
# D6 = Die()
#
# results = []
# for roll_num in range(1000):
#     result = D6.roll()
#     results.append(result)
#
# # 创建空列表，统计每种点数各出现了多少次：
# frequencies = []
# for value in range(1, D6.num_sides+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)
#
# print(frequencies)


# 结果可视化(绘制直方图)：
from die import Die
import pygal

D6 = Die()

results = []
for roll_num in range(1000):
    result = D6.roll()
    results.append(result)

frequencies = []
for value in range(1, D6.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化处理：
# 创建一个实例：
hist = pygal.Bar()

# 设置标题，坐标轴：
hist.title = 'Results of rolling one D6 1000 times'
hist.x_label = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

# 将一系列值添加到图表中,并制定文件的名称，扩展名必须是.svg：
hist.add('D6', frequencies)
# add第一个参数表示要添加的值的标签
hist.render_to_file('die_visual.svg')





