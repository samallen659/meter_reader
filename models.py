from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List


class Fuel(Enum):
    """Possible Fuel type for Octopus API requests"""

    GAS = 1
    ELECTRICITY = 2


@dataclass
class ConsumptionUnit:
    """Single Unit of consumption contained within ConsumptionResponse"""

    consumption: int
    interval_start: datetime
    interval_end: datetime


@dataclass
class ConsumptionResponse:
    """Structure of response from the Octopus API consumption Endpoint"""

    count: int
    next: None | str
    previous: None | str
    results: List[ConsumptionUnit]
