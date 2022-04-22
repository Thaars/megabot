from enum import Enum


class ExecutionReportRejectReason(str, Enum):
    ACCOUNTCLOSED = "AccountClosed"
    ADVANCEDTRAILINGSTOPUNSUPPORTED = "AdvancedTrailingStopUnsupported"
    ANOTHERCOMMANDPENDING = "AnotherCommandPending"
    BACKMONTHPROHIBITED = "BackMonthProhibited"
    EXECUTIONPROVIDERNOTCONFIGURED = "ExecutionProviderNotConfigured"
    EXECUTIONPROVIDERUNAVAILABLE = "ExecutionProviderUnavailable"
    INVALIDCONTRACT = "InvalidContract"
    INVALIDPRICE = "InvalidPrice"
    LIQUIDATIONONLY = "LiquidationOnly"
    LIQUIDATIONONLYBEFOREEXPIRATION = "LiquidationOnlyBeforeExpiration"
    MAXORDERQTYISNOTSPECIFIED = "MaxOrderQtyIsNotSpecified"
    MAXORDERQTYLIMITREACHED = "MaxOrderQtyLimitReached"
    MAXPOSLIMITMISCONFIGURED = "MaxPosLimitMisconfigured"
    MAXPOSLIMITREACHED = "MaxPosLimitReached"
    MAXTOTALPOSLIMITREACHED = "MaxTotalPosLimitReached"
    MULTIPLEACCOUNTPLANREQUIRED = "MultipleAccountPlanRequired"
    NOQUOTE = "NoQuote"
    NOTENOUGHLIQUIDITY = "NotEnoughLiquidity"
    OTHEREXECUTIONRELATED = "OtherExecutionRelated"
    PARENTREJECTED = "ParentRejected"
    RISKCHECKTIMEOUT = "RiskCheckTimeout"
    SESSIONCLOSED = "SessionClosed"
    SUCCESS = "Success"
    TOOLATE = "TooLate"
    TRADINGLOCKED = "TradingLocked"
    TRAILINGSTOPNONORDERQTYMODIFY = "TrailingStopNonOrderQtyModify"
    UNAUTHORIZED = "Unauthorized"
    UNKNOWNREASON = "UnknownReason"
    UNSUPPORTED = "Unsupported"

    def __str__(self) -> str:
        return str(self.value)
