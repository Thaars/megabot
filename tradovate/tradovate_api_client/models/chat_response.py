from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.chat import Chat
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatResponse")


@attr.s(auto_attribs=True)
class ChatResponse:
    """
    Attributes:
        error_text (Union[Unset, str]): Non-empty if the request failed
        chat (Union[Unset, Chat]):
    """

    error_text: Union[Unset, str] = UNSET
    chat: Union[Unset, Chat] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_text = self.error_text
        chat: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.chat, Unset):
            chat = self.chat.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if chat is not UNSET:
            field_dict["chat"] = chat

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error_text = d.pop("errorText", UNSET)

        _chat = d.pop("chat", UNSET)
        chat: Union[Unset, Chat]
        if isinstance(_chat, Unset):
            chat = UNSET
        else:
            chat = Chat.from_dict(_chat)

        chat_response = cls(
            error_text=error_text,
            chat=chat,
        )

        chat_response.additional_properties = d
        return chat_response

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
