from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RequestTradingPermission")


@attr.s(auto_attribs=True)
class RequestTradingPermission:
    """
    Attributes:
        account_id (int):
        cta_contact (str):
        cta_email (str):
    """

    account_id: int
    cta_contact: str
    cta_email: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        cta_contact = self.cta_contact
        cta_email = self.cta_email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "ctaContact": cta_contact,
                "ctaEmail": cta_email,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("accountId")

        cta_contact = d.pop("ctaContact")

        cta_email = d.pop("ctaEmail")

        request_trading_permission = cls(
            account_id=account_id,
            cta_contact=cta_contact,
            cta_email=cta_email,
        )

        request_trading_permission.additional_properties = d
        return request_trading_permission

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
