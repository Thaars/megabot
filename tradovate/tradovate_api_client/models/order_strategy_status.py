from enum import Enum


class OrderStrategyStatus(str, Enum):
    ACTIVESTRATEGY = "ActiveStrategy"
    EXECUTIONFAILED = "ExecutionFailed"
    EXECUTIONFINISHED = "ExecutionFinished"
    EXECUTIONINTERRUPTED = "ExecutionInterrupted"
    INACTIVESTRATEGY = "InactiveStrategy"
    NOTENOUGHLIQUIDITY = "NotEnoughLiquidity"
    STOPPEDBYUSER = "StoppedByUser"

    def __str__(self) -> str:
        return str(self.value)
