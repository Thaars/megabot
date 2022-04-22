from enum import Enum


class TradovateSubscriptionResponseErrorCode(str, Enum):
    CONFLICTWITHEXISTING = "ConflictWithExisting"
    DOWNGRADENOTALLOWED = "DowngradeNotAllowed"
    INCOMPATIBLECMEMARKETDATASUBSCRIPTIONPLANS = "IncompatibleCMEMarketDataSubscriptionPlans"
    INCORRECTPAYMENTMETHOD = "IncorrectPaymentMethod"
    INSUFFICIENTFUNDS = "InsufficientFunds"
    PAYMENTPROVIDERERROR = "PaymentProviderError"
    PLANDISCONTINUED = "PlanDiscontinued"
    SINGLETRIALONLY = "SingleTrialOnly"
    SUCCESS = "Success"
    UNKNOWNERROR = "UnknownError"

    def __str__(self) -> str:
        return str(self.value)
