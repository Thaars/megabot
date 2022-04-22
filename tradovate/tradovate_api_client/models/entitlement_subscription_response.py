from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.entitlement_subscription_response_error_code import EntitlementSubscriptionResponseErrorCode
from ..models.user_plugin import UserPlugin
from ..types import UNSET, Unset

T = TypeVar("T", bound="EntitlementSubscriptionResponse")


@attr.s(auto_attribs=True)
class EntitlementSubscriptionResponse:
    """
    Attributes:
        error_text (Union[Unset, str]): Non-empty if the request failed
        error_code (Union[Unset, EntitlementSubscriptionResponseErrorCode]): ConflictWithExisting, DowngradeNotAllowed,
            IncompatibleCMEMarketDataSubscriptionPlans, IncorrectPaymentMethod, InsufficientFunds, PaymentProviderError,
            PlanDiscontinued, SingleTrialOnly, Success, UnknownError
        entitlement_subscription (Union[Unset, UserPlugin]):
    """

    error_text: Union[Unset, str] = UNSET
    error_code: Union[Unset, EntitlementSubscriptionResponseErrorCode] = UNSET
    entitlement_subscription: Union[Unset, UserPlugin] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_text = self.error_text
        error_code: Union[Unset, str] = UNSET
        if not isinstance(self.error_code, Unset):
            error_code = self.error_code.value

        entitlement_subscription: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entitlement_subscription, Unset):
            entitlement_subscription = self.entitlement_subscription.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if entitlement_subscription is not UNSET:
            field_dict["entitlementSubscription"] = entitlement_subscription

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error_text = d.pop("errorText", UNSET)

        _error_code = d.pop("errorCode", UNSET)
        error_code: Union[Unset, EntitlementSubscriptionResponseErrorCode]
        if isinstance(_error_code, Unset):
            error_code = UNSET
        else:
            error_code = EntitlementSubscriptionResponseErrorCode(_error_code)

        _entitlement_subscription = d.pop("entitlementSubscription", UNSET)
        entitlement_subscription: Union[Unset, UserPlugin]
        if isinstance(_entitlement_subscription, Unset):
            entitlement_subscription = UNSET
        else:
            entitlement_subscription = UserPlugin.from_dict(_entitlement_subscription)

        entitlement_subscription_response = cls(
            error_text=error_text,
            error_code=error_code,
            entitlement_subscription=entitlement_subscription,
        )

        entitlement_subscription_response.additional_properties = d
        return entitlement_subscription_response

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
