from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenDemoAccount")


@attr.s(auto_attribs=True)
class OpenDemoAccount:
    """
    Attributes:
        template_account_id (Union[Unset, int]):
        name (Union[Unset, str]):
        initial_balance (Union[Unset, float]):
    """

    template_account_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    initial_balance: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        template_account_id = self.template_account_id
        name = self.name
        initial_balance = self.initial_balance

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if template_account_id is not UNSET:
            field_dict["templateAccountId"] = template_account_id
        if name is not UNSET:
            field_dict["name"] = name
        if initial_balance is not UNSET:
            field_dict["initialBalance"] = initial_balance

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        template_account_id = d.pop("templateAccountId", UNSET)

        name = d.pop("name", UNSET)

        initial_balance = d.pop("initialBalance", UNSET)

        open_demo_account = cls(
            template_account_id=template_account_id,
            name=name,
            initial_balance=initial_balance,
        )

        open_demo_account.additional_properties = d
        return open_demo_account

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
