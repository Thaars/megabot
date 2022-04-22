from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.start_order_strategy_action import StartOrderStrategyAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="StartOrderStrategy")


@attr.s(auto_attribs=True)
class StartOrderStrategy:
    """
    Attributes:
        symbol (str):
        order_strategy_type_id (int):
        action (StartOrderStrategyAction): Buy, Sell
        account_id (Union[Unset, int]):
        account_spec (Union[Unset, str]):
        params (Union[Unset, str]):
        uuid (Union[Unset, str]):
        custom_tag_50 (Union[Unset, str]):
    """

    symbol: str
    order_strategy_type_id: int
    action: StartOrderStrategyAction
    account_id: Union[Unset, int] = UNSET
    account_spec: Union[Unset, str] = UNSET
    params: Union[Unset, str] = UNSET
    uuid: Union[Unset, str] = UNSET
    custom_tag_50: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        symbol = self.symbol
        order_strategy_type_id = self.order_strategy_type_id
        action = self.action.value

        account_id = self.account_id
        account_spec = self.account_spec
        params = self.params
        uuid = self.uuid
        custom_tag_50 = self.custom_tag_50

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "orderStrategyTypeId": order_strategy_type_id,
                "action": action,
            }
        )
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if account_spec is not UNSET:
            field_dict["accountSpec"] = account_spec
        if params is not UNSET:
            field_dict["params"] = params
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if custom_tag_50 is not UNSET:
            field_dict["customTag50"] = custom_tag_50

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        symbol = d.pop("symbol")

        order_strategy_type_id = d.pop("orderStrategyTypeId")

        action = StartOrderStrategyAction(d.pop("action"))

        account_id = d.pop("accountId", UNSET)

        account_spec = d.pop("accountSpec", UNSET)

        params = d.pop("params", UNSET)

        uuid = d.pop("uuid", UNSET)

        custom_tag_50 = d.pop("customTag50", UNSET)

        start_order_strategy = cls(
            symbol=symbol,
            order_strategy_type_id=order_strategy_type_id,
            action=action,
            account_id=account_id,
            account_spec=account_spec,
            params=params,
            uuid=uuid,
            custom_tag_50=custom_tag_50,
        )

        start_order_strategy.additional_properties = d
        return start_order_strategy

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
