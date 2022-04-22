from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModifyOrderStrategy")


@attr.s(auto_attribs=True)
class ModifyOrderStrategy:
    """
    Attributes:
        order_strategy_id (int):
        command (str):
        custom_tag_50 (Union[Unset, str]):
    """

    order_strategy_id: int
    command: str
    custom_tag_50: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_strategy_id = self.order_strategy_id
        command = self.command
        custom_tag_50 = self.custom_tag_50

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orderStrategyId": order_strategy_id,
                "command": command,
            }
        )
        if custom_tag_50 is not UNSET:
            field_dict["customTag50"] = custom_tag_50

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        order_strategy_id = d.pop("orderStrategyId")

        command = d.pop("command")

        custom_tag_50 = d.pop("customTag50", UNSET)

        modify_order_strategy = cls(
            order_strategy_id=order_strategy_id,
            command=command,
            custom_tag_50=custom_tag_50,
        )

        modify_order_strategy.additional_properties = d
        return modify_order_strategy

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
