import os
import json
import requests
from multiprocessing import Pool
from requests.exceptions import RequestException


base_url = 'https://api.yii.dgtle.com/v2/news?token=&perpage=24&typeid=388&page='

def get_page_index(page):
    try:
        print('page:', page)
        url = base_url + str(page)
        response = requests.get(url)
        if response.status_code == 200:
            parse_page(response.text)
            #return response.text
        #return None
    except RequestException:
        print('请求索引页出错！')
        #return None

def parse_page(html):
    try:
        data = json.loads(html)
        # print(data.keys())
        lst = data['list']
        # print(lst)
        for li in lst:
            #print(li['message'], li['subject'], li['cover_name'])
            download_image(li['message'], li['cover_name'])
    except Exception as e:
        print('解析页面出错:', e.args)


def download_image(title, url):
    print('正在下载', title, url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            save_image(title, response.content)
        return None
    except requests.exceptions.RequestException:
        print('请求图片地址出错！')
        return None

def save_image(title, content):
    image_path = os.getcwd() + '/Images'
    if not os.path.exists(image_path):
        os.makedirs(image_path)
    file_path = '{0}/{1}.jpg'.format(image_path, title)
    if not os.path.exists(file_path):
        print('保存：', file_path)
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()


def main():
    for i in range(1, 12):
        get_page_index(i)

    # pool = Pool()
    # pool.map(get_page_index, [i for i in range(1, 12)])



if __name__ == '__main__':
    main()
