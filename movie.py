# coding = utf-8
import requests
from requests.exceptions import RequestException
import re
import json
from multiprocessing import Pool


def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    # 正则匹配
    pattern = re.compile('<li>.*?<em.*?>(\d+)</em>.*?src="(.*?)".*?title">(.*?)</span>.*?v:average">(.*?)</span>.*?inq">(.*?)</span>.*?</li>', re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'score': item[3],
            'inq': item[4]
        }


def write_to_file(content):
    with open('movie.txt', 'a', encoding='utf-8') as f:
        jsondumps=json.dumps(content,ensure_ascii=False)
        f.write(jsondumps+'\n')
    f.close()


def main(start):
    url = 'https://movie.douban.com/top250?start='+str(start)+'&filter='
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i * 25 for i in range(10)])


