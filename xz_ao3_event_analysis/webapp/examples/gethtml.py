import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        return f"异常{e}"


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    print(getHTMLText(url))
