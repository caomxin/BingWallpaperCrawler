import urllib
from urllib import request
import re
from datetime import datetime


url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&cc=us"
url_ori = "https://www.bing.com"
req = request.Request(url)
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
	html = f.read().decode('utf-8')
#	print(html)
	r = r'/az[^\s]*\.jpg'
	re_img=re.compile(r)
	imgList=re.findall(re_img,html)
	addr = url_ori + imgList[0]
	save_path = r'G:/Pictures/'+datetime.now().strftime('%y%m%d')+'.jpg'
	urllib.request.urlretrieve(addr, save_path)
#	print('今日bing主页的图片已经保存到你的bingWallpaper文件夹')
