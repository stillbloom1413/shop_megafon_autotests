from dataclasses import dataclass
from typing import Optional, List, Union


@dataclass
class FilterDTO:
    filter_type: str
    group: str
    value: Optional[Union[str, int, List[Union[int, str]]]] = None
    boundary: Optional[List[str]] = None
    characteristic: Optional[str] = None
