import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.cash_balance_log_cash_change_type import CashBalanceLogCashChangeType
from ..models.trade_date import TradeDate
from ..types import UNSET, Unset

T = TypeVar("T", bound="CashBalanceLog")


@attr.s(auto_attribs=True)
class CashBalanceLog:
    """
    Attributes:
        account_id (int):
        timestamp (datetime.datetime):
        trade_date (TradeDate):
        currency_id (int):
        amount (float):
        cash_change_type (CashBalanceLogCashChangeType): AutomaticReconciliation, BrokerageFee, CancelledPairedTrade,
            ClearingFee, Commission, DeskFee, EntitlementSubscription, ExchangeFee, FundTransaction, FundTransactionFee,
            IPFee, LiquidationFee, ManualAdjustment, MarketDataSubscription, NewSession, NfaFee, OptionsTrade,
            OrderRoutingFee, TradePaired, TradovateSubscription
        delta (float):
        id (Union[Unset, int]):
        realized_pn_l (Union[Unset, float]):
        week_realized_pn_l (Union[Unset, float]):
        fill_pair_id (Union[Unset, int]):
        fill_id (Union[Unset, int]):
        fund_transaction_id (Union[Unset, int]):
        comment (Union[Unset, str]):
        sender_id (Union[Unset, int]):
    """

    account_id: int
    timestamp: datetime.datetime
    trade_date: TradeDate
    currency_id: int
    amount: float
    cash_change_type: CashBalanceLogCashChangeType
    delta: float
    id: Union[Unset, int] = UNSET
    realized_pn_l: Union[Unset, float] = UNSET
    week_realized_pn_l: Union[Unset, float] = UNSET
    fill_pair_id: Union[Unset, int] = UNSET
    fill_id: Union[Unset, int] = UNSET
    fund_transaction_id: Union[Unset, int] = UNSET
    comment: Union[Unset, str] = UNSET
    sender_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        timestamp = self.timestamp.isoformat()

        trade_date = self.trade_date.to_dict()

        currency_id = self.currency_id
        amount = self.amount
        cash_change_type = self.cash_change_type.value

        delta = self.delta
        id = self.id
        realized_pn_l = self.realized_pn_l
        week_realized_pn_l = self.week_realized_pn_l
        fill_pair_id = self.fill_pair_id
        fill_id = self.fill_id
        fund_transaction_id = self.fund_transaction_id
        comment = self.comment
        sender_id = self.sender_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "timestamp": timestamp,
                "tradeDate": trade_date,
                "currencyId": currency_id,
                "amount": amount,
                "cashChangeType": cash_change_type,
                "delta": delta,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if realized_pn_l is not UNSET:
            field_dict["realizedPnL"] = realized_pn_l
        if week_realized_pn_l is not UNSET:
            field_dict["weekRealizedPnL"] = week_realized_pn_l
        if fill_pair_id is not UNSET:
            field_dict["fillPairId"] = fill_pair_id
        if fill_id is not UNSET:
            field_dict["fillId"] = fill_id
        if fund_transaction_id is not UNSET:
            field_dict["fundTransactionId"] = fund_transaction_id
        if comment is not UNSET:
            field_dict["comment"] = comment
        if sender_id is not UNSET:
            field_dict["senderId"] = sender_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("accountId")

        timestamp = isoparse(d.pop("timestamp"))

        trade_date = TradeDate.from_dict(d.pop("tradeDate"))

        currency_id = d.pop("currencyId")

        amount = d.pop("amount")

        cash_change_type = CashBalanceLogCashChangeType(d.pop("cashChangeType"))

        delta = d.pop("delta")

        id = d.pop("id", UNSET)

        realized_pn_l = d.pop("realizedPnL", UNSET)

        week_realized_pn_l = d.pop("weekRealizedPnL", UNSET)

        fill_pair_id = d.pop("fillPairId", UNSET)

        fill_id = d.pop("fillId", UNSET)

        fund_transaction_id = d.pop("fundTransactionId", UNSET)

        comment = d.pop("comment", UNSET)

        sender_id = d.pop("senderId", UNSET)

        cash_balance_log = cls(
            account_id=account_id,
            timestamp=timestamp,
            trade_date=trade_date,
            currency_id=currency_id,
            amount=amount,
            cash_change_type=cash_change_type,
            delta=delta,
            id=id,
            realized_pn_l=realized_pn_l,
            week_realized_pn_l=week_realized_pn_l,
            fill_pair_id=fill_pair_id,
            fill_id=fill_id,
            fund_transaction_id=fund_transaction_id,
            comment=comment,
            sender_id=sender_id,
        )

        cash_balance_log.additional_properties = d
        return cash_balance_log

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
