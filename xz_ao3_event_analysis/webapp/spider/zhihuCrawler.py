#/!/bin/python
from bs4 import BeautifulSoup as bsoup
import requests
import logging
import codecs
import json

class Config(object):
    headers = {
        'Referer': 'https://zhuanlan.zhihu.com/p/20410446',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }

url = 'https://www.zhihu.com/question/394980583/answers/updated'

class Context:
    last_page = 0
    last_idx = 0
    all_page = 0
    def dump(self):
        obj = {}
        for i in self.attrs:
            obj[key] = val

    def load(self, path=''):
        if not path:
            try:
                with open('abs.path', 'r') as f:
                    json.load()
            except Exception as e:
                logging.info(f"load failed {e}")
        pass


class Tool():
    def __init__(self, url):
        self.url = url

    def get_page_num(self):
        response = requests.get(self.url, verify=False, headers=Config.headers)
        if response.status_code >= 200 and response.status_code < 400:
            soup = bsoup(response.content.decode('utf-8'), 'lxml')
            with codecs.open('data_str.html', 'w', 'utf-8') as f:
                logging.info(f'type = {type(response.text)}')
                f.write(response.text)
            # print(response.text)
            pages = soup.find('div', {'class': '.Pagination'})
            children = pages.findChildren('button', recursive=False)

    def get_contents(self):
        data_params = {"include": "data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B*%5D.topics"}
        offset = 945
        data_params["offset"] = offset
        data_params["limit"] = 15
        data_params["sort_by"] = 'updated'
        data_url = 'https://www.zhihu.com/api/v4/questions/394980583/answers'
        response = requests.get(self.url, verify=False, params=data_params, headers=Config.headers)
        if response.status_code >= 200 and response.status_code < 400:
            logging.info(f'response status_code {response.status_code} {response.text}')
            answers = json.loads(response.text)
            with open(f'response_{offset}.json', 'w') as f:
                json.dump(answers, f, indent=4, ensure_ascii=False)

    def fetch_page(self, page_num):
        response = requests.get(self.url, headers=Config.headers)
        pass

    def run():
        pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='[%(levelname).1s][%(asctime)s %(filename)s line:%(lineno)d]%(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S')
    tool = Tool(url)
    tool.get_contents()
    pass

'''
HTML解析库 —— Request HTML 初体验 https://zhuanlan.zhihu.com/p/43972449

'''