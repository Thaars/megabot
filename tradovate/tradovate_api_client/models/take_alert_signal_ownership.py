from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="TakeAlertSignalOwnership")


@attr.s(auto_attribs=True)
class TakeAlertSignalOwnership:
    """
    Attributes:
        admin_alert_signal_id (int):
    """

    admin_alert_signal_id: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        admin_alert_signal_id = self.admin_alert_signal_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "adminAlertSignalId": admin_alert_signal_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        admin_alert_signal_id = d.pop("adminAlertSignalId")

        take_alert_signal_ownership = cls(
            admin_alert_signal_id=admin_alert_signal_id,
        )

        take_alert_signal_ownership.additional_properties = d
        return take_alert_signal_ownership

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
