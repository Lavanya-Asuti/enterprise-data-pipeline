import boto3

# Step 1: Connect to S3
s3 = boto3.client('s3')

# Step 2: Upload file
s3.upload_file(
    "data/raw/transaction.csv",   # local file path
    "banking-raw-data-bucket-lav",      # bucket name
    "transaction.csv"              # file name in S3
)

print("Upload successful!")