# -*-coding:utf-8-*-

# 豆瓣图书Top250
# Url:'https://www.jqhtml.com/13275.html'
# BeautifulSoup_Doc:'https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/'

import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'
}

url = 'https://book.douban.com/top250?start=0'


resp = requests.get(url, headers=headers)

if resp.status_code == 200:
    print('成功链接')
elif resp.status_code == 301:
    print('跳转')
elif resp.status_code == 404:
    print('文件不存在')
elif resp.status_code == 403:
    print('无权限访问')
elif resp.status_code == 502:
    print('服务器错误')
else:
    print('链接失败')

soup = BeautifulSoup(resp.text, 'lxml')

# 标题
title = soup.title.text.split('_')[0]

# 书名
alldiv = soup.find_all('div', class_='pl2')
for a in alldiv:
    names = a.find('a')['title']

# 作者
allp = soup.find_all('p', class_='pl')
for p in allp:
    authers = p.get_text()

# 评分
starspan = soup.find_all('span', class_='rating_nums')
for s in starspan:
    scores = s.get_text()

# 评价人数
people = soup.find_all('span', class_='pl')
for m in people:
    peoples = m.get_text()

# 简介
sumspan = soup.find_all('span', class_='inq')
for i in sumspan:
    sums = i.get_text()


# for name,auther,score,sum in zip(names,authers,scores,sums):
#     name='书名:'+str(name)+'\n'
#     auther='作者:'+str(auther)+'\n'
#     score='评分:'+str(score)+'\n'
#     sum='简介:'+str(sum)+'\n'
#     data=name+auther+score+sum
#     print(data)

for name, auther, score, peoples, sum in zip(alldiv, allp, starspan, people, sumspan):
    name = '书名:'+str(name.find('a')['title'])+'\n'
    auther = '作者:'+str(auther.get_text())+'\n'
    score = '评分:'+str(score.get_text())+'\n'
    peoples = '评价人数:'+str(peoples.get_text().replace(' ',
                                                     '').replace('(', '').replace(')', '').replace('\n', ''))+'\n'
    sum = '简介:'+str(sum.get_text())+'\n'
    data = name+auther+score+peoples+sum
    print(data)
