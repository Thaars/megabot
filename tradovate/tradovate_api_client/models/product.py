from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.product_price_format_type import ProductPriceFormatType
from ..models.product_product_type import ProductProductType
from ..models.product_status import ProductStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Product")


@attr.s(auto_attribs=True)
class Product:
    """
    Attributes:
        name (str):
        currency_id (int):
        product_type (ProductProductType): CommonStock, Continuous, Cryptocurrency, Futures, MarketInternals, Options,
            Spread
        description (str):
        exchange_id (int):
        contract_group_id (int):
        status (ProductStatus): Inactive, Locked, ReadyForContracts, ReadyToTrade, Verified
        value_per_point (float):
        price_format_type (ProductPriceFormatType): Decimal, Fractional
        price_format (int):
        tick_size (float): Product Tick Size
        id (Union[Unset, int]):
        risk_discount_contract_group_id (Union[Unset, int]):
        months (Union[Unset, str]):
        is_secured (Union[Unset, bool]):
    """

    name: str
    currency_id: int
    product_type: ProductProductType
    description: str
    exchange_id: int
    contract_group_id: int
    status: ProductStatus
    value_per_point: float
    price_format_type: ProductPriceFormatType
    price_format: int
    tick_size: float
    id: Union[Unset, int] = UNSET
    risk_discount_contract_group_id: Union[Unset, int] = UNSET
    months: Union[Unset, str] = UNSET
    is_secured: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        currency_id = self.currency_id
        product_type = self.product_type.value

        description = self.description
        exchange_id = self.exchange_id
        contract_group_id = self.contract_group_id
        status = self.status.value

        value_per_point = self.value_per_point
        price_format_type = self.price_format_type.value

        price_format = self.price_format
        tick_size = self.tick_size
        id = self.id
        risk_discount_contract_group_id = self.risk_discount_contract_group_id
        months = self.months
        is_secured = self.is_secured

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "currencyId": currency_id,
                "productType": product_type,
                "description": description,
                "exchangeId": exchange_id,
                "contractGroupId": contract_group_id,
                "status": status,
                "valuePerPoint": value_per_point,
                "priceFormatType": price_format_type,
                "priceFormat": price_format,
                "tickSize": tick_size,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if risk_discount_contract_group_id is not UNSET:
            field_dict["riskDiscountContractGroupId"] = risk_discount_contract_group_id
        if months is not UNSET:
            field_dict["months"] = months
        if is_secured is not UNSET:
            field_dict["isSecured"] = is_secured

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        currency_id = d.pop("currencyId")

        product_type = ProductProductType(d.pop("productType"))

        description = d.pop("description")

        exchange_id = d.pop("exchangeId")

        contract_group_id = d.pop("contractGroupId")

        status = ProductStatus(d.pop("status"))

        value_per_point = d.pop("valuePerPoint")

        price_format_type = ProductPriceFormatType(d.pop("priceFormatType"))

        price_format = d.pop("priceFormat")

        tick_size = d.pop("tickSize")

        id = d.pop("id", UNSET)

        risk_discount_contract_group_id = d.pop("riskDiscountContractGroupId", UNSET)

        months = d.pop("months", UNSET)

        is_secured = d.pop("isSecured", UNSET)

        product = cls(
            name=name,
            currency_id=currency_id,
            product_type=product_type,
            description=description,
            exchange_id=exchange_id,
            contract_group_id=contract_group_id,
            status=status,
            value_per_point=value_per_point,
            price_format_type=price_format_type,
            price_format=price_format,
            tick_size=tick_size,
            id=id,
            risk_discount_contract_group_id=risk_discount_contract_group_id,
            months=months,
            is_secured=is_secured,
        )

        product.additional_properties = d
        return product

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
