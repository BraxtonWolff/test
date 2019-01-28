# 豆瓣图书Top250
# Url:'https://www.jqhtml.com/13275.html'

import requests
import time
from bs4 import BeautifulSoup


headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'
}

url='https://book.douban.com/top250?start=0'


resp=requests.get(url,headers=headers)

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

soup=BeautifulSoup(resp.text,'lxml')

alldiv=soup.find_all('div',class_='pl2')

# 书名
for a in alldiv:
    names=a.find('a')['title']
    print(names)

# 作者
allp=soup.find_all('p',class_='pl')
for p in allp:
    authers=p.get_text()
    print(authers)
