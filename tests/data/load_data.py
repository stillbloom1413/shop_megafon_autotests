import json
from pathlib import Path


def load_data(query, num=None):
    current_dir = Path(__file__).resolve().parent
    data_file = current_dir / "search_queries.json"
    with open(data_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    result = data[query]

    if num is not None:
        return result[num]

    return result
