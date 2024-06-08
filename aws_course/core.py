import os
from pathlib import Path

import boto3
from dotenv import load_dotenv


def load_environment_variables(environment_filename: str, source_folder_name: str = ".envs"):
    def find_envs_folder(current_dir: Path):
        env_folder = current_dir / source_folder_name
        if env_folder.exists():
            return env_folder
        else:
            return find_envs_folder(current_dir.parent)

    environment_folder = find_envs_folder(Path(__file__).parent)
    environment_file = environment_folder / environment_filename
    # print(f'{environment_file} {environment_file.exists()}')
    load_dotenv(dotenv_path=environment_file)


def get_boto3_client(service_name: str, region_name: str, access_key: str, secret_key: str):
    return boto3.client(service_name, region_name=region_name
                        , aws_access_key_id=access_key
                        , aws_secret_access_key=secret_key)


def get_boto3_client_from_environment(service_name: str, user_prefix: str):
    access_key_name = f'{user_prefix}_AWS_ACCESS_KEY'
    secret_key_name = f'{user_prefix}_AWS_SECRET_ACCESS_KEY'
    load_environment_variables("AWS_environment.txt")
    key = os.getenv(access_key_name)
    secret = os.getenv(secret_key_name)
    return get_boto3_client(service_name, 'us-east-2', access_key=key, secret_key=secret)
