# 制作世界人口地图

# # 查看world_population.json文件(每个元素都是一个包含四个键的字典)，读取其中每个国家2010年的人口数量：
# import json
#
# filename = 'population_data.json'
#
# with open(filename) as f:
#     # 将数据加载到一个列表中(json.load()将数据转换为Python能处理的格式，这里是一个列表)：
#     population_data = json.load(f)
#
#     # 打印每个国家2010年的人口数量：
#     for pop_dict in population_data:
#         # 遍历每个元素：
#         if pop_dict["Year"] == "2010":
#             country_name = pop_dict["Country Name"]
#             # 将人口数量转换为数值(int不能直接将带有小数点的字符串转化成整数，所以先用float转化成浮点数，再用int转换成整数)：
#             population = int(float(pop_dict["Value"]))
#             print(country_name + ": " + str(population))


# # 将国家名显示为国别码：
# import json
# from country_code import get_country_code
#
# filename = 'population_data.json'
#
# with open(filename) as f:
#     population_data = json.load(f)
#
#     for pop_dict in population_data:
#         if pop_dict["Year"] == "2010":
#             country_name = pop_dict["Country Name"]
#             population = int(float(pop_dict["Value"]))
#
#             # 提取国别码：
#             code = get_country_code(country_name)
#             # 如果国别码存在：
#             if code:
#                 print(code + ": " + str(population))
#             else:
#                 print('ERROR' + ' - ' + country_name)




# 制作世界地图：
import json
import pygal
from country_code import get_country_code
from pygal.style import LightColorizedStyle, RotateStyle


filename = 'population_data.json'

with open(filename) as f:
    population_data = json.load(f)

    # 创建一个包含人口数量的字典：
    cc_population = {}

    for pop_dict in population_data:
        if pop_dict["Year"] == "2010":
            country_name = pop_dict["Country Name"]
            population = int(float(pop_dict["Value"]))

            code = get_country_code(country_name)
            if code:
                cc_population[code] = population

# 根据人口数量将所有国家分成三组以作区分：
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_population.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    elif pop > 1000000000:
        cc_pops_3[cc] = pop

# 查看每组分别包含多少个国家：
# print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

# 设置世界地图的样式：
# wm_style = RotateStyle('#336699')
# 加亮颜色主题(使用这个类时不能直接控制使用的颜色，因此可以将LightColorizedStyle作为基本样式)：
# wm_style = LightColorizedStyle

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)

wm = pygal.Worldmap(style=wm_style)
wm.title = 'World Population in 2010, by Country'
# wm.add('2010', cc_population)
# 颜色越深表示人口越多：
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')




















