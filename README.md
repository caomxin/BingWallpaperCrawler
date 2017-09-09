# BingWallpaperCrawler
Using python3 to crawl the Bing wallpaper


# How to use
1. Download the ["crawler.py"](https://github.com/caomxin/CrawlBingWallpaper/blob/master/crawler.py) python file to your file system
2. Run it in command line with argument `python crawler.py`. 
3. And it will automatically save today's bing wallpaper to your computer. 

The default location is "G:/Pictures/", you can modify it directly in the source code. Thank you!

## Besides
- If you are more interested other region's bing wallpaper today, you can easily do this by changing the url in the source file.
Specifically, if you change `url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&cc=us"` 
to `url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&cc=cn"`, 
it will download the Chinese Bing website wallpaper for you. 

## The meaning of the url in the crawler.py
Given `url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&cc=us"`

- `idx` means index
    - if you change it to -1, it will download the next day's wallpaper for you(i.e. tomorrow's wallpaper);
    - if you change it to 1(or other positive number), it will download the wallpaper 1 day before(i.e. yesterday);
- `n` means the number of wallpapers it will load, with maximum number 8; 
    - However, in the source code, I simplify the problem to download only the first picture that loaded. But you can change this by modifying `addr = url_ori + imgList[0]` and `savepath` name. It's quite easy.

# Acknowledgement
[舞恸零一's blog](https://liwei2.com/2014/07/11/27.html)
