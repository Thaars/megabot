import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.chat_category import ChatCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="Chat")


@attr.s(auto_attribs=True)
class Chat:
    """
    Attributes:
        user_id (int):
        timestamp (datetime.datetime):
        category (ChatCategory): Support, TradeDesk
        id (Union[Unset, int]):
        assigned_support_id (Union[Unset, int]): Assigned To
        closed_by_id (Union[Unset, int]): Closed By
        close_timestamp (Union[Unset, datetime.datetime]):
    """

    user_id: int
    timestamp: datetime.datetime
    category: ChatCategory
    id: Union[Unset, int] = UNSET
    assigned_support_id: Union[Unset, int] = UNSET
    closed_by_id: Union[Unset, int] = UNSET
    close_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        timestamp = self.timestamp.isoformat()

        category = self.category.value

        id = self.id
        assigned_support_id = self.assigned_support_id
        closed_by_id = self.closed_by_id
        close_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.close_timestamp, Unset):
            close_timestamp = self.close_timestamp.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "timestamp": timestamp,
                "category": category,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if assigned_support_id is not UNSET:
            field_dict["assignedSupportId"] = assigned_support_id
        if closed_by_id is not UNSET:
            field_dict["closedById"] = closed_by_id
        if close_timestamp is not UNSET:
            field_dict["closeTimestamp"] = close_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("userId")

        timestamp = isoparse(d.pop("timestamp"))

        category = ChatCategory(d.pop("category"))

        id = d.pop("id", UNSET)

        assigned_support_id = d.pop("assignedSupportId", UNSET)

        closed_by_id = d.pop("closedById", UNSET)

        _close_timestamp = d.pop("closeTimestamp", UNSET)
        close_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_close_timestamp, Unset):
            close_timestamp = UNSET
        else:
            close_timestamp = isoparse(_close_timestamp)

        chat = cls(
            user_id=user_id,
            timestamp=timestamp,
            category=category,
            id=id,
            assigned_support_id=assigned_support_id,
            closed_by_id=closed_by_id,
            close_timestamp=close_timestamp,
        )

        chat.additional_properties = d
        return chat

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
