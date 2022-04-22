import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.execution_report_action import ExecutionReportAction
from ..models.execution_report_exec_type import ExecutionReportExecType
from ..models.execution_report_ord_status import ExecutionReportOrdStatus
from ..models.execution_report_reject_reason import ExecutionReportRejectReason
from ..models.trade_date import TradeDate
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionReport")


@attr.s(auto_attribs=True)
class ExecutionReport:
    """
    Attributes:
        command_id (int):
        name (str):
        account_id (int):
        contract_id (int):
        timestamp (datetime.datetime):
        order_id (int):
        exec_type (ExecutionReportExecType): Canceled, Completed, DoneForDay, Expired, New, OrderStatus, PendingCancel,
            PendingNew, PendingReplace, Rejected, Replaced, Stopped, Suspended, Trade, TradeCancel, TradeCorrect
        action (ExecutionReportAction): Buy, Sell
        id (Union[Unset, int]):
        trade_date (Union[Unset, TradeDate]):
        exec_ref_id (Union[Unset, str]):
        ord_status (Union[Unset, ExecutionReportOrdStatus]): Canceled, Completed, Expired, Filled, PendingCancel,
            PendingNew, PendingReplace, Rejected, Suspended, Unknown, Working
        cum_qty (Union[Unset, int]):
        avg_px (Union[Unset, float]):
        last_qty (Union[Unset, int]):
        last_px (Union[Unset, float]):
        reject_reason (Union[Unset, ExecutionReportRejectReason]): AccountClosed, AdvancedTrailingStopUnsupported,
            AnotherCommandPending, BackMonthProhibited, ExecutionProviderNotConfigured, ExecutionProviderUnavailable,
            InvalidContract, InvalidPrice, LiquidationOnly, LiquidationOnlyBeforeExpiration, MaxOrderQtyIsNotSpecified,
            MaxOrderQtyLimitReached, MaxPosLimitMisconfigured, MaxPosLimitReached, MaxTotalPosLimitReached,
            MultipleAccountPlanRequired, NoQuote, NotEnoughLiquidity, OtherExecutionRelated, ParentRejected,
            RiskCheckTimeout, SessionClosed, Success, TooLate, TradingLocked, TrailingStopNonOrderQtyModify, Unauthorized,
            UnknownReason, Unsupported
        text (Union[Unset, str]):
        exchange_order_id (Union[Unset, str]):
    """

    command_id: int
    name: str
    account_id: int
    contract_id: int
    timestamp: datetime.datetime
    order_id: int
    exec_type: ExecutionReportExecType
    action: ExecutionReportAction
    id: Union[Unset, int] = UNSET
    trade_date: Union[Unset, TradeDate] = UNSET
    exec_ref_id: Union[Unset, str] = UNSET
    ord_status: Union[Unset, ExecutionReportOrdStatus] = UNSET
    cum_qty: Union[Unset, int] = UNSET
    avg_px: Union[Unset, float] = UNSET
    last_qty: Union[Unset, int] = UNSET
    last_px: Union[Unset, float] = UNSET
    reject_reason: Union[Unset, ExecutionReportRejectReason] = UNSET
    text: Union[Unset, str] = UNSET
    exchange_order_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        command_id = self.command_id
        name = self.name
        account_id = self.account_id
        contract_id = self.contract_id
        timestamp = self.timestamp.isoformat()

        order_id = self.order_id
        exec_type = self.exec_type.value

        action = self.action.value

        id = self.id
        trade_date: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.trade_date, Unset):
            trade_date = self.trade_date.to_dict()

        exec_ref_id = self.exec_ref_id
        ord_status: Union[Unset, str] = UNSET
        if not isinstance(self.ord_status, Unset):
            ord_status = self.ord_status.value

        cum_qty = self.cum_qty
        avg_px = self.avg_px
        last_qty = self.last_qty
        last_px = self.last_px
        reject_reason: Union[Unset, str] = UNSET
        if not isinstance(self.reject_reason, Unset):
            reject_reason = self.reject_reason.value

        text = self.text
        exchange_order_id = self.exchange_order_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commandId": command_id,
                "name": name,
                "accountId": account_id,
                "contractId": contract_id,
                "timestamp": timestamp,
                "orderId": order_id,
                "execType": exec_type,
                "action": action,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if trade_date is not UNSET:
            field_dict["tradeDate"] = trade_date
        if exec_ref_id is not UNSET:
            field_dict["execRefId"] = exec_ref_id
        if ord_status is not UNSET:
            field_dict["ordStatus"] = ord_status
        if cum_qty is not UNSET:
            field_dict["cumQty"] = cum_qty
        if avg_px is not UNSET:
            field_dict["avgPx"] = avg_px
        if last_qty is not UNSET:
            field_dict["lastQty"] = last_qty
        if last_px is not UNSET:
            field_dict["lastPx"] = last_px
        if reject_reason is not UNSET:
            field_dict["rejectReason"] = reject_reason
        if text is not UNSET:
            field_dict["text"] = text
        if exchange_order_id is not UNSET:
            field_dict["exchangeOrderId"] = exchange_order_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        command_id = d.pop("commandId")

        name = d.pop("name")

        account_id = d.pop("accountId")

        contract_id = d.pop("contractId")

        timestamp = isoparse(d.pop("timestamp"))

        order_id = d.pop("orderId")

        exec_type = ExecutionReportExecType(d.pop("execType"))

        action = ExecutionReportAction(d.pop("action"))

        id = d.pop("id", UNSET)

        _trade_date = d.pop("tradeDate", UNSET)
        trade_date: Union[Unset, TradeDate]
        if isinstance(_trade_date, Unset):
            trade_date = UNSET
        else:
            trade_date = TradeDate.from_dict(_trade_date)

        exec_ref_id = d.pop("execRefId", UNSET)

        _ord_status = d.pop("ordStatus", UNSET)
        ord_status: Union[Unset, ExecutionReportOrdStatus]
        if isinstance(_ord_status, Unset):
            ord_status = UNSET
        else:
            ord_status = ExecutionReportOrdStatus(_ord_status)

        cum_qty = d.pop("cumQty", UNSET)

        avg_px = d.pop("avgPx", UNSET)

        last_qty = d.pop("lastQty", UNSET)

        last_px = d.pop("lastPx", UNSET)

        _reject_reason = d.pop("rejectReason", UNSET)
        reject_reason: Union[Unset, ExecutionReportRejectReason]
        if isinstance(_reject_reason, Unset):
            reject_reason = UNSET
        else:
            reject_reason = ExecutionReportRejectReason(_reject_reason)

        text = d.pop("text", UNSET)

        exchange_order_id = d.pop("exchangeOrderId", UNSET)

        execution_report = cls(
            command_id=command_id,
            name=name,
            account_id=account_id,
            contract_id=contract_id,
            timestamp=timestamp,
            order_id=order_id,
            exec_type=exec_type,
            action=action,
            id=id,
            trade_date=trade_date,
            exec_ref_id=exec_ref_id,
            ord_status=ord_status,
            cum_qty=cum_qty,
            avg_px=avg_px,
            last_qty=last_qty,
            last_px=last_px,
            reject_reason=reject_reason,
            text=text,
            exchange_order_id=exchange_order_id,
        )

        execution_report.additional_properties = d
        return execution_report

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
