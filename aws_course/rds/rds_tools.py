from aws_course.core import get_boto3_client_from_environment


def main():
    client = get_boto3_client_from_environment('rds', 'DUMMY_USER')
    response = client.describe_db_instances()
    print(response)
    # FIXME Delete ------------------------------
    var_name = 'response'
    var_value = eval(var_name)
    from pathlib import Path
    import json
    file = Path(__name__).parent / f'__{var_name}.json'
    with open(file, 'w') as f:
        json.dump(var_value, f, indent=4, default=str)
    print(f'>>>> Saved file {file}')
    # ---------------------------------------


if __name__ == '__main__':
    main()
