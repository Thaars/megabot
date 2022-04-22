from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.chat_message import ChatMessage
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatMessageResponse")


@attr.s(auto_attribs=True)
class ChatMessageResponse:
    """
    Attributes:
        error_text (Union[Unset, str]): Non-empty if the request failed
        chat_message (Union[Unset, ChatMessage]):
    """

    error_text: Union[Unset, str] = UNSET
    chat_message: Union[Unset, ChatMessage] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_text = self.error_text
        chat_message: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.chat_message, Unset):
            chat_message = self.chat_message.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if chat_message is not UNSET:
            field_dict["chatMessage"] = chat_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error_text = d.pop("errorText", UNSET)

        _chat_message = d.pop("chatMessage", UNSET)
        chat_message: Union[Unset, ChatMessage]
        if isinstance(_chat_message, Unset):
            chat_message = UNSET
        else:
            chat_message = ChatMessage.from_dict(_chat_message)

        chat_message_response = cls(
            error_text=error_text,
            chat_message=chat_message,
        )

        chat_message_response.additional_properties = d
        return chat_message_response

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
