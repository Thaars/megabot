from enum import Enum


class ProductProductType(str, Enum):
    COMMONSTOCK = "CommonStock"
    CONTINUOUS = "Continuous"
    CRYPTOCURRENCY = "Cryptocurrency"
    FUTURES = "Futures"
    MARKETINTERNALS = "MarketInternals"
    OPTIONS = "Options"
    SPREAD = "Spread"

    def __str__(self) -> str:
        return str(self.value)
