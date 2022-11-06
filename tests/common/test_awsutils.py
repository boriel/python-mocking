import unittest
from io import BytesIO

from typing import Any
from unittest.mock import patch

from src.common import awsutils


def mock_get_object_s3(
    botocore_obj: Any, command: str, obj: dict[str, Any]
) -> dict[str, Any]:
    """
    Mocks S3 GetObject call
    """
    if command == "GetObject":
        if obj.get("Bucket") != "my_bucket":
            raise ValueError(f"Invalid bucket {obj.get('Bucket')}")
        if obj.get("Key") != "path/my_file":
            raise ValueError(f"Invalid obj key {obj.get('Key')}")

        return {"Body": BytesIO(b"Fake object content in S3")}

    raise ValueError(f"Unexpected command '{command}")


class TestAWSUtils(unittest.TestCase):
    @patch("botocore.client.BaseClient._make_api_call", new=mock_get_object_s3)
    def test_read_s3_object(self):
        expected = b"Fake object content in S3"
        result = awsutils.read_s3_object("s3://my_bucket/path/my_file")

        self.assertEqual(result, expected)
