import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContractMaturity")


@attr.s(auto_attribs=True)
class ContractMaturity:
    """
    Attributes:
        product_id (int):
        expiration_month (int):
        expiration_date (datetime.datetime):
        is_front (bool):
        id (Union[Unset, int]):
        first_intent_date (Union[Unset, datetime.datetime]):
        underlying_id (Union[Unset, int]): Underlying
    """

    product_id: int
    expiration_month: int
    expiration_date: datetime.datetime
    is_front: bool
    id: Union[Unset, int] = UNSET
    first_intent_date: Union[Unset, datetime.datetime] = UNSET
    underlying_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        product_id = self.product_id
        expiration_month = self.expiration_month
        expiration_date = self.expiration_date.isoformat()

        is_front = self.is_front
        id = self.id
        first_intent_date: Union[Unset, str] = UNSET
        if not isinstance(self.first_intent_date, Unset):
            first_intent_date = self.first_intent_date.isoformat()

        underlying_id = self.underlying_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "productId": product_id,
                "expirationMonth": expiration_month,
                "expirationDate": expiration_date,
                "isFront": is_front,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if first_intent_date is not UNSET:
            field_dict["firstIntentDate"] = first_intent_date
        if underlying_id is not UNSET:
            field_dict["underlyingId"] = underlying_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        product_id = d.pop("productId")

        expiration_month = d.pop("expirationMonth")

        expiration_date = isoparse(d.pop("expirationDate"))

        is_front = d.pop("isFront")

        id = d.pop("id", UNSET)

        _first_intent_date = d.pop("firstIntentDate", UNSET)
        first_intent_date: Union[Unset, datetime.datetime]
        if isinstance(_first_intent_date, Unset):
            first_intent_date = UNSET
        else:
            first_intent_date = isoparse(_first_intent_date)

        underlying_id = d.pop("underlyingId", UNSET)

        contract_maturity = cls(
            product_id=product_id,
            expiration_month=expiration_month,
            expiration_date=expiration_date,
            is_front=is_front,
            id=id,
            first_intent_date=first_intent_date,
            underlying_id=underlying_id,
        )

        contract_maturity.additional_properties = d
        return contract_maturity

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
