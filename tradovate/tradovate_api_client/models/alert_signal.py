import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertSignal")


@attr.s(auto_attribs=True)
class AlertSignal:
    """
    Attributes:
        timestamp (datetime.datetime):
        alert_id (int):
        is_read (bool):
        text (str):
        id (Union[Unset, int]):
    """

    timestamp: datetime.datetime
    alert_id: int
    is_read: bool
    text: str
    id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        alert_id = self.alert_id
        is_read = self.is_read
        text = self.text
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "alertId": alert_id,
                "isRead": is_read,
                "text": text,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timestamp = isoparse(d.pop("timestamp"))

        alert_id = d.pop("alertId")

        is_read = d.pop("isRead")

        text = d.pop("text")

        id = d.pop("id", UNSET)

        alert_signal = cls(
            timestamp=timestamp,
            alert_id=alert_id,
            is_read=is_read,
            text=text,
            id=id,
        )

        alert_signal.additional_properties = d
        return alert_signal

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
