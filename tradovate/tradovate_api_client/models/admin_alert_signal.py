import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminAlertSignal")


@attr.s(auto_attribs=True)
class AdminAlertSignal:
    """
    Attributes:
        timestamp (datetime.datetime):
        admin_alert_id (int):
        text (str):
        email_sent (bool):
        subject_id (int):
        id (Union[Unset, int]):
        related_to_account_id (Union[Unset, int]):
        related_to_user_id (Union[Unset, int]):
        owned_by_admin_id (Union[Unset, int]): Owned By...
        completed (Union[Unset, datetime.datetime]):
    """

    timestamp: datetime.datetime
    admin_alert_id: int
    text: str
    email_sent: bool
    subject_id: int
    id: Union[Unset, int] = UNSET
    related_to_account_id: Union[Unset, int] = UNSET
    related_to_user_id: Union[Unset, int] = UNSET
    owned_by_admin_id: Union[Unset, int] = UNSET
    completed: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        admin_alert_id = self.admin_alert_id
        text = self.text
        email_sent = self.email_sent
        subject_id = self.subject_id
        id = self.id
        related_to_account_id = self.related_to_account_id
        related_to_user_id = self.related_to_user_id
        owned_by_admin_id = self.owned_by_admin_id
        completed: Union[Unset, str] = UNSET
        if not isinstance(self.completed, Unset):
            completed = self.completed.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "adminAlertId": admin_alert_id,
                "text": text,
                "emailSent": email_sent,
                "subjectId": subject_id,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if related_to_account_id is not UNSET:
            field_dict["relatedToAccountId"] = related_to_account_id
        if related_to_user_id is not UNSET:
            field_dict["relatedToUserId"] = related_to_user_id
        if owned_by_admin_id is not UNSET:
            field_dict["ownedByAdminId"] = owned_by_admin_id
        if completed is not UNSET:
            field_dict["completed"] = completed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timestamp = isoparse(d.pop("timestamp"))

        admin_alert_id = d.pop("adminAlertId")

        text = d.pop("text")

        email_sent = d.pop("emailSent")

        subject_id = d.pop("subjectId")

        id = d.pop("id", UNSET)

        related_to_account_id = d.pop("relatedToAccountId", UNSET)

        related_to_user_id = d.pop("relatedToUserId", UNSET)

        owned_by_admin_id = d.pop("ownedByAdminId", UNSET)

        _completed = d.pop("completed", UNSET)
        completed: Union[Unset, datetime.datetime]
        if isinstance(_completed, Unset):
            completed = UNSET
        else:
            completed = isoparse(_completed)

        admin_alert_signal = cls(
            timestamp=timestamp,
            admin_alert_id=admin_alert_id,
            text=text,
            email_sent=email_sent,
            subject_id=subject_id,
            id=id,
            related_to_account_id=related_to_account_id,
            related_to_user_id=related_to_user_id,
            owned_by_admin_id=owned_by_admin_id,
            completed=completed,
        )

        admin_alert_signal.additional_properties = d
        return admin_alert_signal

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
