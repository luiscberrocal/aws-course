from aws_course.core import get_boto3_client_from_environment


def list_buckets():
    s3 = get_boto3_client_from_environment('s3', 'DUMMY_USER')
    response = s3.list_buckets()
    return response['Buckets']



if __name__ == '__main__':
    print(list_buckets())
