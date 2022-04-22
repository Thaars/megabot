from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CloseChat")


@attr.s(auto_attribs=True)
class CloseChat:
    """
    Attributes:
        chat_id (int):
    """

    chat_id: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        chat_id = self.chat_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chatId": chat_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        chat_id = d.pop("chatId")

        close_chat = cls(
            chat_id=chat_id,
        )

        close_chat.additional_properties = d
        return close_chat

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
