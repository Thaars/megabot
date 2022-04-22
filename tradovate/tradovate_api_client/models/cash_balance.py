import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.trade_date import TradeDate
from ..types import UNSET, Unset

T = TypeVar("T", bound="CashBalance")


@attr.s(auto_attribs=True)
class CashBalance:
    """
    Attributes:
        account_id (int):
        timestamp (datetime.datetime):
        trade_date (TradeDate):
        currency_id (int):
        amount (float):
        id (Union[Unset, int]):
        realized_pn_l (Union[Unset, float]):
        week_realized_pn_l (Union[Unset, float]):
    """

    account_id: int
    timestamp: datetime.datetime
    trade_date: TradeDate
    currency_id: int
    amount: float
    id: Union[Unset, int] = UNSET
    realized_pn_l: Union[Unset, float] = UNSET
    week_realized_pn_l: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        timestamp = self.timestamp.isoformat()

        trade_date = self.trade_date.to_dict()

        currency_id = self.currency_id
        amount = self.amount
        id = self.id
        realized_pn_l = self.realized_pn_l
        week_realized_pn_l = self.week_realized_pn_l

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "timestamp": timestamp,
                "tradeDate": trade_date,
                "currencyId": currency_id,
                "amount": amount,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if realized_pn_l is not UNSET:
            field_dict["realizedPnL"] = realized_pn_l
        if week_realized_pn_l is not UNSET:
            field_dict["weekRealizedPnL"] = week_realized_pn_l

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("accountId")

        timestamp = isoparse(d.pop("timestamp"))

        trade_date = TradeDate.from_dict(d.pop("tradeDate"))

        currency_id = d.pop("currencyId")

        amount = d.pop("amount")

        id = d.pop("id", UNSET)

        realized_pn_l = d.pop("realizedPnL", UNSET)

        week_realized_pn_l = d.pop("weekRealizedPnL", UNSET)

        cash_balance = cls(
            account_id=account_id,
            timestamp=timestamp,
            trade_date=trade_date,
            currency_id=currency_id,
            amount=amount,
            id=id,
            realized_pn_l=realized_pn_l,
            week_realized_pn_l=week_realized_pn_l,
        )

        cash_balance.additional_properties = d
        return cash_balance

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
