import boto3

s3 = boto3.client('s3')

bucket_name = 'is698-lab3c'

file_name = 'myfile.txt'

s3.delete_object(Bucket=bucket_name, Key=file_name)

print(f'File {file_name} has been deleted successfully!')

