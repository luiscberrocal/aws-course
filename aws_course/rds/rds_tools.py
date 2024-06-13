from aws_course.core import get_boto3_client_from_environment
from aws_course.rds.schemas import DBInstanceList


def get_instances(user_prefix: str) -> DBInstanceList:
    client = get_boto3_client_from_environment('rds', user_prefix=user_prefix)
    response = client.describe_db_instances()
    instance_list = DBInstanceList(**response)
    return instance_list


if __name__ == '__main__':
    instances = get_instances('ADELANTOS')
    for instance in instances.db_instances:
        print(instance.db_instance_identifier)
        print(instance.engine, instance.engine_version)
        print(instance.db_instance_class)
        print(instance.allocated_storage, "GB")
        print("-" * 80)
