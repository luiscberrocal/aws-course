from pathlib import Path
from typing import List, Dict, Any

import boto3

from aws_course.core import get_boto3_client_from_environment
from aws_course.settings import COURSE_FOLDER


def get_content_type(file: Path):
    ext = file.suffix.lower()
    if ext == '.js':
        return 'application/javascript'
    elif ext == '.html':
        return 'text/html'
    elif ext == '.txt':
        return 'text/plain'
    elif ext == '.json':
        return 'application/json'
    elif ext == '.ico':
        return 'image/x-icon'
    elif ext == '.svg':
        return 'image/svg+xml'
    elif ext == '.css':
        return 'text/css'
    elif ext in ['.jpg', '.jpeg']:
        return 'image/jpeg'
    elif ext == '.png':
        return 'image/png'
    elif ext == '.webp':
        return 'image/webp'
    elif ext == '.map':
        return 'binary/octet-stream'


def list_buckets(user_prefix='DUMMY_USER') -> List[Dict[str, Any]]:
    """ List all buckets in the account.

    This function expects environment variables to be set in the following way:
    DUMMY_USER_AWS_ACCESS_KEY=xxxxxxxxxxxxxxxxxxxx
    DUMMY_USER_AWS_SECRET_ACCESS_KEY=XXXXXXXXXXXXXXXXXXXX/XXXXXXXXXXXXXXXXXXX
    """
    s3_client = get_boto3_client_from_environment('s3', user_prefix)
    response = s3_client.list_buckets()
    return response['Buckets']


def update_docker_file_versions(client: 'boto3.client', bucket_name: str):
    docker_html = COURSE_FOLDER / "s3" / "docker.html"

    client.upload_file(str(docker_html), bucket_name, "index.html", ExtraArgs={'ContentType': 'text/html'})


if __name__ == '__main__':
    print(list_buckets())
    client = get_boto3_client_from_environment('s3', 'DUMMY_USER')
    bucket = "aws-lucho-course-v002"

    # file_to_upload = COURSE_FOLDER / "s3" / "coffee.jpg"
    # print(file_to_upload, file_to_upload.exists())

    # s3.upload_file(str(file_to_upload), bucket_name, "coffee.jpg")
    # print(f"File {file_to_upload} uploaded")
    # http://aws-lucho-course-v002.s3-website.us-east-2.amazonaws.com
    update_docker_file_versions(client, bucket)
