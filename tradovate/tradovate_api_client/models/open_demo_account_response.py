from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenDemoAccountResponse")


@attr.s(auto_attribs=True)
class OpenDemoAccountResponse:
    """
    Attributes:
        error_text (Union[Unset, str]): Non-empty if the request failed
        account_id (Union[Unset, int]):
    """

    error_text: Union[Unset, str] = UNSET
    account_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_text = self.error_text
        account_id = self.account_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if account_id is not UNSET:
            field_dict["accountId"] = account_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error_text = d.pop("errorText", UNSET)

        account_id = d.pop("accountId", UNSET)

        open_demo_account_response = cls(
            error_text=error_text,
            account_id=account_id,
        )

        open_demo_account_response.additional_properties = d
        return open_demo_account_response

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
