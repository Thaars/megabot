from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.order_strategy import OrderStrategy
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderStrategyStatusResponse")


@attr.s(auto_attribs=True)
class OrderStrategyStatusResponse:
    """
    Attributes:
        error_text (Union[Unset, str]): Non-empty if the request failed
        order_strategy (Union[Unset, OrderStrategy]):
    """

    error_text: Union[Unset, str] = UNSET
    order_strategy: Union[Unset, OrderStrategy] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_text = self.error_text
        order_strategy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.order_strategy, Unset):
            order_strategy = self.order_strategy.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if order_strategy is not UNSET:
            field_dict["orderStrategy"] = order_strategy

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error_text = d.pop("errorText", UNSET)

        _order_strategy = d.pop("orderStrategy", UNSET)
        order_strategy: Union[Unset, OrderStrategy]
        if isinstance(_order_strategy, Unset):
            order_strategy = UNSET
        else:
            order_strategy = OrderStrategy.from_dict(_order_strategy)

        order_strategy_status_response = cls(
            error_text=error_text,
            order_strategy=order_strategy,
        )

        order_strategy_status_response.additional_properties = d
        return order_strategy_status_response

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
