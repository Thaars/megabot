from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CancelSecondMarketDataSubscription")


@attr.s(auto_attribs=True)
class CancelSecondMarketDataSubscription:
    """
    Attributes:
        second_market_data_subscription_id (int):
    """

    second_market_data_subscription_id: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        second_market_data_subscription_id = self.second_market_data_subscription_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "secondMarketDataSubscriptionId": second_market_data_subscription_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        second_market_data_subscription_id = d.pop("secondMarketDataSubscriptionId")

        cancel_second_market_data_subscription = cls(
            second_market_data_subscription_id=second_market_data_subscription_id,
        )

        cancel_second_market_data_subscription.additional_properties = d
        return cancel_second_market_data_subscription

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
