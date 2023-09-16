from dataclasses import dataclass


@dataclass(init=False)
class History:
    line: str
    answer: float


@dataclass
class History_get:
    line: str
    answer: float
