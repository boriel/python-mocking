import io

import boto3


def read_s3_object(s3_path: str) -> bytes:
    """ This function returns the content of an S3 obj as bytes,
    given it's s3:// URI
    """
    if not s3_path.startswith("s3://"):
        raise ValueError(f"Invalid S3 Uri {s3_path}")

    s3_path = s3_path.replace("s3://", "", 1)
    bucket, obj_key = s3_path.split("/", 1)

    s3_client = boto3.client("s3")

    result = s3_client.get_object(
        Bucket=bucket,
        Key=obj_key
    )

    return result.get("Body", io.BytesIO()).read()

