from enum import Enum


class OrderVersionOrderType(str, Enum):
    LIMIT = "Limit"
    MIT = "MIT"
    MARKET = "Market"
    QTS = "QTS"
    STOP = "Stop"
    STOPLIMIT = "StopLimit"
    TRAILINGSTOP = "TrailingStop"
    TRAILINGSTOPLIMIT = "TrailingStopLimit"

    def __str__(self) -> str:
        return str(self.value)
