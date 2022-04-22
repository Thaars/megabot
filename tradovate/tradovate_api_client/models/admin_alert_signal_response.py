from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.admin_alert_signal import AdminAlertSignal
from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminAlertSignalResponse")


@attr.s(auto_attribs=True)
class AdminAlertSignalResponse:
    """
    Attributes:
        error_text (Union[Unset, str]): Non-empty if the request failed
        admin_alert_signal (Union[Unset, AdminAlertSignal]):
    """

    error_text: Union[Unset, str] = UNSET
    admin_alert_signal: Union[Unset, AdminAlertSignal] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_text = self.error_text
        admin_alert_signal: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.admin_alert_signal, Unset):
            admin_alert_signal = self.admin_alert_signal.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if admin_alert_signal is not UNSET:
            field_dict["adminAlertSignal"] = admin_alert_signal

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error_text = d.pop("errorText", UNSET)

        _admin_alert_signal = d.pop("adminAlertSignal", UNSET)
        admin_alert_signal: Union[Unset, AdminAlertSignal]
        if isinstance(_admin_alert_signal, Unset):
            admin_alert_signal = UNSET
        else:
            admin_alert_signal = AdminAlertSignal.from_dict(_admin_alert_signal)

        admin_alert_signal_response = cls(
            error_text=error_text,
            admin_alert_signal=admin_alert_signal,
        )

        admin_alert_signal_response.additional_properties = d
        return admin_alert_signal_response

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
