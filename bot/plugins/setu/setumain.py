from ...message_handler import EventRegist
from ... import models
from . import setu_api
import bot_api
import json


@EventRegist.reg_privatemsg
@EventRegist.reg_groupmsg
def on_message(event: models.Message):
    if event.message.startswith("来张") and event.message.endswith("色图"):
        try:
            print(f"{event.user_id} 请求色图: {event.message}")
            send = get_setu(event.message)
            bot_api.reply_message(event, send)
        except BaseException as e:
            bot_api.reply_message(event, f"获取失败: {e}")


def get_setu(msg: str):
    tags = msg[2:-2].split(" ")
    tags.remove("") if "" in tags else ...
    if "r18" in tags:
        r18 = 1
        tags.remove("r18")
    else:
        r18 = 0

    data = json.loads(setu_api.lolicon(r18, tags))
    try:
        img_url = data["data"][0]["urls"]["original"]
        img_path = setu_api.download_image(img_url)
        return f"[随机图片]\n{bot_api.GeneCQCode.image(img_path, is_file=True)}"
    except:
        if "error" in data and data["error"] != "":
            return f"获取失败: {data['error']}"
        else:
            return "获取失败"
