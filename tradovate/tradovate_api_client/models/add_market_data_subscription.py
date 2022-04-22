from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddMarketDataSubscription")


@attr.s(auto_attribs=True)
class AddMarketDataSubscription:
    """
    Attributes:
        market_data_subscription_plan_ids (List[int]):
        year (int):
        month (int):
        credit_card_id (Union[Unset, int]):
        account_id (Union[Unset, int]):
        user_id (Union[Unset, int]):
    """

    market_data_subscription_plan_ids: List[int]
    year: int
    month: int
    credit_card_id: Union[Unset, int] = UNSET
    account_id: Union[Unset, int] = UNSET
    user_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        market_data_subscription_plan_ids = self.market_data_subscription_plan_ids

        year = self.year
        month = self.month
        credit_card_id = self.credit_card_id
        account_id = self.account_id
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketDataSubscriptionPlanIds": market_data_subscription_plan_ids,
                "year": year,
                "month": month,
            }
        )
        if credit_card_id is not UNSET:
            field_dict["creditCardId"] = credit_card_id
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        market_data_subscription_plan_ids = cast(List[int], d.pop("marketDataSubscriptionPlanIds"))

        year = d.pop("year")

        month = d.pop("month")

        credit_card_id = d.pop("creditCardId", UNSET)

        account_id = d.pop("accountId", UNSET)

        user_id = d.pop("userId", UNSET)

        add_market_data_subscription = cls(
            market_data_subscription_plan_ids=market_data_subscription_plan_ids,
            year=year,
            month=month,
            credit_card_id=credit_card_id,
            account_id=account_id,
            user_id=user_id,
        )

        add_market_data_subscription.additional_properties = d
        return add_market_data_subscription

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
