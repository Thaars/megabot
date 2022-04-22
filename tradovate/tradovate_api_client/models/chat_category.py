from enum import Enum


class ChatCategory(str, Enum):
    SUPPORT = "Support"
    TRADEDESK = "TradeDesk"

    def __str__(self) -> str:
        return str(self.value)
