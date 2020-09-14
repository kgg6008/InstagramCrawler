# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 21:55:58 2020

@author: h
"""

# instagram crawler
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from math import nan

class InstagramCrawler:
    """
    Web scrapping instagram by Selenium.
    :Args
        arg1 : chrome_driver_path: (str) Path of chrome driver
        arg2 : instagram_email: (str) Instagram input email/id/phone ...
        arg3 : instagram_pw: (str) Instagram password
    todo:
        add image or video scrapping
    """
    def __init__(self, chrome_driver_path, instagram_email, instagram_pw):
        self.webdriver_path = chrome_driver_path
        self.__email = instagram_email
        self.__pw = instagram_pw

    def _get_post(self, html_info):
        """
        Function for scrapping post
        :param html_info: (str) page source of selenium
        :return: (dic) post information like  post_writer, post_context, etc.
        """
        bs = BeautifulSoup(html_info, 'lxml')
        post = bs.find('div', {'class': 'EtaWk'})
        post_writer = post.find('span').find('a').text
        post_context = '$|||$'.join(
            list(map(str, post.find('span', {'class': ''}).findAll(text=True, recursive=False))))
        if not post_context:
            post_context = nan
        post_hashtag = '$|||$'.join(
            [hashtag.strip() for hashtag in list(map(lambda x: x.text, post.findAll('a', {'class': 'xil3i'}))) if
             hashtag.strip().startswith('#')])
        if not post_hashtag:
            post_hashtag = nan
        post_uploaded = bs.find('time', {'class': '_1o9PC Nzb55'}).get('datetime')
        try:
            post_viewed = bs.find('span', {'class': 'vcOH2'}).find('span').text
        except:
            post_viewed = nan
        try:
            post_liked = bs.find('div', {'class': 'Nm9Fw'}).find('span').text
        except:
            post_liked = nan
        return {
            'post_writer': post_writer,
            'post_context': post_context,
            'post_hashtag': post_hashtag,
            'post_uploaded': post_uploaded,
            'post_viewed': post_viewed,
            'post_liked': post_liked
        }

    def start_crawler(self, search_tag, post_num=100):
        """
        Start scraping as many as post_num
        :param search_tag: (str) The tag which you want to find post.
        :param post_num: (int) The number of data you want to crawling. (Default :100)
        :return: (list)list of instagram post information dictionary
        :return_example : [{'post_writer': 'writer', 'post_context':'post_context',... }, ... ]
        """
        result_set = []
        base_instagram_url = 'https://www.instagram.com'
        search_tag_instagram = 'https://www.instagram.com/explore/tags/{}'.format(search_tag)
        driver = webdriver.Chrome(self.webdriver_path)
        driver.get(base_instagram_url)
        time.sleep(2)
        input_id = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[0]
        input_id.clear()
        input_id.send_keys(self.__email)
        time.sleep(1)
        input_pw = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[1]
        input_pw.clear()
        input_pw.send_keys(self.__pw)
        input_pw.submit()
        time.sleep(5)
        try:
            error_occured = driver.find_element_by_id('slfErrorAlert')

            if error_occured:
                print(error_occured.text)
                driver.close()
            return False
        except:
            pass
        driver.get(search_tag_instagram)
        time.sleep(5)
        success_post_crawler_num = 0
        first_target = driver.find_element_by_css_selector('div._9AhH0')
        first_target.click()
        while success_post_crawler_num < post_num:
            time.sleep(3)
            try:
                result_set.append(self._get_post(driver.page_source))
                success_post_crawler_num += 1
            except Exception as e:
                print(e)

            driver.find_element_by_css_selector('a._65Bje.coreSpriteRightPaginationArrow').click()
        driver.close()
        return result_set
