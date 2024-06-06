from aws_course.core import get_boto3_client_from_environment
from aws_course.settings import COURSE_FOLDER


def list_buckets():
    s3 = get_boto3_client_from_environment('s3', 'DUMMY_USER')
    response = s3.list_buckets()
    return response['Buckets']


if __name__ == '__main__':
    print(list_buckets())
    s3 = get_boto3_client_from_environment('s3', 'DUMMY_USER')
    bucket_name = "aws-lucho-course-v001"

    file_to_upload = COURSE_FOLDER / "s3" / "coffee.jpg"
    print(file_to_upload, file_to_upload.exists())

    s3.upload_file(str(file_to_upload), bucket_name, "coffee.jpg")
    print(f"File {file_to_upload} uploaded")
