# 投掷两个骰子：

# from die import Die
# import pygal
#
# # 创建2个实例：
# D61 = Die()
# D62 = Die()
#
# # 存放结果：
# results = []
# for roll_num in range(1000):
#     result = D61.roll() + D62.roll()
#     results.append(result)
#
# # 分析结果：
# frequencies = []
# max_result = D61.num_sides + D62.num_sides
# for value in range(2, max_result+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)
#
# # 结果可视化：
# hist = pygal.Bar()
#
# hist.title = 'Results of rolling two D6 dice 1000 times'
# hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
# hist.x_title = 'Result'
# hist.y_title = 'Frequency of Result'
#
# hist.add('D61+D62', frequencies)
# hist.render_to_file('dice_visual.svg')




# 投掷一个6面和一个10面的骰子：
from die import Die
import pygal

# 创建2个实例：
D6 = Die()
D10 = Die(10)

# 存放结果：
results = []
for roll_num in range(50000):
    result = D6.roll() + D10.roll()
    results.append(result)

# 分析结果：
frequencies = []
max_result = D6.num_sides + D10.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 结果可视化：
hist = pygal.Bar()

hist.title = 'Results of rolling D6 and D10 dice 50000 times'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6+D10', frequencies)
hist.render_to_file('dice_visual.svg')














































