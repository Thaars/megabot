from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSecondMarketDataSubscriptionCost")


@attr.s(auto_attribs=True)
class GetSecondMarketDataSubscriptionCost:
    """
    Attributes:
        year (int):
        month (int):
        user_id (Union[Unset, int]):
    """

    year: int
    month: int
    user_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        year = self.year
        month = self.month
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "year": year,
                "month": month,
            }
        )
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        year = d.pop("year")

        month = d.pop("month")

        user_id = d.pop("userId", UNSET)

        get_second_market_data_subscription_cost = cls(
            year=year,
            month=month,
            user_id=user_id,
        )

        get_second_market_data_subscription_cost.additional_properties = d
        return get_second_market_data_subscription_cost

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
