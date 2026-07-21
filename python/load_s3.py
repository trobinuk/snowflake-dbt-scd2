import boto3

s3_resource = boto3.resource('s3','us-east-1')


file_name = 'Product_Dim_1.csv'
path = 'raw_data'
bucket_name = 'rtamil-etl-scd2'

s3_bucket = s3_resource.Bucket(name=bucket_name)

s3_bucket.upload_file(
    Filename = file_name,
    Key = path + '/' + file_name
    )


