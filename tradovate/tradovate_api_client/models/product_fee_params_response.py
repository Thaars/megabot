from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.product_fee_params import ProductFeeParams

T = TypeVar("T", bound="ProductFeeParamsResponse")


@attr.s(auto_attribs=True)
class ProductFeeParamsResponse:
    """
    Attributes:
        params (List[ProductFeeParams]):
    """

    params: List[ProductFeeParams]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        params = []
        for params_item_data in self.params:
            params_item = params_item_data.to_dict()

            params.append(params_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "params": params,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        params = []
        _params = d.pop("params")
        for params_item_data in _params:
            params_item = ProductFeeParams.from_dict(params_item_data)

            params.append(params_item)

        product_fee_params_response = cls(
            params=params,
        )

        product_fee_params_response.additional_properties = d
        return product_fee_params_response

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
