from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.product_margin import ProductMargin
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductFeeParams")


@attr.s(auto_attribs=True)
class ProductFeeParams:
    """
    Attributes:
        product_id (int):
        clearing_fee (Union[Unset, float]):
        clearing_currency_id (Union[Unset, int]):
        exchange_fee (Union[Unset, float]):
        exchange_currency_id (Union[Unset, int]):
        nfa_fee (Union[Unset, float]):
        nfa_currency_id (Union[Unset, int]):
        brokerage_fee (Union[Unset, float]):
        brokerage_currency_id (Union[Unset, int]):
        ip_fee (Union[Unset, float]):
        ip_currency_id (Union[Unset, int]):
        commission (Union[Unset, float]):
        commission_currency_id (Union[Unset, int]):
        order_routing_fee (Union[Unset, float]):
        order_routing_currency_id (Union[Unset, int]):
        day_margin (Union[Unset, float]):
        night_margin (Union[Unset, float]):
        full_margin (Union[Unset, ProductMargin]):
    """

    product_id: int
    clearing_fee: Union[Unset, float] = UNSET
    clearing_currency_id: Union[Unset, int] = UNSET
    exchange_fee: Union[Unset, float] = UNSET
    exchange_currency_id: Union[Unset, int] = UNSET
    nfa_fee: Union[Unset, float] = UNSET
    nfa_currency_id: Union[Unset, int] = UNSET
    brokerage_fee: Union[Unset, float] = UNSET
    brokerage_currency_id: Union[Unset, int] = UNSET
    ip_fee: Union[Unset, float] = UNSET
    ip_currency_id: Union[Unset, int] = UNSET
    commission: Union[Unset, float] = UNSET
    commission_currency_id: Union[Unset, int] = UNSET
    order_routing_fee: Union[Unset, float] = UNSET
    order_routing_currency_id: Union[Unset, int] = UNSET
    day_margin: Union[Unset, float] = UNSET
    night_margin: Union[Unset, float] = UNSET
    full_margin: Union[Unset, ProductMargin] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        product_id = self.product_id
        clearing_fee = self.clearing_fee
        clearing_currency_id = self.clearing_currency_id
        exchange_fee = self.exchange_fee
        exchange_currency_id = self.exchange_currency_id
        nfa_fee = self.nfa_fee
        nfa_currency_id = self.nfa_currency_id
        brokerage_fee = self.brokerage_fee
        brokerage_currency_id = self.brokerage_currency_id
        ip_fee = self.ip_fee
        ip_currency_id = self.ip_currency_id
        commission = self.commission
        commission_currency_id = self.commission_currency_id
        order_routing_fee = self.order_routing_fee
        order_routing_currency_id = self.order_routing_currency_id
        day_margin = self.day_margin
        night_margin = self.night_margin
        full_margin: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.full_margin, Unset):
            full_margin = self.full_margin.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "productId": product_id,
            }
        )
        if clearing_fee is not UNSET:
            field_dict["clearingFee"] = clearing_fee
        if clearing_currency_id is not UNSET:
            field_dict["clearingCurrencyId"] = clearing_currency_id
        if exchange_fee is not UNSET:
            field_dict["exchangeFee"] = exchange_fee
        if exchange_currency_id is not UNSET:
            field_dict["exchangeCurrencyId"] = exchange_currency_id
        if nfa_fee is not UNSET:
            field_dict["nfaFee"] = nfa_fee
        if nfa_currency_id is not UNSET:
            field_dict["nfaCurrencyId"] = nfa_currency_id
        if brokerage_fee is not UNSET:
            field_dict["brokerageFee"] = brokerage_fee
        if brokerage_currency_id is not UNSET:
            field_dict["brokerageCurrencyId"] = brokerage_currency_id
        if ip_fee is not UNSET:
            field_dict["ipFee"] = ip_fee
        if ip_currency_id is not UNSET:
            field_dict["ipCurrencyId"] = ip_currency_id
        if commission is not UNSET:
            field_dict["commission"] = commission
        if commission_currency_id is not UNSET:
            field_dict["commissionCurrencyId"] = commission_currency_id
        if order_routing_fee is not UNSET:
            field_dict["orderRoutingFee"] = order_routing_fee
        if order_routing_currency_id is not UNSET:
            field_dict["orderRoutingCurrencyId"] = order_routing_currency_id
        if day_margin is not UNSET:
            field_dict["dayMargin"] = day_margin
        if night_margin is not UNSET:
            field_dict["nightMargin"] = night_margin
        if full_margin is not UNSET:
            field_dict["fullMargin"] = full_margin

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        product_id = d.pop("productId")

        clearing_fee = d.pop("clearingFee", UNSET)

        clearing_currency_id = d.pop("clearingCurrencyId", UNSET)

        exchange_fee = d.pop("exchangeFee", UNSET)

        exchange_currency_id = d.pop("exchangeCurrencyId", UNSET)

        nfa_fee = d.pop("nfaFee", UNSET)

        nfa_currency_id = d.pop("nfaCurrencyId", UNSET)

        brokerage_fee = d.pop("brokerageFee", UNSET)

        brokerage_currency_id = d.pop("brokerageCurrencyId", UNSET)

        ip_fee = d.pop("ipFee", UNSET)

        ip_currency_id = d.pop("ipCurrencyId", UNSET)

        commission = d.pop("commission", UNSET)

        commission_currency_id = d.pop("commissionCurrencyId", UNSET)

        order_routing_fee = d.pop("orderRoutingFee", UNSET)

        order_routing_currency_id = d.pop("orderRoutingCurrencyId", UNSET)

        day_margin = d.pop("dayMargin", UNSET)

        night_margin = d.pop("nightMargin", UNSET)

        _full_margin = d.pop("fullMargin", UNSET)
        full_margin: Union[Unset, ProductMargin]
        if isinstance(_full_margin, Unset):
            full_margin = UNSET
        else:
            full_margin = ProductMargin.from_dict(_full_margin)

        product_fee_params = cls(
            product_id=product_id,
            clearing_fee=clearing_fee,
            clearing_currency_id=clearing_currency_id,
            exchange_fee=exchange_fee,
            exchange_currency_id=exchange_currency_id,
            nfa_fee=nfa_fee,
            nfa_currency_id=nfa_currency_id,
            brokerage_fee=brokerage_fee,
            brokerage_currency_id=brokerage_currency_id,
            ip_fee=ip_fee,
            ip_currency_id=ip_currency_id,
            commission=commission,
            commission_currency_id=commission_currency_id,
            order_routing_fee=order_routing_fee,
            order_routing_currency_id=order_routing_currency_id,
            day_margin=day_margin,
            night_margin=night_margin,
            full_margin=full_margin,
        )

        product_fee_params.additional_properties = d
        return product_fee_params

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
