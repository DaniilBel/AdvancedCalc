from dataclasses import dataclass


@dataclass(init=True)
class History:
    line: str
    answer: float
    date: str


@dataclass
class HistoryGet:
    line: str
    answer: float
    date: str
