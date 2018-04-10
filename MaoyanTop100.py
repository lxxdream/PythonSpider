import requests
import requests.exceptions
import re
import json
import multiprocessing

def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        }
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            return response.text
        return None
    except requests.exceptions.RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?(\d+)</i>' #排名
                         + '.*?data-src="(.*?)"' #图片链接
                         + '.*?name"><a.*?>(.*?)</a>' #电影名称
                         + '.*?star">(.*?)</p>' #主演
                         + '.*?releasetime">(.*?)</p>' #上映时间
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>' #评分
                         , re.S)
    items = re.findall(pattern, html)
    # print(items)
    for item in items:
        yield{
            'rank':  item[0].strip(),
            'image': item[1].strip(),
            'name':  item[2].strip(),
            'actor': item[3].strip(),
            'time':  item[4].strip(),
            'score': item[5] + item[6]
        }

def write_to_file(content):
    with open('MaoyanTop100.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    # print(html)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pool.map(main, [i*10 for i in range(10)])
