from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LiquidatePosition")


@attr.s(auto_attribs=True)
class LiquidatePosition:
    """
    Attributes:
        account_id (int):
        contract_id (int):
        admin (bool):
        custom_tag_50 (Union[Unset, str]):
    """

    account_id: int
    contract_id: int
    admin: bool
    custom_tag_50: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        contract_id = self.contract_id
        admin = self.admin
        custom_tag_50 = self.custom_tag_50

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "contractId": contract_id,
                "admin": admin,
            }
        )
        if custom_tag_50 is not UNSET:
            field_dict["customTag50"] = custom_tag_50

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("accountId")

        contract_id = d.pop("contractId")

        admin = d.pop("admin")

        custom_tag_50 = d.pop("customTag50", UNSET)

        liquidate_position = cls(
            account_id=account_id,
            contract_id=contract_id,
            admin=admin,
            custom_tag_50=custom_tag_50,
        )

        liquidate_position.additional_properties = d
        return liquidate_position

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
