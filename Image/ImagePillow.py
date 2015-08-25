Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from PIL import Image,ImageDraw,ImageFont,ImageFilter
>>> import random
>>> def rndChar():
	return chr(random.randint(65,90))

>>> def radColor():
	return(random.randint(65,255),random.randint (64,255),random.randint (64,255))

>>> def radColor2():
	return(random.randint(32,127),random.randint (32,127),random.randint (32,127))

>>> width = 60*4
>>> height = 60
>>> image = Image.new('RGB',(width,height),(255,255,255))
>>> font= ImageFont.truetype('Airal.ttf',36)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    font= ImageFont.truetype('Airal.ttf',36)
  File "C:\Python34\lib\site-packages\PIL\ImageFont.py", line 260, in truetype
    return FreeTypeFont(font, size, index, encoding)
  File "C:\Python34\lib\site-packages\PIL\ImageFont.py", line 140, in __init__
    self.font = core.getfont(font, size, index, encoding)
OSError: cannot open resource
>>> font= ImageFont.truetype()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    font= ImageFont.truetype()
  File "C:\Python34\lib\site-packages\PIL\ImageFont.py", line 260, in truetype
    return FreeTypeFont(font, size, index, encoding)
  File "C:\Python34\lib\site-packages\PIL\ImageFont.py", line 142, in __init__
    self.font_bytes = font.read()
AttributeError: 'NoneType' object has no attribute 'read'
>>> font= ImageFont.truetype("微软雅黑",36)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    font= ImageFont.truetype("微软雅黑",36)
  File "C:\Python34\lib\site-packages\PIL\ImageFont.py", line 260, in truetype
    return FreeTypeFont(font, size, index, encoding)
  File "C:\Python34\lib\site-packages\PIL\ImageFont.py", line 140, in __init__
    self.font = core.getfont(font, size, index, encoding)
OSError: cannot open resource
>>> draw = ImageDraw.Draw(image)
>>> for x in range(width)
SyntaxError: invalid syntax
>>> for x in range(width):
	for y in range(height)
	
SyntaxError: invalid syntax
>>> for x in range(width):
	for y in range(height):
		draw.point((x,y),fill = radColor())

		
>>> image = image.filter(ImageFilter.BLUR)
>>> image.save("code.jpg","jpeg")
>>> 
