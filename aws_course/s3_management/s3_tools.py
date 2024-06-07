import boto3

from aws_course.core import get_boto3_client_from_environment
from aws_course.settings import COURSE_FOLDER


def list_buckets():
    s3 = get_boto3_client_from_environment('s3', 'DUMMY_USER')
    response = s3.list_buckets()
    return response['Buckets']


def update_docker_file_versions(client: 'boto3.client', bucket_name: str):
    docker_html = COURSE_FOLDER / "s3" / "docker.html"

    client.upload_file(str(docker_html), bucket_name, "index.html", ExtraArgs={'ContentType':'text/html'})


if __name__ == '__main__':
    print(list_buckets())
    s3 = get_boto3_client_from_environment('s3', 'DUMMY_USER')
    bucket_name = "aws-lucho-course-v002"

    # file_to_upload = COURSE_FOLDER / "s3" / "coffee.jpg"
    # print(file_to_upload, file_to_upload.exists())

    # s3.upload_file(str(file_to_upload), bucket_name, "coffee.jpg")
    # print(f"File {file_to_upload} uploaded")
# http://aws-lucho-course-v002.s3-website.us-east-2.amazonaws.com
    update_docker_file_versions(s3, bucket_name)
