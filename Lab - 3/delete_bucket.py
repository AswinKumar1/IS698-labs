import boto3

s3 = boto3.client('s3')

bucket_name = 'is698-lab3c'

s3.delete_bucket(Bucket=bucket_name)

print(f'Bucket {bucket_name} has been deleted successfully!')


