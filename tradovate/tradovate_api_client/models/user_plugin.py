import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.trade_date import TradeDate
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserPlugin")


@attr.s(auto_attribs=True)
class UserPlugin:
    """
    Attributes:
        user_id (int):
        timestamp (datetime.datetime):
        plan_price (float):
        plugin_name (str):
        approval (bool):
        start_date (TradeDate):
        paid_amount (float):
        id (Union[Unset, int]):
        credit_card_transaction_id (Union[Unset, int]):
        cash_balance_log_id (Union[Unset, int]):
        credit_card_id (Union[Unset, int]):
        account_id (Union[Unset, int]):
        entitlement_id (Union[Unset, int]):
        expiration_date (Union[Unset, TradeDate]):
        autorenewal (Union[Unset, bool]):
        plan_categories (Union[Unset, str]):
    """

    user_id: int
    timestamp: datetime.datetime
    plan_price: float
    plugin_name: str
    approval: bool
    start_date: TradeDate
    paid_amount: float
    id: Union[Unset, int] = UNSET
    credit_card_transaction_id: Union[Unset, int] = UNSET
    cash_balance_log_id: Union[Unset, int] = UNSET
    credit_card_id: Union[Unset, int] = UNSET
    account_id: Union[Unset, int] = UNSET
    entitlement_id: Union[Unset, int] = UNSET
    expiration_date: Union[Unset, TradeDate] = UNSET
    autorenewal: Union[Unset, bool] = UNSET
    plan_categories: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        timestamp = self.timestamp.isoformat()

        plan_price = self.plan_price
        plugin_name = self.plugin_name
        approval = self.approval
        start_date = self.start_date.to_dict()

        paid_amount = self.paid_amount
        id = self.id
        credit_card_transaction_id = self.credit_card_transaction_id
        cash_balance_log_id = self.cash_balance_log_id
        credit_card_id = self.credit_card_id
        account_id = self.account_id
        entitlement_id = self.entitlement_id
        expiration_date: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.to_dict()

        autorenewal = self.autorenewal
        plan_categories = self.plan_categories

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "timestamp": timestamp,
                "planPrice": plan_price,
                "pluginName": plugin_name,
                "approval": approval,
                "startDate": start_date,
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
        if entitlement_id is not UNSET:
            field_dict["entitlementId"] = entitlement_id
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if autorenewal is not UNSET:
            field_dict["autorenewal"] = autorenewal
        if plan_categories is not UNSET:
            field_dict["planCategories"] = plan_categories

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("userId")

        timestamp = isoparse(d.pop("timestamp"))

        plan_price = d.pop("planPrice")

        plugin_name = d.pop("pluginName")

        approval = d.pop("approval")

        start_date = TradeDate.from_dict(d.pop("startDate"))

        paid_amount = d.pop("paidAmount")

        id = d.pop("id", UNSET)

        credit_card_transaction_id = d.pop("creditCardTransactionId", UNSET)

        cash_balance_log_id = d.pop("cashBalanceLogId", UNSET)

        credit_card_id = d.pop("creditCardId", UNSET)

        account_id = d.pop("accountId", UNSET)

        entitlement_id = d.pop("entitlementId", UNSET)

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: Union[Unset, TradeDate]
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = TradeDate.from_dict(_expiration_date)

        autorenewal = d.pop("autorenewal", UNSET)

        plan_categories = d.pop("planCategories", UNSET)

        user_plugin = cls(
            user_id=user_id,
            timestamp=timestamp,
            plan_price=plan_price,
            plugin_name=plugin_name,
            approval=approval,
            start_date=start_date,
            paid_amount=paid_amount,
            id=id,
            credit_card_transaction_id=credit_card_transaction_id,
            cash_balance_log_id=cash_balance_log_id,
            credit_card_id=credit_card_id,
            account_id=account_id,
            entitlement_id=entitlement_id,
            expiration_date=expiration_date,
            autorenewal=autorenewal,
            plan_categories=plan_categories,
        )

        user_plugin.additional_properties = d
        return user_plugin

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
