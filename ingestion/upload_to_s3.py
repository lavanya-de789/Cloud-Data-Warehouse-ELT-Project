import boto3

s3=boto3.client(
's3'
)

s3.upload_file(
'data/customers.csv',
'my-data-bucket',
'customers.csv'
)

print(
'uploaded successfully'
)
