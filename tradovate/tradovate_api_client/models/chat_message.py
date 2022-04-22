import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatMessage")


@attr.s(auto_attribs=True)
class ChatMessage:
    """
    Attributes:
        timestamp (datetime.datetime):
        chat_id (int):
        sender_id (int):
        text (str):
        read_status (bool):
        id (Union[Unset, int]):
        sender_name (Union[Unset, str]):
    """

    timestamp: datetime.datetime
    chat_id: int
    sender_id: int
    text: str
    read_status: bool
    id: Union[Unset, int] = UNSET
    sender_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        chat_id = self.chat_id
        sender_id = self.sender_id
        text = self.text
        read_status = self.read_status
        id = self.id
        sender_name = self.sender_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "chatId": chat_id,
                "senderId": sender_id,
                "text": text,
                "readStatus": read_status,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if sender_name is not UNSET:
            field_dict["senderName"] = sender_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timestamp = isoparse(d.pop("timestamp"))

        chat_id = d.pop("chatId")

        sender_id = d.pop("senderId")

        text = d.pop("text")

        read_status = d.pop("readStatus")

        id = d.pop("id", UNSET)

        sender_name = d.pop("senderName", UNSET)

        chat_message = cls(
            timestamp=timestamp,
            chat_id=chat_id,
            sender_id=sender_id,
            text=text,
            read_status=read_status,
            id=id,
            sender_name=sender_name,
        )

        chat_message.additional_properties = d
        return chat_message

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
