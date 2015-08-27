from multiprocessing import Pool
import requests
import multiprocessing
from bs4 import BeautifulSoup

urlList = ['http://tieba.baidu.com/p/4002041208',]

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
        for link in soup.find_all('img'):
            file.write('\n')
            file.write(link.get('src'))
			

if __name__ == '__main__':
    running(urlList[0])
		
#if __name__ == '__main__':
    print(urlList)
    manager = multiprocessing.Manager()
    p = Pool(len(urlList))
    q = manager.Queue()
    lock = manager.Lock()
    for url in urlList:
        p.apply_async(running, args=(url,q))
    p.close()
    p.join()
    

