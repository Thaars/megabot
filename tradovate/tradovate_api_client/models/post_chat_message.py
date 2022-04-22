from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.post_chat_message_category import PostChatMessageCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostChatMessage")


@attr.s(auto_attribs=True)
class PostChatMessage:
    """
    Attributes:
        category (PostChatMessageCategory): Support, TradeDesk
        text (str):
        user_id (Union[Unset, int]):
    """

    category: PostChatMessageCategory
    text: str
    user_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category = self.category.value

        text = self.text
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "text": text,
            }
        )
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        category = PostChatMessageCategory(d.pop("category"))

        text = d.pop("text")

        user_id = d.pop("userId", UNSET)

        post_chat_message = cls(
            category=category,
            text=text,
            user_id=user_id,
        )

        post_chat_message.additional_properties = d
        return post_chat_message

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
