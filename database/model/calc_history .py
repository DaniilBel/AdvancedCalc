from dataclasses import dataclass


@dataclass(init=False)
class History:
    line: str
    answer: int


@dataclass
class History_get:
    line: str
    answer: int
