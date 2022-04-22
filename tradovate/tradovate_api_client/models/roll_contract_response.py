from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.contract import Contract
from ..types import UNSET, Unset

T = TypeVar("T", bound="RollContractResponse")


@attr.s(auto_attribs=True)
class RollContractResponse:
    """
    Attributes:
        error_text (Union[Unset, str]): Non-empty if the request failed
        contract (Union[Unset, Contract]):
    """

    error_text: Union[Unset, str] = UNSET
    contract: Union[Unset, Contract] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_text = self.error_text
        contract: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contract, Unset):
            contract = self.contract.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if contract is not UNSET:
            field_dict["contract"] = contract

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error_text = d.pop("errorText", UNSET)

        _contract = d.pop("contract", UNSET)
        contract: Union[Unset, Contract]
        if isinstance(_contract, Unset):
            contract = UNSET
        else:
            contract = Contract.from_dict(_contract)

        roll_contract_response = cls(
            error_text=error_text,
            contract=contract,
        )

        roll_contract_response.additional_properties = d
        return roll_contract_response

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
