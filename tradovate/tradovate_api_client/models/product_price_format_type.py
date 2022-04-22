from enum import Enum


class ProductPriceFormatType(str, Enum):
    DECIMAL = "Decimal"
    FRACTIONAL = "Fractional"

    def __str__(self) -> str:
        return str(self.value)
