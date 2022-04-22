import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="CheckReplaySession")


@attr.s(auto_attribs=True)
class CheckReplaySession:
    """
    Attributes:
        start_timestamp (datetime.datetime):
    """

    start_timestamp: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_timestamp = self.start_timestamp.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startTimestamp": start_timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start_timestamp = isoparse(d.pop("startTimestamp"))

        check_replay_session = cls(
            start_timestamp=start_timestamp,
        )

        check_replay_session.additional_properties = d
        return check_replay_session

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
