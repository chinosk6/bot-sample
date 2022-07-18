import json

with open("config.json", "r", encoding="utf8") as f:
    config = json.load(f)

class CQhttp:
    ip = config["cq"]["ip"]
    cq_ws_port = config["cq"]["cq_ws_port"]  # gocq 正向ws端口
    cq_http_port = config["cq"]["cq_http_port"]  # gocq HTTP端口


lolicon_pixiv_proxy = config["lolicon_pixiv_proxy"]  # lolicon api的反代地址
setu_proxy_url = config["setu_proxy_url"]  # 图片获取/下载代理, 例: http://127.0.0.1:10087, 没有请留空
