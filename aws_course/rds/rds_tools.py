from pathlib import Path

from aws_course.core import get_boto3_client_from_environment
from aws_course.rds.schemas import DBInstanceList
from aws_course.reporting.rds import write_to_csv


def get_instances(user_prefix: str) -> DBInstanceList:
    client = get_boto3_client_from_environment('rds', user_prefix=user_prefix)
    response = client.describe_db_instances()
    instance_list = DBInstanceList(**response)
    return instance_list


if __name__ == '__main__':
    instances = get_instances('ADELANTOS')
    for i, instance in enumerate(instances.db_instances, 1):
        print(i, instance.db_instance_identifier)
        print(instance.engine, instance.engine_version)
        print(instance.db_instance_class, instance.allocated_storage, "GB")
        # d = instance.model_dump(exclude_none=True)
        # print(d)
        print("-" * 80)

        write_to_csv(Path("../../output/rds_instances.csv"), instances)
