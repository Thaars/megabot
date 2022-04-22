from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.market_data_subscription import MarketDataSubscription
from ..models.market_data_subscription_response_error_code import MarketDataSubscriptionResponseErrorCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketDataSubscriptionResponse")


@attr.s(auto_attribs=True)
class MarketDataSubscriptionResponse:
    """
    Attributes:
        error_text (Union[Unset, str]): Non-empty if the request failed
        error_code (Union[Unset, MarketDataSubscriptionResponseErrorCode]): ConflictWithExisting, DowngradeNotAllowed,
            IncompatibleCMEMarketDataSubscriptionPlans, IncorrectPaymentMethod, InsufficientFunds, PaymentProviderError,
            PlanDiscontinued, SingleTrialOnly, Success, UnknownError
        market_data_subscription (Union[Unset, MarketDataSubscription]):
    """

    error_text: Union[Unset, str] = UNSET
    error_code: Union[Unset, MarketDataSubscriptionResponseErrorCode] = UNSET
    market_data_subscription: Union[Unset, MarketDataSubscription] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_text = self.error_text
        error_code: Union[Unset, str] = UNSET
        if not isinstance(self.error_code, Unset):
            error_code = self.error_code.value

        market_data_subscription: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.market_data_subscription, Unset):
            market_data_subscription = self.market_data_subscription.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if market_data_subscription is not UNSET:
            field_dict["marketDataSubscription"] = market_data_subscription

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error_text = d.pop("errorText", UNSET)

        _error_code = d.pop("errorCode", UNSET)
        error_code: Union[Unset, MarketDataSubscriptionResponseErrorCode]
        if isinstance(_error_code, Unset):
            error_code = UNSET
        else:
            error_code = MarketDataSubscriptionResponseErrorCode(_error_code)

        _market_data_subscription = d.pop("marketDataSubscription", UNSET)
        market_data_subscription: Union[Unset, MarketDataSubscription]
        if isinstance(_market_data_subscription, Unset):
            market_data_subscription = UNSET
        else:
            market_data_subscription = MarketDataSubscription.from_dict(_market_data_subscription)

        market_data_subscription_response = cls(
            error_text=error_text,
            error_code=error_code,
            market_data_subscription=market_data_subscription,
        )

        market_data_subscription_response.additional_properties = d
        return market_data_subscription_response

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
