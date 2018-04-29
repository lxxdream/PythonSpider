import requests
from requests.exceptions import ConnectionError
from urllib.parse import urlencode
from pyquery import PyQuery as pq
from Weixin.config import *

base_url = 'http://weixin.sogou.com/weixin?'
proxy = None

headers = {
    'Cookie': 'SUID=011F51DA2208990A0000000056E53116; SUV=1457860887313425; LSTMV=93%2C165; LCLKINT=5969; IPLOC=CN3201; ABTEST=0|1524583521|v1; weixinIndexVisited=1; JSESSIONID=aaa5flRVkUktfeaDiU2lw; sct=10; PHPSESSID=fv9h1dbdbrurk85sqsgsbuqrh4; SUIR=AD375A2111157A89D222E7EA11DFC87E; SNUID=83066912222649D49333953C23DBF663; seccodeRight=success; successCount=1|Sun, 29 Apr 2018 06:22:12 GMT; ppinf=5|1524982652|1526192252|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo0OkphY2t8Y3J0OjEwOjE1MjQ5ODI2NTJ8cmVmbmljazo0OkphY2t8dXNlcmlkOjQ0Om85dDJsdUVfVE5EY0RhaFp2WjV0NVdkaWdmMk1Ad2VpeGluLnNvaHUuY29tfA; pprdig=UbTo8TCN-82bBJGzHPET2wIDxb5rUXNXIK5no99IHmCWFgJXUky5Tt1BbrX4GveQLfHjAH8BsR05WrOK3RTXhYJN93OUmIEose2cXW_LCYkuG7qrxC5kJnZLxA_yTYbwplGWnyuJYDv5eJnKPhsPZ-GSc53krz3GL8xEEJuf52Q; sgid=01-32630541-AVrlY3xdkkAX01j2tw1EZhI; ppmdig=15249826520000000e4915d9aba1a2e4621c4d4c6eb17897',
    'Host': 'weixin.sogou.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None


def get_html(url, count=1):

    print('Request:', url)
    print('Try:', count)

    global proxy

    if count >= MAX_COUNT:
        print('Tried Too Many Counts')
        return None

    try:
        if proxy:
            proxies = {
                'http': 'http://' + proxy
            }
            response = requests.get(url, allow_redirects=False, headers=headers, proxies=proxies)
        else:
            response = requests.get(url, allow_redirects=False, headers=headers)
        #response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:
            print('302')
            proxy = get_proxy()
            if proxy:
                print('Using Proxy', proxy)
                #count += 1
                return get_html(url)
            else:
                print('Get Proxy Failed')
                return None
    except ConnectionError as e:
        print('Error Occurred:', e.args)
        proxy = get_proxy()
        count += 1
        return get_html(url, count)


def get_index(keyword, page):
    data = {
        'query': keyword,
        'type': 2,
        'page': page
    }
    params = urlencode(data)
    url = base_url + params
    html = get_html(url)
    return html


def parse_index(html):
    doc = pq(html)
    items = doc('.news-box .news-list li .text-box h3 a').items()
    for item in items:
        print(item.text())
        yield item.attr('href')


def main():
    for page in range(1, 101):
        html = get_index(KEYWORD, page)
        #print(html)
        if html:
            article_urls = parse_index(html)
            for article_url in article_urls:
                print('article_url:', article_url)


if __name__ == '__main__':
    main()
    #html = requests.get('http://weixin.sogou.com/weixin?query=%E9%A3%8E%E6%99%AF&type=2&page=1', headers=headers).text
    #html = get_index('风景', 1)
    #print(html)
