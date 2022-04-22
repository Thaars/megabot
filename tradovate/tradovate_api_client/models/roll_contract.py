from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RollContract")


@attr.s(auto_attribs=True)
class RollContract:
    """
    Attributes:
        name (str):
        forward (bool):
        if_expired (Union[Unset, bool]):
    """

    name: str
    forward: bool
    if_expired: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        forward = self.forward
        if_expired = self.if_expired

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "forward": forward,
            }
        )
        if if_expired is not UNSET:
            field_dict["ifExpired"] = if_expired

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        forward = d.pop("forward")

        if_expired = d.pop("ifExpired", UNSET)

        roll_contract = cls(
            name=name,
            forward=forward,
            if_expired=if_expired,
        )

        roll_contract.additional_properties = d
        return roll_contract

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
