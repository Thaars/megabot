from enum import Enum


class OrderAction(str, Enum):
    BUY = "Buy"
    SELL = "Sell"

    def __str__(self) -> str:
        return str(self.value)
