import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.command_report_command_status import CommandReportCommandStatus
from ..models.command_report_ord_status import CommandReportOrdStatus
from ..models.command_report_reject_reason import CommandReportRejectReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="CommandReport")


@attr.s(auto_attribs=True)
class CommandReport:
    """
    Attributes:
        command_id (int):
        timestamp (datetime.datetime):
        command_status (CommandReportCommandStatus): AtExecution, ExecutionRejected, ExecutionStopped,
            ExecutionSuspended, OnHold, Pending, PendingExecution, Replaced, RiskPassed, RiskRejected
        id (Union[Unset, int]):
        reject_reason (Union[Unset, CommandReportRejectReason]): AccountClosed, AdvancedTrailingStopUnsupported,
            AnotherCommandPending, BackMonthProhibited, ExecutionProviderNotConfigured, ExecutionProviderUnavailable,
            InvalidContract, InvalidPrice, LiquidationOnly, LiquidationOnlyBeforeExpiration, MaxOrderQtyIsNotSpecified,
            MaxOrderQtyLimitReached, MaxPosLimitMisconfigured, MaxPosLimitReached, MaxTotalPosLimitReached,
            MultipleAccountPlanRequired, NoQuote, NotEnoughLiquidity, OtherExecutionRelated, ParentRejected,
            RiskCheckTimeout, SessionClosed, Success, TooLate, TradingLocked, TrailingStopNonOrderQtyModify, Unauthorized,
            UnknownReason, Unsupported
        text (Union[Unset, str]):
        ord_status (Union[Unset, CommandReportOrdStatus]): Canceled, Completed, Expired, Filled, PendingCancel,
            PendingNew, PendingReplace, Rejected, Suspended, Unknown, Working
    """

    command_id: int
    timestamp: datetime.datetime
    command_status: CommandReportCommandStatus
    id: Union[Unset, int] = UNSET
    reject_reason: Union[Unset, CommandReportRejectReason] = UNSET
    text: Union[Unset, str] = UNSET
    ord_status: Union[Unset, CommandReportOrdStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        command_id = self.command_id
        timestamp = self.timestamp.isoformat()

        command_status = self.command_status.value

        id = self.id
        reject_reason: Union[Unset, str] = UNSET
        if not isinstance(self.reject_reason, Unset):
            reject_reason = self.reject_reason.value

        text = self.text
        ord_status: Union[Unset, str] = UNSET
        if not isinstance(self.ord_status, Unset):
            ord_status = self.ord_status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commandId": command_id,
                "timestamp": timestamp,
                "commandStatus": command_status,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if reject_reason is not UNSET:
            field_dict["rejectReason"] = reject_reason
        if text is not UNSET:
            field_dict["text"] = text
        if ord_status is not UNSET:
            field_dict["ordStatus"] = ord_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        command_id = d.pop("commandId")

        timestamp = isoparse(d.pop("timestamp"))

        command_status = CommandReportCommandStatus(d.pop("commandStatus"))

        id = d.pop("id", UNSET)

        _reject_reason = d.pop("rejectReason", UNSET)
        reject_reason: Union[Unset, CommandReportRejectReason]
        if isinstance(_reject_reason, Unset):
            reject_reason = UNSET
        else:
            reject_reason = CommandReportRejectReason(_reject_reason)

        text = d.pop("text", UNSET)

        _ord_status = d.pop("ordStatus", UNSET)
        ord_status: Union[Unset, CommandReportOrdStatus]
        if isinstance(_ord_status, Unset):
            ord_status = UNSET
        else:
            ord_status = CommandReportOrdStatus(_ord_status)

        command_report = cls(
            command_id=command_id,
            timestamp=timestamp,
            command_status=command_status,
            id=id,
            reject_reason=reject_reason,
            text=text,
            ord_status=ord_status,
        )

        command_report.additional_properties = d
        return command_report

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
