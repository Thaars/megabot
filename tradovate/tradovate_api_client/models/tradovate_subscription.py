import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.trade_date import TradeDate
from ..types import UNSET, Unset

T = TypeVar("T", bound="TradovateSubscription")


@attr.s(auto_attribs=True)
class TradovateSubscription:
    """
    Attributes:
        user_id (int):
        timestamp (datetime.datetime):
        plan_price (float):
        tradovate_subscription_plan_id (int):
        start_date (TradeDate):
        expiration_date (TradeDate):
        paid_amount (float):
        id (Union[Unset, int]):
        credit_card_transaction_id (Union[Unset, int]):
        cash_balance_log_id (Union[Unset, int]):
        credit_card_id (Union[Unset, int]):
        account_id (Union[Unset, int]):
        cancelled_renewal (Union[Unset, bool]):
        cancel_reason (Union[Unset, str]):
    """

    user_id: int
    timestamp: datetime.datetime
    plan_price: float
    tradovate_subscription_plan_id: int
    start_date: TradeDate
    expiration_date: TradeDate
    paid_amount: float
    id: Union[Unset, int] = UNSET
    credit_card_transaction_id: Union[Unset, int] = UNSET
    cash_balance_log_id: Union[Unset, int] = UNSET
    credit_card_id: Union[Unset, int] = UNSET
    account_id: Union[Unset, int] = UNSET
    cancelled_renewal: Union[Unset, bool] = UNSET
    cancel_reason: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        timestamp = self.timestamp.isoformat()

        plan_price = self.plan_price
        tradovate_subscription_plan_id = self.tradovate_subscription_plan_id
        start_date = self.start_date.to_dict()

        expiration_date = self.expiration_date.to_dict()

        paid_amount = self.paid_amount
        id = self.id
        credit_card_transaction_id = self.credit_card_transaction_id
        cash_balance_log_id = self.cash_balance_log_id
        credit_card_id = self.credit_card_id
        account_id = self.account_id
        cancelled_renewal = self.cancelled_renewal
        cancel_reason = self.cancel_reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "timestamp": timestamp,
                "planPrice": plan_price,
                "tradovateSubscriptionPlanId": tradovate_subscription_plan_id,
                "startDate": start_date,
                "expirationDate": expiration_date,
                "paidAmount": paid_amount,
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
        if cancelled_renewal is not UNSET:
            field_dict["cancelledRenewal"] = cancelled_renewal
        if cancel_reason is not UNSET:
            field_dict["cancelReason"] = cancel_reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("userId")

        timestamp = isoparse(d.pop("timestamp"))

        plan_price = d.pop("planPrice")

        tradovate_subscription_plan_id = d.pop("tradovateSubscriptionPlanId")

        start_date = TradeDate.from_dict(d.pop("startDate"))

        expiration_date = TradeDate.from_dict(d.pop("expirationDate"))

        paid_amount = d.pop("paidAmount")

        id = d.pop("id", UNSET)

        credit_card_transaction_id = d.pop("creditCardTransactionId", UNSET)

        cash_balance_log_id = d.pop("cashBalanceLogId", UNSET)

        credit_card_id = d.pop("creditCardId", UNSET)

        account_id = d.pop("accountId", UNSET)

        cancelled_renewal = d.pop("cancelledRenewal", UNSET)

        cancel_reason = d.pop("cancelReason", UNSET)

        tradovate_subscription = cls(
            user_id=user_id,
            timestamp=timestamp,
            plan_price=plan_price,
            tradovate_subscription_plan_id=tradovate_subscription_plan_id,
            start_date=start_date,
            expiration_date=expiration_date,
            paid_amount=paid_amount,
            id=id,
            credit_card_transaction_id=credit_card_transaction_id,
            cash_balance_log_id=cash_balance_log_id,
            credit_card_id=credit_card_id,
            account_id=account_id,
            cancelled_renewal=cancelled_renewal,
            cancel_reason=cancel_reason,
        )

        tradovate_subscription.additional_properties = d
        return tradovate_subscription

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
