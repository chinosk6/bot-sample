from pydantic import BaseModel
import typing as t

class SenderInfo(BaseModel):
    age: t.Optional[int]
    area: t.Optional[str]
    card: t.Optional[str]
    level: t.Optional[str]
    nickname: t.Optional[str]
    role: t.Optional[str]
    sex: t.Optional[str]
    title: t.Optional[str]
    user_id: t.Optional[int]


class Message(BaseModel):
    post_type: str
    message_type: str
    time: int
    self_id: int
    sub_type: str
    user_id: int
    font: int
    group_id: t.Optional[int]
    message: str
    # message_seq: int
    raw_message: str
    # anonymous: NoneType
    sender: SenderInfo
    message_id: int


# class PrivateMessage(BaseModel):
#     post_type: str
#     message_type: str
#     time: int
#     self_id: int
#     sub_type: str
#     font: int
#     sender: SenderInfo
#     message_id: int
#     user_id: int
#     target_id: int
#     message: str
#     raw_message: str
