from multiprocessing import Pool
import requests
import multiprocessing
from bs4 import BeautifulSoup
import re

urlList = ['http://www.qiushibaike.com/hot/page/1',]

for index in range(1,5):
    url = 'http://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=%d' % (index*50)
    urlList.append(url)

def running(url):
    print(url)
    html = requests.get(url)
    if html.status_code == 200:
        print(html.encoding)
        html_text = html.text
    soup = BeautifulSoup(html_text,'html.parser')
    with open("td.txt","a+",encoding= 'UTF-8') as file:
        for link in soup.find_all('div',attrs={"class": "author"}):
            if link.text == None:
                break
            print(link.get_text())
            file.write('\n')
            file.write(link.text)
			

if __name__ == '__main__':
    running(urlList[0])
		

