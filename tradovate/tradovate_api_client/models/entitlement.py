from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.entitlement_duration_units import EntitlementDurationUnits
from ..models.trade_date import TradeDate
from ..types import UNSET, Unset

T = TypeVar("T", bound="Entitlement")


@attr.s(auto_attribs=True)
class Entitlement:
    """
    Attributes:
        title (str):
        price (float):
        name (str):
        id (Union[Unset, int]):
        start_date (Union[Unset, TradeDate]):
        discontinued_date (Union[Unset, TradeDate]):
        duration (Union[Unset, int]):
        duration_units (Union[Unset, EntitlementDurationUnits]): Month, Quarter, Week, Year
        autorenewal (Union[Unset, bool]):
    """

    title: str
    price: float
    name: str
    id: Union[Unset, int] = UNSET
    start_date: Union[Unset, TradeDate] = UNSET
    discontinued_date: Union[Unset, TradeDate] = UNSET
    duration: Union[Unset, int] = UNSET
    duration_units: Union[Unset, EntitlementDurationUnits] = UNSET
    autorenewal: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        price = self.price
        name = self.name
        id = self.id
        start_date: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.to_dict()

        discontinued_date: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.discontinued_date, Unset):
            discontinued_date = self.discontinued_date.to_dict()

        duration = self.duration
        duration_units: Union[Unset, str] = UNSET
        if not isinstance(self.duration_units, Unset):
            duration_units = self.duration_units.value

        autorenewal = self.autorenewal

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "price": price,
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if discontinued_date is not UNSET:
            field_dict["discontinuedDate"] = discontinued_date
        if duration is not UNSET:
            field_dict["duration"] = duration
        if duration_units is not UNSET:
            field_dict["durationUnits"] = duration_units
        if autorenewal is not UNSET:
            field_dict["autorenewal"] = autorenewal

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        price = d.pop("price")

        name = d.pop("name")

        id = d.pop("id", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, TradeDate]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = TradeDate.from_dict(_start_date)

        _discontinued_date = d.pop("discontinuedDate", UNSET)
        discontinued_date: Union[Unset, TradeDate]
        if isinstance(_discontinued_date, Unset):
            discontinued_date = UNSET
        else:
            discontinued_date = TradeDate.from_dict(_discontinued_date)

        duration = d.pop("duration", UNSET)

        _duration_units = d.pop("durationUnits", UNSET)
        duration_units: Union[Unset, EntitlementDurationUnits]
        if isinstance(_duration_units, Unset):
            duration_units = UNSET
        else:
            duration_units = EntitlementDurationUnits(_duration_units)

        autorenewal = d.pop("autorenewal", UNSET)

        entitlement = cls(
            title=title,
            price=price,
            name=name,
            id=id,
            start_date=start_date,
            discontinued_date=discontinued_date,
            duration=duration,
            duration_units=duration_units,
            autorenewal=autorenewal,
        )

        entitlement.additional_properties = d
        return entitlement

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
