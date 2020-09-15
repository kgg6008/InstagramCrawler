# Instagram Web Scrapper(Crawler)

## What is this?
This is crawler Instagram.  
```main.py``` is example of test crawler.  
I seperated contexts and hashtags by '$|||$', so if you want to split then split by '$|||$'.  
Before the usage please read [Instagram Help Center](https://www.facebook.com/help/instagram/1188470931252371).

## install pip list
```bash
pip install -r requirement.txt 
```
## Usage
You must install chromedriver.  
```
https://chromedriver.chromium.org/downloads
```
### Example Code
#### Input
```python
from InstagramCrawler import InstagramCrawler

instagram_crawler = InstagramCrawler(chrome_driver_path=chrome_driver_path,instagram_email=instagram_email,instagram_pw=instagram_pw)
rs = instagram_crawler.start_crawler('스칼렛요한슨',post_num=10)

```

#### Output
````
[{'post_writer': '', 'post_context': '𝗛𝗲𝘆, 𝗳𝗲𝗹𝗹𝗮𝘀.$|||$⠀$|||$Scarlett Photos ❤ INSTAGRAM $|||$Scarlett Gifs ❤ TWITTER ', 'post_hashtag': '#scarlettjohansson$|||$#blackwidow$|...
````
