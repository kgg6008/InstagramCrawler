from InstagramCrawler import InstagramCrawler

if __name__ =='__main__':
    instagram_crawler = InstagramCrawler(chrome_driver_path=chrome_driver_path,instagram_email=email,instagram_pw=pw)
    rs = instagram_crawler.start_crawler('스칼렛요한슨',post_num=10)
    print(rs)