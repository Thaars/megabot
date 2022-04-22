import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.place_order_action import PlaceOrderAction
from ..models.place_order_order_type import PlaceOrderOrderType
from ..models.place_order_time_in_force import PlaceOrderTimeInForce
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlaceOrder")


@attr.s(auto_attribs=True)
class PlaceOrder:
    """
    Attributes:
        action (PlaceOrderAction): Buy, Sell
        symbol (str):
        order_qty (int):
        order_type (PlaceOrderOrderType): Limit, MIT, Market, QTS, Stop, StopLimit, TrailingStop, TrailingStopLimit
        account_spec (Union[Unset, str]):
        account_id (Union[Unset, int]):
        cl_ord_id (Union[Unset, str]):
        price (Union[Unset, float]):
        stop_price (Union[Unset, float]):
        max_show (Union[Unset, int]):
        peg_difference (Union[Unset, float]):
        time_in_force (Union[Unset, PlaceOrderTimeInForce]): Day, FOK, GTC, GTD, IOC
        expire_time (Union[Unset, datetime.datetime]):
        text (Union[Unset, str]):
        activation_time (Union[Unset, datetime.datetime]):
        custom_tag_50 (Union[Unset, str]):
        is_automated (Union[Unset, bool]):
    """

    action: PlaceOrderAction
    symbol: str
    order_qty: int
    order_type: PlaceOrderOrderType
    account_spec: Union[Unset, str] = UNSET
    account_id: Union[Unset, int] = UNSET
    cl_ord_id: Union[Unset, str] = UNSET
    price: Union[Unset, float] = UNSET
    stop_price: Union[Unset, float] = UNSET
    max_show: Union[Unset, int] = UNSET
    peg_difference: Union[Unset, float] = UNSET
    time_in_force: Union[Unset, PlaceOrderTimeInForce] = UNSET
    expire_time: Union[Unset, datetime.datetime] = UNSET
    text: Union[Unset, str] = UNSET
    activation_time: Union[Unset, datetime.datetime] = UNSET
    custom_tag_50: Union[Unset, str] = UNSET
    is_automated: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action = self.action.value

        symbol = self.symbol
        order_qty = self.order_qty
        order_type = self.order_type.value

        account_spec = self.account_spec
        account_id = self.account_id
        cl_ord_id = self.cl_ord_id
        price = self.price
        stop_price = self.stop_price
        max_show = self.max_show
        peg_difference = self.peg_difference
        time_in_force: Union[Unset, str] = UNSET
        if not isinstance(self.time_in_force, Unset):
            time_in_force = self.time_in_force.value

        expire_time: Union[Unset, str] = UNSET
        if not isinstance(self.expire_time, Unset):
            expire_time = self.expire_time.isoformat()

        text = self.text
        activation_time: Union[Unset, str] = UNSET
        if not isinstance(self.activation_time, Unset):
            activation_time = self.activation_time.isoformat()

        custom_tag_50 = self.custom_tag_50
        is_automated = self.is_automated

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "symbol": symbol,
                "orderQty": order_qty,
                "orderType": order_type,
            }
        )
        if account_spec is not UNSET:
            field_dict["accountSpec"] = account_spec
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if cl_ord_id is not UNSET:
            field_dict["clOrdId"] = cl_ord_id
        if price is not UNSET:
            field_dict["price"] = price
        if stop_price is not UNSET:
            field_dict["stopPrice"] = stop_price
        if max_show is not UNSET:
            field_dict["maxShow"] = max_show
        if peg_difference is not UNSET:
            field_dict["pegDifference"] = peg_difference
        if time_in_force is not UNSET:
            field_dict["timeInForce"] = time_in_force
        if expire_time is not UNSET:
            field_dict["expireTime"] = expire_time
        if text is not UNSET:
            field_dict["text"] = text
        if activation_time is not UNSET:
            field_dict["activationTime"] = activation_time
        if custom_tag_50 is not UNSET:
            field_dict["customTag50"] = custom_tag_50
        if is_automated is not UNSET:
            field_dict["isAutomated"] = is_automated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        action = PlaceOrderAction(d.pop("action"))

        symbol = d.pop("symbol")

        order_qty = d.pop("orderQty")

        order_type = PlaceOrderOrderType(d.pop("orderType"))

        account_spec = d.pop("accountSpec", UNSET)

        account_id = d.pop("accountId", UNSET)

        cl_ord_id = d.pop("clOrdId", UNSET)

        price = d.pop("price", UNSET)

        stop_price = d.pop("stopPrice", UNSET)

        max_show = d.pop("maxShow", UNSET)

        peg_difference = d.pop("pegDifference", UNSET)

        _time_in_force = d.pop("timeInForce", UNSET)
        time_in_force: Union[Unset, PlaceOrderTimeInForce]
        if isinstance(_time_in_force, Unset):
            time_in_force = UNSET
        else:
            time_in_force = PlaceOrderTimeInForce(_time_in_force)

        _expire_time = d.pop("expireTime", UNSET)
        expire_time: Union[Unset, datetime.datetime]
        if isinstance(_expire_time, Unset):
            expire_time = UNSET
        else:
            expire_time = isoparse(_expire_time)

        text = d.pop("text", UNSET)

        _activation_time = d.pop("activationTime", UNSET)
        activation_time: Union[Unset, datetime.datetime]
        if isinstance(_activation_time, Unset):
            activation_time = UNSET
        else:
            activation_time = isoparse(_activation_time)

        custom_tag_50 = d.pop("customTag50", UNSET)

        is_automated = d.pop("isAutomated", UNSET)

        place_order = cls(
            action=action,
            symbol=symbol,
            order_qty=order_qty,
            order_type=order_type,
            account_spec=account_spec,
            account_id=account_id,
            cl_ord_id=cl_ord_id,
            price=price,
            stop_price=stop_price,
            max_show=max_show,
            peg_difference=peg_difference,
            time_in_force=time_in_force,
            expire_time=expire_time,
            text=text,
            activation_time=activation_time,
            custom_tag_50=custom_tag_50,
            is_automated=is_automated,
        )

        place_order.additional_properties = d
        return place_order

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
