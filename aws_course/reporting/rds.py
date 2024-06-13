from pathlib import Path

from aws_course.rds.schemas import DBInstanceList


def write_to_csv(filename: Path, rds_instance_list: DBInstanceList):
    with open(filename, 'w') as file:
        file.write("Environment,DBInstanceIdentifier,Engine,EngineVersion,DBInstanceClass,AllocatedStorage\n")
        for instance in rds_instance_list.db_instances:
            environment = "UNKNOWN"
            if 'internal' in instance.db_instance_identifier:
                environment = 'STAGING'
            elif 'production' in instance.db_instance_identifier:
                environment = 'PRODUCTION'
            file.write(f"{environment},{instance.db_instance_identifier},{instance.engine},{instance.engine_version},{instance.db_instance_class},{instance.allocated_storage}\n")
