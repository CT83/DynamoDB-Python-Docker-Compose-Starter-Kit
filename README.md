# DynamoDB-Python-Docker-Compose-Starter-Kit
A Docker and Docker Compose starter kit to help you get started with AWS DynamoDB quickly.

There are 2 modes in which you can run the `app.py` in.

### 1. Local DynamoDB Mode - 
Where a Local instance of DynamoDB is spun up using, Docker and Amazon's Official Local DynamoDB Image - all the database
operations are then performed on this local instance.

### 2. AWS DynamoDB Mode 
Here, the `app.py` will connect to the AWS DyanamoDB Instance, this is how your code might run in the production.
In this mode you are expected to 
1. create a Python Virtual Environment 
2. Do `pip install -r requirements.txt`
3. Create an `.env` file with your AWS Credentials, like `example.env`.  
4. Replace *docker* with *aws* in the env-config.yml
3. Run using `python app.py` 