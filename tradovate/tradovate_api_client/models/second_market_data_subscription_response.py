from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.second_market_data_subscription import SecondMarketDataSubscription
from ..models.second_market_data_subscription_response_error_code import SecondMarketDataSubscriptionResponseErrorCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="SecondMarketDataSubscriptionResponse")


@attr.s(auto_attribs=True)
class SecondMarketDataSubscriptionResponse:
    """
    Attributes:
        error_text (Union[Unset, str]): Non-empty if the request failed
        error_code (Union[Unset, SecondMarketDataSubscriptionResponseErrorCode]): ConflictWithExisting,
            DowngradeNotAllowed, IncompatibleCMEMarketDataSubscriptionPlans, IncorrectPaymentMethod, InsufficientFunds,
            PaymentProviderError, PlanDiscontinued, SingleTrialOnly, Success, UnknownError
        second_market_data_subscription (Union[Unset, SecondMarketDataSubscription]):
    """

    error_text: Union[Unset, str] = UNSET
    error_code: Union[Unset, SecondMarketDataSubscriptionResponseErrorCode] = UNSET
    second_market_data_subscription: Union[Unset, SecondMarketDataSubscription] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_text = self.error_text
        error_code: Union[Unset, str] = UNSET
        if not isinstance(self.error_code, Unset):
            error_code = self.error_code.value

        second_market_data_subscription: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.second_market_data_subscription, Unset):
            second_market_data_subscription = self.second_market_data_subscription.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if second_market_data_subscription is not UNSET:
            field_dict["secondMarketDataSubscription"] = second_market_data_subscription

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error_text = d.pop("errorText", UNSET)

        _error_code = d.pop("errorCode", UNSET)
        error_code: Union[Unset, SecondMarketDataSubscriptionResponseErrorCode]
        if isinstance(_error_code, Unset):
            error_code = UNSET
        else:
            error_code = SecondMarketDataSubscriptionResponseErrorCode(_error_code)

        _second_market_data_subscription = d.pop("secondMarketDataSubscription", UNSET)
        second_market_data_subscription: Union[Unset, SecondMarketDataSubscription]
        if isinstance(_second_market_data_subscription, Unset):
            second_market_data_subscription = UNSET
        else:
            second_market_data_subscription = SecondMarketDataSubscription.from_dict(_second_market_data_subscription)

        second_market_data_subscription_response = cls(
            error_text=error_text,
            error_code=error_code,
            second_market_data_subscription=second_market_data_subscription,
        )

        second_market_data_subscription_response.additional_properties = d
        return second_market_data_subscription_response

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
