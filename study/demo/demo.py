import requests


def request( url, num_retries=3):
    from requests.adapters import HTTPAdapter
    try:
        s = requests.Session()
        r = s.get(url, timeout=30)
        r.raise_for_status()  # raise_for_status(),如果不是200会抛出HTTPError错误

        html = r.content
        status_code = r.status_code
        return status_code

    except Exception as e:
        print(num_retries)

        html = None
        if num_retries > 0:
            # 如果不是200就重试，每次递减重试次数
            return request(url, num_retries - 1)

    print("请求失败！！！！！！！！")
    return 500

request('https://www.baidu.com123',)