# csv模块可用于分析CSV文件中的数据

# import csv
#
# filename = 'sitka_weather_07-2014.csv'
# with open(filename) as f:
#     # 创建一个阅读器对象：
#     reader = csv.reader(f)
#     # 调用next()函数，返回文件中的下一行(只调用next一次，所以得到的是文件的第一行)：
#     header_row = next(reader)
#     # print(header_row)
#     # reader处理文件中以逗号分隔的第一行数据，并将每项数据都作为一个元素储存在列表中
#
#     # 打印文件头及其位置,调用函数enumerate()获取每个元素的索引及其值：
#     for index, column_header in enumerate(header_row):
#         print(index, column_header)


# # 由上述所知，最高气温存储在第二列，提取并读取它：
# import csv
# import matplotlib.pyplot as plt
# from datetime import datetime
#
# filename = 'sitka_weather_07-2014.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     # 添加日期：
#     dates, highs = [], []
#
#     # 读取每一行第一列和第二列的数据,并将第二列转换成数字：
#     for row in reader:
#         current_date = datetime.strptime(row[0], "%Y-%m-%d")
#         dates.append(current_date)
#         high = int(row[1])
#         highs.append(high)
#
#     # print(highs)
#
#     # 绘制图表：
#     fig = plt.figure(dpi=128, figsize=(10, 6))
#     plt.plot(dates, highs, c='red')
#
#     plt.title('Daily high temperatures,July 2014', fontsize=24)
#     plt.xlabel('', fontsize=16)
#     # 绘制斜的日期标签：
#     fig.autofmt_xdate()
#     plt.ylabel('Temperature(F)', fontsize=16)
#
#     # axis='both'表示同时设置x,y轴的坐标刻度
#     plt.tick_params(axis='both', which='major', labelsize=16)
#
#     plt.show()




# # 绘制一整年的最高温度数据,并添加最低温度数据：
# import csv
# import matplotlib.pyplot as plt
# from datetime import datetime
#
# filename = 'sitka_weather_2014.csv'
#
# with open(filename) as f:
#     reader = csv.reader(f)
#     head_row = next(reader)
#
#     dates, highs, lows = [], [], []
#
#     for row in reader:
#         current_date = datetime.strptime(row[0], "%Y-%m-%d")
#         dates.append(current_date)
#
#         high = int(row[1])
#         highs.append(high)
#
#         low = int(row[3])
#         lows.append(low)
#
#     fig = plt.figure(dpi=128, figsize=(10, 6))
#     plt.plot(dates, highs, c='red', alpha=0.5)
#     plt.plot(dates, lows, c='blue', alpha=0.5)
#     # alpha表示颜色透明度，为0表示完全透明
#
#     # 给图表区域着色，来呈现每天的气温范围：
#     # fill_between()接受一个x值系列和两个y值系列，并填充两个y值系列之间的空间：
#     plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
#
#     plt.title("Daily high and low temperatures - 2014", fontsize=24)
#     plt.xlabel('', fontsize=16)
#     plt.ylabel('Temperature(F)', fontsize=16)
#     fig.autofmt_xdate()
#
#     plt.tick_params(axis='both', which='major', labelsize=16)
#
#     plt.show()




# 当数据缺失时会引发异常，因此在读取数据时执行错误检查代码，进行处理：
import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)

    dates, highs, lows = [], [], []

    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])

        except ValueError:
            print(current_date, 'missing date')

        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    # alpha表示颜色透明度，为0表示完全透明

    # 给图表区域着色，来呈现每天的气温范围：
    # fill_between()接受一个x值系列和两个y值系列，并填充两个y值系列之间的空间：
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA", fontsize=20)
    plt.xlabel('', fontsize=16)
    plt.ylabel('Temperature(F)', fontsize=16)
    fig.autofmt_xdate()

    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()














