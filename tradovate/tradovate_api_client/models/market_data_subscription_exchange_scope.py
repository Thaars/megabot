from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketDataSubscriptionExchangeScope")


@attr.s(auto_attribs=True)
class MarketDataSubscriptionExchangeScope:
    """
    Attributes:
        name (str):
        id (Union[Unset, int]):
        bundle_of (Union[Unset, str]):
    """

    name: str
    id: Union[Unset, int] = UNSET
    bundle_of: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        bundle_of = self.bundle_of

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if bundle_of is not UNSET:
            field_dict["bundleOf"] = bundle_of

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id", UNSET)

        bundle_of = d.pop("bundleOf", UNSET)

        market_data_subscription_exchange_scope = cls(
            name=name,
            id=id,
            bundle_of=bundle_of,
        )

        market_data_subscription_exchange_scope.additional_properties = d
        return market_data_subscription_exchange_scope

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
