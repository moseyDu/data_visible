# 此程序自动下载github上星级最高的Python项目的信息，并对这些信息进行可视化
# 查看API调用：https://api.github.com/search/repositories?q=language:python&sort=stars
# 查看搜索API的速率限制：https://api.github.com/rate_limit
# requests包让Python程序能轻松地向网站请求信息以及检查返回的响应


# import requests
#
# # 执行API调用并存储响应
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# r = requests.get(url)
# # r为一个响应对象，包含一个名为status_code的属性，让我们知道请求是否成功了(状态码200表示成功)：
# print("Status code:", r.status_code)
#
# # API响应返回json格式的信息，因此我们使用json()将这些信息转换为一个Python字典,并将其储存在变量中：
# response_dict = r.json()
# print("Total count:", response_dict['total_count'])
#
# # # 打印response_dict中的键；
# # print(response_dict.keys())
#
# # 探索有关仓库的信息(获悉我们共获得了多少个仓库的信息)：
# repo_dicts = response_dict['items']
# # items包含一个列表，列表中含有很多字典，获取列表的长度即可知道包含多少字典：
# print("the count of repositories:", len(repo_dicts))
#
# # 研究第一个仓库：
# repo_dict_1 = repo_dicts[0]
# print("the number of Keys:", len(repo_dict_1))
# # 打印每个key值：
# for key in sorted(repo_dict_1.keys()):
#     print(key)
#
# # 打印第一个仓库某些相关的信息：
# print("\nSelect information about first repository:")
# print("Name:", repo_dict_1['name'])
# print("Owner:", repo_dict_1['owner']['login'])
# print("Stars:", repo_dict_1['stargazers_count'])
# print("Descriptions:", repo_dict_1['description'])
#
# # 打印每一个仓库的某些相关信息：
# print("\nSelect information about each repository:")
# for repo_dict in repo_dicts:
#     print("\nName:", repo_dict['name'])
#     print("Owner:", repo_dict['owner']['login'])
#     print("Stars:", repo_dict['stargazers_count'])
#     print("Descriptions:", repo_dict['description'])


# # 数据可视化：创建交互条形图，表示每个项目获得的星数
# import requests
# import pygal
# from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
#
# # 执行API调用并响应：
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# r = requests.get(url)
# print("Status code:", r.status_code)
#
# # 将API响应储存在一个变量中：
# response_dict = r.json()
# print("Total count:", response_dict['total_count'])
#
# # 研究有关仓库的信息：
# repo_dicts = response_dict['items']
#
# # 获取项目名称和对应的星数：
# names, stars = [], []
# for repo_dict in repo_dicts:
#     names.append(repo_dict['name'])
#     stars.append(repo_dict['stargazers_count'])
#
# # 设置图表的样式：
# my_config = pygal.Config()
# my_config.x_label_rotation = 45
# # show_legend=False不显示图例：
# my_config.show_legend = False
# my_config.title_font_size = 24
# # 设置主标签和副标签字体大小(主标签是y轴上5000整数倍的刻度，副标签是x轴上的项目名及y轴上的大部分数字)：
# my_config.major_label_font_size = 18
# my_config.label_font_size = 14
# # 将较长的项目名缩短为15个字符：
# my_config.truncate_label = 15
# # 隐藏图表中的水平线：
# my_config.show_y_guides = False
# # 设置自定义宽度：
# my_config.width = 1000
#
# # 绘制数据表：
# my_style = LS('#333366', base_style=LCS)
# chart = pygal.Bar(my_config, style=my_style)
# chart.title = 'Most-Starred Python Projects on Github'
# chart.x_labels = names
#
# chart.add('', stars)
# chart.render_to_file('python_repos.svg')


# 添加条形图自定义描述:
import pygal
import requests
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

response_dict = r.json()
print("Total count:", response_dict['total_count'])

repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    name = repo_dict['name']
    names.append(name)

    # 在图表中添加可单机跳转的链接：
    plot_dict = {'value': repo_dict['stargazers_count'],
                 'label': repo_dict['description'],
                 'xlink': repo_dict['html_url']}
    plot_dicts.append(plot_dict)

my_config = pygal.Config()
my_config.width = 1000
my_config.show_y_guides = False
my_config.show_legend = False
my_config.x_label_rotation = 45
my_config.truncate_label = 15
my_config.title_font_size = 24
my_config.major_label_font_size = 18
my_config.label_font_size = 14

my_style = LS("#333366", base_style=LCS)
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos1.svg')





















