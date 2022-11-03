import unittest
from unittest.mock import patch, mock_open

from src.common import csvutils


class TestCSVUtils(unittest.TestCase):
    def test_it_reads_a_csv(self):
        csv_data = ("name,age\n"
                    "John,32\n"
                    "Anne,31\n")

        expected = [
            {'name': 'John', 'age': '32'},
            {'name': 'Anne', 'age': '31'}
        ]

        with patch("builtins.open", mock_open(read_data=csv_data)):
            result = csvutils.csv_to_rows("fakefile.csv")

        assert result == expected
