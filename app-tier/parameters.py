# import boto3
# import requests

# ssm = boto3.client('ssm')

# master_username = ssm.get_parameter(
#     Name='master_username',
#     WithDecryption=True
# )["Parameter"]["Value"]

# db_password = ssm.get_parameter(
#     Name='db_password',
#     WithDecryption=True
# )["Parameter"]["Value"]

# endpoint = ssm.get_parameter(
#     Name='endpoint',
#     WithDecryption=True
# )["Parameter"]["Value"]

# db_instance_name = ssm.get_parameter(
#     Name='db_instance_name',
#     WithDecryption=True
# )["Parameter"]["Value"]


# if __name__ == "__main__":
#     print(master_username, db_password, endpoint, db_instance_name)

master_username = "admin" 
db_password = "admin12345"
db_instance_name = "userDB"
endpoint = "kubecounty-database-instance-1.cfglxeexdxex.eu-west-1.rds.amazonaws.com"