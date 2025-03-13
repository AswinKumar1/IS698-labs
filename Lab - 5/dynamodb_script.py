import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')

table.put_item(Item={
	'studentID': 'S002',
	'Name': 'Kush Patel',
	'Age': 22,
	'Department': 'Information Systems'
})

#print(f'Inserted student details')

response = table.get_item(Key={'studentID': 'S002'})
print(response['Item'])


