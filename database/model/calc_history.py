from dataclasses import dataclass


@dataclass(init=True)
class History:
    line: str
    answer: float
    is_ans_int: bool
    date: str


@dataclass
class HistoryGet:
    line: str
    answer: float
    is_ans_int: bool
    date: str
