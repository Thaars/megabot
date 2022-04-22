from enum import Enum


class PostChatMessageCategory(str, Enum):
    SUPPORT = "Support"
    TRADEDESK = "TradeDesk"

    def __str__(self) -> str:
        return str(self.value)
