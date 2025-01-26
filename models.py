from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List


class Fuel(Enum):
    GAS = 1
    ELECTRICITY = 2


@dataclass
class ConsumptionUnit:
    consumption: int
    interval_start: datetime
    interval_end: datetime


@dataclass
class ConsumptionResponse:
    count: int
    next: None | str
    previous: None | str
    results: List[ConsumptionUnit]
