import requests
from base_settings import CQhttp
from bot import models
# import urllib.parse

class GeneCQCode:
    @staticmethod
    def image(img_path: str, is_file=False, cache=True):
        return f"[CQ:image,file={'file:///' if is_file else ''}{img_path},cache={str(cache).lower()}]"

def send_private_message(userid: int, msg: str):
    # msg = urllib.parse.quote(msg)
    url = f"http://{CQhttp.ip}:{CQhttp.cq_http_port}/send_private_msg"
    response = requests.request("GET", url, params={"user_id": userid, "message": msg})
    return response.text


def send_group_message(groupid: int, msg: str):
    # msg = urllib.parse.quote(msg)
    url = f"http://{CQhttp.ip}:{CQhttp.cq_http_port}/send_group_msg"
    response = requests.request("GET", url, params={"group_id": groupid, "message": msg})
    return response.text


def reply_message(event: models.Message, msg: str, reply=True):
    if reply:
        msg = f"[CQ:reply,id={event.message_id}] {msg}"

    if event.message_type == "group":
        return send_group_message(event.group_id, msg)

    elif event.message_type == "private":
        return send_private_message(event.user_id, msg)
