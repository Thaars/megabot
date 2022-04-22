from enum import Enum


class FillAction(str, Enum):
    BUY = "Buy"
    SELL = "Sell"

    def __str__(self) -> str:
        return str(self.value)
