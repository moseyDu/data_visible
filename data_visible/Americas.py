# # 创建一个突出北美、中美和南美的简单地图(Pygal提供了图表类型Worldmap来制作地图)：
#
# import pygal
#
# wm = pygal.Worldmap()
# wm.title = 'North, Center, and South America'
#
# # add()接受一个标签和一个列表，后者包含要突出的国家的国别码，每次调用add时会为指定的国家选择一种颜色：
# wm.add('North America', ['ca', 'mx', 'us'])
# wm.add('Center America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
# wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])
#
# wm.render_to_file('Americas.svg')


# 在地图上呈现数据(显示三个北美国家的人口数量)：
import pygal

wm = pygal.Worldmap()
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('North America.svg')

















