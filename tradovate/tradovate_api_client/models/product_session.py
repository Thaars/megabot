from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.trade_time import TradeTime
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductSession")


@attr.s(auto_attribs=True)
class ProductSession:
    """
    Attributes:
        open_time (TradeTime):
        start_time (TradeTime):
        stop_time (TradeTime):
        close_time (TradeTime):
        id (Union[Unset, int]):
        sunday_open_time (Union[Unset, TradeTime]):
    """

    open_time: TradeTime
    start_time: TradeTime
    stop_time: TradeTime
    close_time: TradeTime
    id: Union[Unset, int] = UNSET
    sunday_open_time: Union[Unset, TradeTime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        open_time = self.open_time.to_dict()

        start_time = self.start_time.to_dict()

        stop_time = self.stop_time.to_dict()

        close_time = self.close_time.to_dict()

        id = self.id
        sunday_open_time: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sunday_open_time, Unset):
            sunday_open_time = self.sunday_open_time.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "openTime": open_time,
                "startTime": start_time,
                "stopTime": stop_time,
                "closeTime": close_time,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if sunday_open_time is not UNSET:
            field_dict["sundayOpenTime"] = sunday_open_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        open_time = TradeTime.from_dict(d.pop("openTime"))

        start_time = TradeTime.from_dict(d.pop("startTime"))

        stop_time = TradeTime.from_dict(d.pop("stopTime"))

        close_time = TradeTime.from_dict(d.pop("closeTime"))

        id = d.pop("id", UNSET)

        _sunday_open_time = d.pop("sundayOpenTime", UNSET)
        sunday_open_time: Union[Unset, TradeTime]
        if isinstance(_sunday_open_time, Unset):
            sunday_open_time = UNSET
        else:
            sunday_open_time = TradeTime.from_dict(_sunday_open_time)

        product_session = cls(
            open_time=open_time,
            start_time=start_time,
            stop_time=stop_time,
            close_time=close_time,
            id=id,
            sunday_open_time=sunday_open_time,
        )

        product_session.additional_properties = d
        return product_session

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
