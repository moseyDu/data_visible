# 获取两个字母的国别码（用国别码表示国家）：

# # Pygal使用的国别码储存在模块i18n中,字典COUNTRIES包含的键和值分别为国别码和国名：
# from pygal.i18n import COUNTRIES
# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code, COUNTRIES[country_code])


# 编写一个函数：
from pygal.i18n import COUNTRIES

def get_country_code(country_name):
    """根据指定的国家，返回对应的国别码"""

    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    # 如果没有找到对应国家，则返回None：
    return None














