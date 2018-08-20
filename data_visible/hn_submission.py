# 执行API调用，返回Hacker News上当前热门文章的ID，再查看每篇排名靠前的文章

import requests
from operator import itemgetter

# 执行API调用并储存响应(这个调用返回一个列表，包含当前最热门的500篇文章的ID)：
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# 处理文章有关的信息：
submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[0:30]:
    # 获取前30的文章，对每篇文章，都做一个调用：
    url = 'https://hacker-news.firebaseio.com/v0/item' + str(submission_id) + '.json'
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    # 创建一个空列表，储存每个文章的信息：
    submission_dict = {'title': response_dict['title'],
                       'link': 'https://hacker-news.firebaseio.com/v0/item?id=' + str(submission_id),
                       'comments': response_dict.get('descendants', 0)}
    # 不确定某个键是否包含在字典中时，可以用方法dict.get()，它在指定的键存在时返回与之关联的值，不存在时返回指定的值
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)
for submission_dict in submission_dicts:
    print('\nTitle:', submission_dict['title'])
    print('Discuss link:', submission_dict['link'])
    print('Comments:', submission_dict['comments'])










































































