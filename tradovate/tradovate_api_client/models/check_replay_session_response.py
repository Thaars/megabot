import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.check_replay_session_response_check_status import CheckReplaySessionResponseCheckStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckReplaySessionResponse")


@attr.s(auto_attribs=True)
class CheckReplaySessionResponse:
    """
    Attributes:
        check_status (CheckReplaySessionResponseCheckStatus): Ineligible, OK, StartTimestampAdjusted
        start_timestamp (Union[Unset, datetime.datetime]):
    """

    check_status: CheckReplaySessionResponseCheckStatus
    start_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        check_status = self.check_status.value

        start_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.start_timestamp, Unset):
            start_timestamp = self.start_timestamp.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "checkStatus": check_status,
            }
        )
        if start_timestamp is not UNSET:
            field_dict["startTimestamp"] = start_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        check_status = CheckReplaySessionResponseCheckStatus(d.pop("checkStatus"))

        _start_timestamp = d.pop("startTimestamp", UNSET)
        start_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_start_timestamp, Unset):
            start_timestamp = UNSET
        else:
            start_timestamp = isoparse(_start_timestamp)

        check_replay_session_response = cls(
            check_status=check_status,
            start_timestamp=start_timestamp,
        )

        check_replay_session_response.additional_properties = d
        return check_replay_session_response

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
