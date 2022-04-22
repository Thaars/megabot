import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketDataSubscription")


@attr.s(auto_attribs=True)
class MarketDataSubscription:
    """
    Attributes:
        user_id (int):
        timestamp (datetime.datetime):
        plan_price (float):
        market_data_subscription_plan_id (int):
        year (int):
        month (int):
        id (Union[Unset, int]):
        credit_card_transaction_id (Union[Unset, int]):
        cash_balance_log_id (Union[Unset, int]):
        credit_card_id (Union[Unset, int]):
        account_id (Union[Unset, int]):
        renewal_credit_card_id (Union[Unset, int]):
        renewal_account_id (Union[Unset, int]):
    """

    user_id: int
    timestamp: datetime.datetime
    plan_price: float
    market_data_subscription_plan_id: int
    year: int
    month: int
    id: Union[Unset, int] = UNSET
    credit_card_transaction_id: Union[Unset, int] = UNSET
    cash_balance_log_id: Union[Unset, int] = UNSET
    credit_card_id: Union[Unset, int] = UNSET
    account_id: Union[Unset, int] = UNSET
    renewal_credit_card_id: Union[Unset, int] = UNSET
    renewal_account_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        timestamp = self.timestamp.isoformat()

        plan_price = self.plan_price
        market_data_subscription_plan_id = self.market_data_subscription_plan_id
        year = self.year
        month = self.month
        id = self.id
        credit_card_transaction_id = self.credit_card_transaction_id
        cash_balance_log_id = self.cash_balance_log_id
        credit_card_id = self.credit_card_id
        account_id = self.account_id
        renewal_credit_card_id = self.renewal_credit_card_id
        renewal_account_id = self.renewal_account_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "timestamp": timestamp,
                "planPrice": plan_price,
                "marketDataSubscriptionPlanId": market_data_subscription_plan_id,
                "year": year,
                "month": month,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if credit_card_transaction_id is not UNSET:
            field_dict["creditCardTransactionId"] = credit_card_transaction_id
        if cash_balance_log_id is not UNSET:
            field_dict["cashBalanceLogId"] = cash_balance_log_id
        if credit_card_id is not UNSET:
            field_dict["creditCardId"] = credit_card_id
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if renewal_credit_card_id is not UNSET:
            field_dict["renewalCreditCardId"] = renewal_credit_card_id
        if renewal_account_id is not UNSET:
            field_dict["renewalAccountId"] = renewal_account_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("userId")

        timestamp = isoparse(d.pop("timestamp"))

        plan_price = d.pop("planPrice")

        market_data_subscription_plan_id = d.pop("marketDataSubscriptionPlanId")

        year = d.pop("year")

        month = d.pop("month")

        id = d.pop("id", UNSET)

        credit_card_transaction_id = d.pop("creditCardTransactionId", UNSET)

        cash_balance_log_id = d.pop("cashBalanceLogId", UNSET)

        credit_card_id = d.pop("creditCardId", UNSET)

        account_id = d.pop("accountId", UNSET)

        renewal_credit_card_id = d.pop("renewalCreditCardId", UNSET)

        renewal_account_id = d.pop("renewalAccountId", UNSET)

        market_data_subscription = cls(
            user_id=user_id,
            timestamp=timestamp,
            plan_price=plan_price,
            market_data_subscription_plan_id=market_data_subscription_plan_id,
            year=year,
            month=month,
            id=id,
            credit_card_transaction_id=credit_card_transaction_id,
            cash_balance_log_id=cash_balance_log_id,
            credit_card_id=credit_card_id,
            account_id=account_id,
            renewal_credit_card_id=renewal_credit_card_id,
            renewal_account_id=renewal_account_id,
        )

        market_data_subscription.additional_properties = d
        return market_data_subscription

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
