import boto3
from botocore.exceptions import ClientError

# 1. List all files in an S3 bucket
def list_s3_files(bucket_name):
    s3 = boto3.client('s3')
    print(f"Files in bucket: {bucket_name}")
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            for obj in response['Contents']:
                print(f" - {obj['Key']} ({obj['Size']} bytes)")
        else:
            print("Bucket is empty.")
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == "AccessDenied":
            print(f"Access denied. Make sure your IAM user/role has 's3:ListBucket' and 's3:GetObject' for bucket '{bucket_name}'.")
        else:
            print("Error:", e)

# 2. Create a DynamoDB Table
def create_dynamodb_table(table_name):
    dynamodb = boto3.client('dynamodb')
    try:
        print(f"Creating DynamoDB table: {table_name}")
        response = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
            ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
        )
        print("Waiting for table to become active...")
        waiter = dynamodb.get_waiter('table_exists')
        waiter.wait(TableName=table_name)
        print("Table created and active!")
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceInUseException':
            print(f"Table '{table_name}' already exists.")
        else:
            print("Error:", e)

# 3. Insert an item into DynamoDB
def insert_item(table_name, item):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    try:
        table.put_item(Item=item)
        print(f"Inserted item into {table_name}: {item}")
    except ClientError as e:
        print("Error inserting item:", e)

# Run all tasks
if __name__ == "__main__":
    bucket_name = 'is698-homework3-task2'  
    table_name = 'MyDemoTable'
    sample_item = {
        'id': '001',
        'name': 'First entry',
        'person': 'Aswin', 
        'created': '2025-04-21'
    }

    list_s3_files(bucket_name)
    create_dynamodb_table(table_name)
    insert_item(table_name, sample_item)