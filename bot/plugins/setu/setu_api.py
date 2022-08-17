import os
import requests
import json
from base_settings import setu_proxy_url, lolicon_pixiv_proxy
import random
import string


def generate_randstring(num=8):
    value = ''.join(random.sample(string.ascii_letters + string.digits, num))
    return value

def lolicon(r18=0, tags=None):
    url = "https://api.lolicon.app/setu/v2"
    data = {
        "r18": r18,
        "size": ["original"],
        "proxy": lolicon_pixiv_proxy
    }
    if tags:
        data["tag"] = [i.strip() for i in tags]
    proxies = {'http': setu_proxy_url, 'https': setu_proxy_url} if setu_proxy_url else None
    response = requests.request("POST", url, headers={'Content-Type': 'application/json'}, data=json.dumps(data),
                                timeout=30, proxies=proxies)
    # print(data["tag"], response.text)
    return response.text


def download_image(url: str):
    proxies = {'http': setu_proxy_url, 'https': setu_proxy_url} if setu_proxy_url else None
    response = requests.request("GET", url, timeout=60, proxies=proxies)
    save_name = f"{generate_randstring(12)}.png"
    if not os.path.isdir("./temp"):
        os.makedirs("./temp")
    with open(f"./temp/{save_name}", "wb") as f:
        f.write(response.content)
    return os.path.normpath(os.path.abspath(f"./temp/{save_name}")).replace("\\", "/")
