from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.user_account_position_limit_product_type import UserAccountPositionLimitProductType
from ..models.user_account_position_limit_product_verification_status import (
    UserAccountPositionLimitProductVerificationStatus,
)
from ..models.user_account_position_limit_total_by import UserAccountPositionLimitTotalBy
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAccountPositionLimit")


@attr.s(auto_attribs=True)
class UserAccountPositionLimit:
    """
    Attributes:
        active (bool):
        total_by (UserAccountPositionLimitTotalBy): Contract, ContractGroup, DiscountGroup, Exchange, Overall, Product,
            ProductType
        account_id (int):
        id (Union[Unset, int]):
        contract_id (Union[Unset, int]):
        product_id (Union[Unset, int]):
        exchange_id (Union[Unset, int]):
        product_type (Union[Unset, UserAccountPositionLimitProductType]): CommonStock, Continuous, Cryptocurrency,
            Futures, MarketInternals, Options, Spread
        risk_discount_contract_group_id (Union[Unset, int]):
        product_verification_status (Union[Unset, UserAccountPositionLimitProductVerificationStatus]): Inactive, Locked,
            ReadyForContracts, ReadyToTrade, Verified
        contract_group_id (Union[Unset, int]):
        risk_time_period_id (Union[Unset, int]):
        short_limit (Union[Unset, int]):
        long_limit (Union[Unset, int]):
        exposed_limit (Union[Unset, int]):
        description (Union[Unset, str]):
    """

    active: bool
    total_by: UserAccountPositionLimitTotalBy
    account_id: int
    id: Union[Unset, int] = UNSET
    contract_id: Union[Unset, int] = UNSET
    product_id: Union[Unset, int] = UNSET
    exchange_id: Union[Unset, int] = UNSET
    product_type: Union[Unset, UserAccountPositionLimitProductType] = UNSET
    risk_discount_contract_group_id: Union[Unset, int] = UNSET
    product_verification_status: Union[Unset, UserAccountPositionLimitProductVerificationStatus] = UNSET
    contract_group_id: Union[Unset, int] = UNSET
    risk_time_period_id: Union[Unset, int] = UNSET
    short_limit: Union[Unset, int] = UNSET
    long_limit: Union[Unset, int] = UNSET
    exposed_limit: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active = self.active
        total_by = self.total_by.value

        account_id = self.account_id
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
        risk_time_period_id = self.risk_time_period_id
        short_limit = self.short_limit
        long_limit = self.long_limit
        exposed_limit = self.exposed_limit
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
                "totalBy": total_by,
                "accountId": account_id,
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
        if risk_time_period_id is not UNSET:
            field_dict["riskTimePeriodId"] = risk_time_period_id
        if short_limit is not UNSET:
            field_dict["shortLimit"] = short_limit
        if long_limit is not UNSET:
            field_dict["longLimit"] = long_limit
        if exposed_limit is not UNSET:
            field_dict["exposedLimit"] = exposed_limit
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        active = d.pop("active")

        total_by = UserAccountPositionLimitTotalBy(d.pop("totalBy"))

        account_id = d.pop("accountId")

        id = d.pop("id", UNSET)

        contract_id = d.pop("contractId", UNSET)

        product_id = d.pop("productId", UNSET)

        exchange_id = d.pop("exchangeId", UNSET)

        _product_type = d.pop("productType", UNSET)
        product_type: Union[Unset, UserAccountPositionLimitProductType]
        if isinstance(_product_type, Unset):
            product_type = UNSET
        else:
            product_type = UserAccountPositionLimitProductType(_product_type)

        risk_discount_contract_group_id = d.pop("riskDiscountContractGroupId", UNSET)

        _product_verification_status = d.pop("productVerificationStatus", UNSET)
        product_verification_status: Union[Unset, UserAccountPositionLimitProductVerificationStatus]
        if isinstance(_product_verification_status, Unset):
            product_verification_status = UNSET
        else:
            product_verification_status = UserAccountPositionLimitProductVerificationStatus(
                _product_verification_status
            )

        contract_group_id = d.pop("contractGroupId", UNSET)

        risk_time_period_id = d.pop("riskTimePeriodId", UNSET)

        short_limit = d.pop("shortLimit", UNSET)

        long_limit = d.pop("longLimit", UNSET)

        exposed_limit = d.pop("exposedLimit", UNSET)

        description = d.pop("description", UNSET)

        user_account_position_limit = cls(
            active=active,
            total_by=total_by,
            account_id=account_id,
            id=id,
            contract_id=contract_id,
            product_id=product_id,
            exchange_id=exchange_id,
            product_type=product_type,
            risk_discount_contract_group_id=risk_discount_contract_group_id,
            product_verification_status=product_verification_status,
            contract_group_id=contract_group_id,
            risk_time_period_id=risk_time_period_id,
            short_limit=short_limit,
            long_limit=long_limit,
            exposed_limit=exposed_limit,
            description=description,
        )

        user_account_position_limit.additional_properties = d
        return user_account_position_limit

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
