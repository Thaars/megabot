from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CancelTradovateSubscription")


@attr.s(auto_attribs=True)
class CancelTradovateSubscription:
    """
    Attributes:
        tradovate_subscription_id (int):
        cancel_reason (Union[Unset, str]):
        expire (Union[Unset, bool]):
    """

    tradovate_subscription_id: int
    cancel_reason: Union[Unset, str] = UNSET
    expire: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tradovate_subscription_id = self.tradovate_subscription_id
        cancel_reason = self.cancel_reason
        expire = self.expire

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tradovateSubscriptionId": tradovate_subscription_id,
            }
        )
        if cancel_reason is not UNSET:
            field_dict["cancelReason"] = cancel_reason
        if expire is not UNSET:
            field_dict["expire"] = expire

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tradovate_subscription_id = d.pop("tradovateSubscriptionId")

        cancel_reason = d.pop("cancelReason", UNSET)

        expire = d.pop("expire", UNSET)

        cancel_tradovate_subscription = cls(
            tradovate_subscription_id=tradovate_subscription_id,
            cancel_reason=cancel_reason,
            expire=expire,
        )

        cancel_tradovate_subscription.additional_properties = d
        return cancel_tradovate_subscription

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
