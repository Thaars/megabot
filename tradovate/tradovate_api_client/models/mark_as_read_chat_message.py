from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="MarkAsReadChatMessage")


@attr.s(auto_attribs=True)
class MarkAsReadChatMessage:
    """
    Attributes:
        chat_message_id (int):
    """

    chat_message_id: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        chat_message_id = self.chat_message_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chatMessageId": chat_message_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        chat_message_id = d.pop("chatMessageId")

        mark_as_read_chat_message = cls(
            chat_message_id=chat_message_id,
        )

        mark_as_read_chat_message.additional_properties = d
        return mark_as_read_chat_message

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
