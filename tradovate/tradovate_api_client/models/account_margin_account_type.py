from enum import Enum


class AccountMarginAccountType(str, Enum):
    HEDGER = "Hedger"
    SPECULATOR = "Speculator"

    def __str__(self) -> str:
        return str(self.value)
