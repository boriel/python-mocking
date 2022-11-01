from datetime import datetime

from typing import Any


def add_timestamp(response: dict[str, Any]) -> dict[str, Any]:
    return {**response, "timestamp": datetime.utcnow().isoformat()}
