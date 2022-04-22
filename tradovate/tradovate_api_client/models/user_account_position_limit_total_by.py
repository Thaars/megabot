from enum import Enum


class UserAccountPositionLimitTotalBy(str, Enum):
    CONTRACT = "Contract"
    CONTRACTGROUP = "ContractGroup"
    DISCOUNTGROUP = "DiscountGroup"
    EXCHANGE = "Exchange"
    OVERALL = "Overall"
    PRODUCT = "Product"
    PRODUCTTYPE = "ProductType"

    def __str__(self) -> str:
        return str(self.value)
