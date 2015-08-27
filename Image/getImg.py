import re,urllib.request


def getpage(url):
	tieba_url=urllib.request.urlopen(url)
	image_page=tieba_url.read().decode("UTF-8")
	return image_page


def get_image_url(image_page):
	reg=r'src="(.*?\.jpg)" pic_ext='
	image_url=re.compile(reg)
	image_url_list=image_url.findall(image_page)
	index = 0
	for i in image_url_list:
	    index += 1
	    urllib.request.urlretrieve(i,"%s.jpg" %index)
	
page=getpage("http://tieba.baidu.com/p/3998260182")
listes=get_image_url(page)
print(listes)