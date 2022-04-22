from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SecondMarketDataSubscriptionCostResponse")


@attr.s(auto_attribs=True)
class SecondMarketDataSubscriptionCostResponse:
    """
    Attributes:
        error_text (Union[Unset, str]): Non-empty if the request failed
        monthly_cost (Union[Unset, float]):
    """

    error_text: Union[Unset, str] = UNSET
    monthly_cost: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_text = self.error_text
        monthly_cost = self.monthly_cost

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if monthly_cost is not UNSET:
            field_dict["monthlyCost"] = monthly_cost

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error_text = d.pop("errorText", UNSET)

        monthly_cost = d.pop("monthlyCost", UNSET)

        second_market_data_subscription_cost_response = cls(
            error_text=error_text,
            monthly_cost=monthly_cost,
        )

        second_market_data_subscription_cost_response.additional_properties = d
        return second_market_data_subscription_cost_response

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
