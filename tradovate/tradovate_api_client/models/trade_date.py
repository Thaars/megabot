from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="TradeDate")


@attr.s(auto_attribs=True)
class TradeDate:
    """
    Attributes:
        year (int):
        month (int):
        day (int):
    """

    year: int
    month: int
    day: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        year = self.year
        month = self.month
        day = self.day

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "year": year,
                "month": month,
                "day": day,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        year = d.pop("year")

        month = d.pop("month")

        day = d.pop("day")

        trade_date = cls(
            year=year,
            month=month,
            day=day,
        )

        trade_date.additional_properties = d
        return trade_date

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
