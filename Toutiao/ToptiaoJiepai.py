import json
import urllib
import pymongo
import os
import re
import requests
import requests.exceptions
from bs4 import BeautifulSoup
from hashlib import md5
from multiprocessing import Pool
from Toutiao.ToutiaoConfig import *

client = pymongo.MongoClient(MONGO_URL, connect=False)
db = client[MONGO_DB]

def get_page_index(offset, keyword):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'cur_tab': 3,
        'from': 'gallery'
    }
    url = 'https://www.toutiao.com/search_content/?' + urllib.parse.urlencode(data)
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        }
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            return response.text
        return None
    except requests.exceptions.RequestException:
        print('请求索引页出错！')
        return None

def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')

def get_page_detail(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        }
        response = requests.get(url, headers = headers)
        response.encoding='utf-8'
        if response.status_code == 200:
            return response.text
        return None
    except requests.exceptions.RequestException:
        print('请求详情页出错！')
        return None

def parse_page_detail(html, url):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')
    if title:
        #print(title[0].get_text().strip())
        title = title[0].get_text().strip()
    #print(soup.head.title.text.strip())
    data_pattern = re.compile('BASE_DATA.galleryInfo = (.*?)</script>', re.S)
    result = re.findall(data_pattern, html)
    if result:
        #print(result[0])
        base_data = result[0]
        images_pattern = re.compile('.*?gallery: JSON.parse(.*?)siblingList', re.S)
        result = re.findall(images_pattern, base_data)
        if result:
            # print(result)
            data = result[0][2:-8]
            data = data.replace('\\\"', '"')
            # print(data)
            data = json.loads(data)
            if data and 'sub_images' in data.keys():
                #print(data.get('sub_images'))
                sum_images = data.get('sub_images')
                images = [item.get('url').replace('\\', '') for item in sum_images]
                # for image in images:
                #     download_image(title, image)
                return {
                    'url': url,
                    'title': title,
                    'images': images
                }



def parse_base_data(base_data):
    #print(base_data)
    images_pattern = re.compile('.*?gallery: JSON.parse(.*?)siblingList', re.S)
    result = re.findall(images_pattern, base_data)
    if result:
        #print(result)
        data = result[0][2:-8]
        data = data.replace('\\\"', '"')
        #print(data)
        data = json.loads(data)
        if data and 'sub_images' in data.keys():
            #print(data.get('sub_images'))
            sum_images = data.get('sub_images')

def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print('存储到MongoDB成功', result)
    else:
        print('存储到MongoDB失败', result)

def download_image(title, url):
    print('正在下载', title, url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            save_image(title, response.content)
        return None
    except requests.exceptions.RequestException:
        print('请求详情页出错！')
        return None

def save_image(title, content):
    image_path = os.getcwd() + '/Toutiao/Images/' + title
    if not os.path.exists(image_path):
        os.makedirs(image_path)
    file_path = '{0}/{1}.{2}'.format(image_path, md5(content).hexdigest(), 'jpg')
    print(file_path)
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()

def main(offset):
    html = get_page_index(offset, KEYWORD)
    #print(html)
    for url in parse_page_index(html):
        print(url)
        html = get_page_detail(url)
        if html:
            #print(html)
            result = parse_page_detail(html, url)
            if result: save_to_mongo(result)
            print('---------------------------------------------')


if __name__ == '__main__':
    #main(0)
    groups = [x*20 for x in range(GROUP_START, GROUP_END+1)]
    #print(groups)
    pool = Pool()
    pool.map(main, groups)