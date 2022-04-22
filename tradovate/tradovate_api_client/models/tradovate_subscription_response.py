from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.tradovate_subscription import TradovateSubscription
from ..models.tradovate_subscription_response_error_code import TradovateSubscriptionResponseErrorCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="TradovateSubscriptionResponse")


@attr.s(auto_attribs=True)
class TradovateSubscriptionResponse:
    """
    Attributes:
        error_text (Union[Unset, str]): Non-empty if the request failed
        error_code (Union[Unset, TradovateSubscriptionResponseErrorCode]): ConflictWithExisting, DowngradeNotAllowed,
            IncompatibleCMEMarketDataSubscriptionPlans, IncorrectPaymentMethod, InsufficientFunds, PaymentProviderError,
            PlanDiscontinued, SingleTrialOnly, Success, UnknownError
        tradovate_subscription (Union[Unset, TradovateSubscription]):
    """

    error_text: Union[Unset, str] = UNSET
    error_code: Union[Unset, TradovateSubscriptionResponseErrorCode] = UNSET
    tradovate_subscription: Union[Unset, TradovateSubscription] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_text = self.error_text
        error_code: Union[Unset, str] = UNSET
        if not isinstance(self.error_code, Unset):
            error_code = self.error_code.value

        tradovate_subscription: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tradovate_subscription, Unset):
            tradovate_subscription = self.tradovate_subscription.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if tradovate_subscription is not UNSET:
            field_dict["tradovateSubscription"] = tradovate_subscription

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error_text = d.pop("errorText", UNSET)

        _error_code = d.pop("errorCode", UNSET)
        error_code: Union[Unset, TradovateSubscriptionResponseErrorCode]
        if isinstance(_error_code, Unset):
            error_code = UNSET
        else:
            error_code = TradovateSubscriptionResponseErrorCode(_error_code)

        _tradovate_subscription = d.pop("tradovateSubscription", UNSET)
        tradovate_subscription: Union[Unset, TradovateSubscription]
        if isinstance(_tradovate_subscription, Unset):
            tradovate_subscription = UNSET
        else:
            tradovate_subscription = TradovateSubscription.from_dict(_tradovate_subscription)

        tradovate_subscription_response = cls(
            error_text=error_text,
            error_code=error_code,
            tradovate_subscription=tradovate_subscription,
        )

        tradovate_subscription_response.additional_properties = d
        return tradovate_subscription_response

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
