from enum import Enum


class AccountAccountType(str, Enum):
    CUSTOMER = "Customer"
    GIVEUP = "Giveup"
    HOUSE = "House"
    OMNIBUS = "Omnibus"
    WASH = "Wash"

    def __str__(self) -> str:
        return str(self.value)
