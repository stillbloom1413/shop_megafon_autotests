from dataclasses import dataclass
from typing import Optional


@dataclass
class FilterDTO:
    type: str
    group: str
    value: Optional[str] = None
    min: Optional[str] = None
    max: Optional[str] = None
