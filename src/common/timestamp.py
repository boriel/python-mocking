from datetime import datetime

from typing import Any


def add_timestamp(response: dict[str, Any]) -> dict[str, Any]:
    """ Simple function that returns a copy of a dictionary with en extra "timestamp" which is
    the current date time (UTC) in ISO 8601 format.
    """
    return {**response, "timestamp": datetime.utcnow().isoformat()}
