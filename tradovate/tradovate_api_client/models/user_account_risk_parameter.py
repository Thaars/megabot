from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.user_account_risk_parameter_product_type import UserAccountRiskParameterProductType
from ..models.user_account_risk_parameter_product_verification_status import (
    UserAccountRiskParameterProductVerificationStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAccountRiskParameter")


@attr.s(auto_attribs=True)
class UserAccountRiskParameter:
    """
    Attributes:
        user_account_position_limit_id (int):
        id (Union[Unset, int]):
        contract_id (Union[Unset, int]):
        product_id (Union[Unset, int]):
        exchange_id (Union[Unset, int]):
        product_type (Union[Unset, UserAccountRiskParameterProductType]): CommonStock, Continuous, Cryptocurrency,
            Futures, MarketInternals, Options, Spread
        risk_discount_contract_group_id (Union[Unset, int]):
        product_verification_status (Union[Unset, UserAccountRiskParameterProductVerificationStatus]): Inactive, Locked,
            ReadyForContracts, ReadyToTrade, Verified
        contract_group_id (Union[Unset, int]):
        max_opening_order_qty (Union[Unset, int]):
        max_closing_order_qty (Union[Unset, int]):
        max_back_month (Union[Unset, int]):
        pre_expiration_days (Union[Unset, int]):
        margin_percentage (Union[Unset, float]):
        margin_dollar_value (Union[Unset, float]):
        hard_limit (Union[Unset, bool]):
    """

    user_account_position_limit_id: int
    id: Union[Unset, int] = UNSET
    contract_id: Union[Unset, int] = UNSET
    product_id: Union[Unset, int] = UNSET
    exchange_id: Union[Unset, int] = UNSET
    product_type: Union[Unset, UserAccountRiskParameterProductType] = UNSET
    risk_discount_contract_group_id: Union[Unset, int] = UNSET
    product_verification_status: Union[Unset, UserAccountRiskParameterProductVerificationStatus] = UNSET
    contract_group_id: Union[Unset, int] = UNSET
    max_opening_order_qty: Union[Unset, int] = UNSET
    max_closing_order_qty: Union[Unset, int] = UNSET
    max_back_month: Union[Unset, int] = UNSET
    pre_expiration_days: Union[Unset, int] = UNSET
    margin_percentage: Union[Unset, float] = UNSET
    margin_dollar_value: Union[Unset, float] = UNSET
    hard_limit: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_account_position_limit_id = self.user_account_position_limit_id
        id = self.id
        contract_id = self.contract_id
        product_id = self.product_id
        exchange_id = self.exchange_id
        product_type: Union[Unset, str] = UNSET
        if not isinstance(self.product_type, Unset):
            product_type = self.product_type.value

        risk_discount_contract_group_id = self.risk_discount_contract_group_id
        product_verification_status: Union[Unset, str] = UNSET
        if not isinstance(self.product_verification_status, Unset):
            product_verification_status = self.product_verification_status.value

        contract_group_id = self.contract_group_id
        max_opening_order_qty = self.max_opening_order_qty
        max_closing_order_qty = self.max_closing_order_qty
        max_back_month = self.max_back_month
        pre_expiration_days = self.pre_expiration_days
        margin_percentage = self.margin_percentage
        margin_dollar_value = self.margin_dollar_value
        hard_limit = self.hard_limit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userAccountPositionLimitId": user_account_position_limit_id,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if contract_id is not UNSET:
            field_dict["contractId"] = contract_id
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if exchange_id is not UNSET:
            field_dict["exchangeId"] = exchange_id
        if product_type is not UNSET:
            field_dict["productType"] = product_type
        if risk_discount_contract_group_id is not UNSET:
            field_dict["riskDiscountContractGroupId"] = risk_discount_contract_group_id
        if product_verification_status is not UNSET:
            field_dict["productVerificationStatus"] = product_verification_status
        if contract_group_id is not UNSET:
            field_dict["contractGroupId"] = contract_group_id
        if max_opening_order_qty is not UNSET:
            field_dict["maxOpeningOrderQty"] = max_opening_order_qty
        if max_closing_order_qty is not UNSET:
            field_dict["maxClosingOrderQty"] = max_closing_order_qty
        if max_back_month is not UNSET:
            field_dict["maxBackMonth"] = max_back_month
        if pre_expiration_days is not UNSET:
            field_dict["preExpirationDays"] = pre_expiration_days
        if margin_percentage is not UNSET:
            field_dict["marginPercentage"] = margin_percentage
        if margin_dollar_value is not UNSET:
            field_dict["marginDollarValue"] = margin_dollar_value
        if hard_limit is not UNSET:
            field_dict["hardLimit"] = hard_limit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_account_position_limit_id = d.pop("userAccountPositionLimitId")

        id = d.pop("id", UNSET)

        contract_id = d.pop("contractId", UNSET)

        product_id = d.pop("productId", UNSET)

        exchange_id = d.pop("exchangeId", UNSET)

        _product_type = d.pop("productType", UNSET)
        product_type: Union[Unset, UserAccountRiskParameterProductType]
        if isinstance(_product_type, Unset):
            product_type = UNSET
        else:
            product_type = UserAccountRiskParameterProductType(_product_type)

        risk_discount_contract_group_id = d.pop("riskDiscountContractGroupId", UNSET)

        _product_verification_status = d.pop("productVerificationStatus", UNSET)
        product_verification_status: Union[Unset, UserAccountRiskParameterProductVerificationStatus]
        if isinstance(_product_verification_status, Unset):
            product_verification_status = UNSET
        else:
            product_verification_status = UserAccountRiskParameterProductVerificationStatus(
                _product_verification_status
            )

        contract_group_id = d.pop("contractGroupId", UNSET)

        max_opening_order_qty = d.pop("maxOpeningOrderQty", UNSET)

        max_closing_order_qty = d.pop("maxClosingOrderQty", UNSET)

        max_back_month = d.pop("maxBackMonth", UNSET)

        pre_expiration_days = d.pop("preExpirationDays", UNSET)

        margin_percentage = d.pop("marginPercentage", UNSET)

        margin_dollar_value = d.pop("marginDollarValue", UNSET)

        hard_limit = d.pop("hardLimit", UNSET)

        user_account_risk_parameter = cls(
            user_account_position_limit_id=user_account_position_limit_id,
            id=id,
            contract_id=contract_id,
            product_id=product_id,
            exchange_id=exchange_id,
            product_type=product_type,
            risk_discount_contract_group_id=risk_discount_contract_group_id,
            product_verification_status=product_verification_status,
            contract_group_id=contract_group_id,
            max_opening_order_qty=max_opening_order_qty,
            max_closing_order_qty=max_closing_order_qty,
            max_back_month=max_back_month,
            pre_expiration_days=pre_expiration_days,
            margin_percentage=margin_percentage,
            margin_dollar_value=margin_dollar_value,
            hard_limit=hard_limit,
        )

        user_account_risk_parameter.additional_properties = d
        return user_account_risk_parameter

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
