from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.place_oco_result_failure_reason import PlaceOcoResultFailureReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlaceOcoResult")


@attr.s(auto_attribs=True)
class PlaceOcoResult:
    """
    Attributes:
        failure_reason (Union[Unset, PlaceOcoResultFailureReason]): AccountClosed, AdvancedTrailingStopUnsupported,
            AnotherCommandPending, BackMonthProhibited, ExecutionProviderNotConfigured, ExecutionProviderUnavailable,
            InvalidContract, InvalidPrice, LiquidationOnly, LiquidationOnlyBeforeExpiration, MaxOrderQtyIsNotSpecified,
            MaxOrderQtyLimitReached, MaxPosLimitMisconfigured, MaxPosLimitReached, MaxTotalPosLimitReached,
            MultipleAccountPlanRequired, NoQuote, NotEnoughLiquidity, OtherExecutionRelated, ParentRejected,
            RiskCheckTimeout, SessionClosed, Success, TooLate, TradingLocked, TrailingStopNonOrderQtyModify, Unauthorized,
            UnknownReason, Unsupported
        failure_text (Union[Unset, str]):
        order_id (Union[Unset, int]):
        oco_id (Union[Unset, int]):
    """

    failure_reason: Union[Unset, PlaceOcoResultFailureReason] = UNSET
    failure_text: Union[Unset, str] = UNSET
    order_id: Union[Unset, int] = UNSET
    oco_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        failure_reason: Union[Unset, str] = UNSET
        if not isinstance(self.failure_reason, Unset):
            failure_reason = self.failure_reason.value

        failure_text = self.failure_text
        order_id = self.order_id
        oco_id = self.oco_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if failure_reason is not UNSET:
            field_dict["failureReason"] = failure_reason
        if failure_text is not UNSET:
            field_dict["failureText"] = failure_text
        if order_id is not UNSET:
            field_dict["orderId"] = order_id
        if oco_id is not UNSET:
            field_dict["ocoId"] = oco_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _failure_reason = d.pop("failureReason", UNSET)
        failure_reason: Union[Unset, PlaceOcoResultFailureReason]
        if isinstance(_failure_reason, Unset):
            failure_reason = UNSET
        else:
            failure_reason = PlaceOcoResultFailureReason(_failure_reason)

        failure_text = d.pop("failureText", UNSET)

        order_id = d.pop("orderId", UNSET)

        oco_id = d.pop("ocoId", UNSET)

        place_oco_result = cls(
            failure_reason=failure_reason,
            failure_text=failure_text,
            order_id=order_id,
            oco_id=oco_id,
        )

        place_oco_result.additional_properties = d
        return place_oco_result

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
