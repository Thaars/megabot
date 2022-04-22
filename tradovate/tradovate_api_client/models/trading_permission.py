import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.trading_permission_status import TradingPermissionStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="TradingPermission")


@attr.s(auto_attribs=True)
class TradingPermission:
    """
    Attributes:
        user_id (int):
        account_id (int):
        account_holder_contact (str):
        account_holder_email (str):
        cta_contact (str):
        cta_email (str):
        status (TradingPermissionStatus): Accepted, Approved, Declined, Requested, Revoked
        id (Union[Unset, int]):
        updated (Union[Unset, datetime.datetime]):
        approved_by_id (Union[Unset, int]):
    """

    user_id: int
    account_id: int
    account_holder_contact: str
    account_holder_email: str
    cta_contact: str
    cta_email: str
    status: TradingPermissionStatus
    id: Union[Unset, int] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    approved_by_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        account_id = self.account_id
        account_holder_contact = self.account_holder_contact
        account_holder_email = self.account_holder_email
        cta_contact = self.cta_contact
        cta_email = self.cta_email
        status = self.status.value

        id = self.id
        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        approved_by_id = self.approved_by_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "accountId": account_id,
                "accountHolderContact": account_holder_contact,
                "accountHolderEmail": account_holder_email,
                "ctaContact": cta_contact,
                "ctaEmail": cta_email,
                "status": status,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if updated is not UNSET:
            field_dict["updated"] = updated
        if approved_by_id is not UNSET:
            field_dict["approvedById"] = approved_by_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("userId")

        account_id = d.pop("accountId")

        account_holder_contact = d.pop("accountHolderContact")

        account_holder_email = d.pop("accountHolderEmail")

        cta_contact = d.pop("ctaContact")

        cta_email = d.pop("ctaEmail")

        status = TradingPermissionStatus(d.pop("status"))

        id = d.pop("id", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, datetime.datetime]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        approved_by_id = d.pop("approvedById", UNSET)

        trading_permission = cls(
            user_id=user_id,
            account_id=account_id,
            account_holder_contact=account_holder_contact,
            account_holder_email=account_holder_email,
            cta_contact=cta_contact,
            cta_email=cta_email,
            status=status,
            id=id,
            updated=updated,
            approved_by_id=approved_by_id,
        )

        trading_permission.additional_properties = d
        return trading_permission

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
