import unittest
from unittest.mock import patch, Mock
import datetime

from src.common import timestamp


class TestTimestamp(unittest.TestCase):
    _CURRENT_DATETIME = datetime.datetime(2022, 11, 7, 12, 13, 14)

    # BAD approach
    # @patch("src.common.timestamp.datetime.utcnow", return_value=_CURRENT_DATETIME)
    # def test_it_sets_timestamp(self):
    #     expected = {"username": "john", "timestamp": self._CURRENT_DATETIME.isoformat()}
    #     result = timestamp.add_timestamp({"username": "john"})
    #     assert result == expected

    @patch.object(timestamp, "datetime", Mock(wraps=datetime.datetime))
    def test_it_sets_timestamp(self):
        with patch("src.common.timestamp.datetime.utcnow", return_value=self._CURRENT_DATETIME) as ts:
            expected = {"username": "john", "timestamp": ts().isoformat()}
            result = timestamp.add_timestamp({"username": "john"})
            assert result == expected


if __name__ == '__main__':
    unittest.main()
