# bot-sample
- 此处提供了**最基础的**基于[go-cqhttp](https://github.com/Mrs4s/go-cqhttp)的sdk + 插件示例
- 由于是基础示例, sdk部分仅使用了多线程, 没有使用异步。



# 使用方法

- 安装Python 3, 建议安装`3.8`及以上的版本
- 安装`requirements.txt`中的依赖

```shell
pip install -r requirements.txt
```

- 下载gocq, 像分布式客户端那样设置好`正向ws`端口和`HTTP`端口
- 打开`base_settings.py`, 填入您的设置

```python
class CQhttp:
    ip = "127.0.0.1"
    cq_ws_port = 11415  # gocq 正向ws端口
    cq_http_port = 1988  # gocq HTTP端口


lolicon_pixiv_proxy = "i.pixiv.re"  # lolicon api的反代地址
setu_proxy_url = ""  # 图片获取/下载代理, 例: http://127.0.0.1:10087, 没有请留空
```

- 运行`run.py`即可

```shell
python run.py
```



# 插件部分

## 1. 涩图插件

- 基于lolicon api
- 指令: `来张xx色图`
  - `xx`部分为tag, 可不填。若需要填写多个tag, 请使用空格分割
  - 指令例: `来张色图`, `来张r18色图`, `来张白丝色图`, `来张萝莉 白丝色图`
