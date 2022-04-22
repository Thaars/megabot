import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="InitializeClock")


@attr.s(auto_attribs=True)
class InitializeClock:
    """
    Attributes:
        start_timestamp (datetime.datetime):
        speed (int):
        initial_balance (Union[Unset, float]):
    """

    start_timestamp: datetime.datetime
    speed: int
    initial_balance: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_timestamp = self.start_timestamp.isoformat()

        speed = self.speed
        initial_balance = self.initial_balance

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startTimestamp": start_timestamp,
                "speed": speed,
            }
        )
        if initial_balance is not UNSET:
            field_dict["initialBalance"] = initial_balance

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start_timestamp = isoparse(d.pop("startTimestamp"))

        speed = d.pop("speed")

        initial_balance = d.pop("initialBalance", UNSET)

        initialize_clock = cls(
            start_timestamp=start_timestamp,
            speed=speed,
            initial_balance=initial_balance,
        )

        initialize_clock.additional_properties = d
        return initialize_clock

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
