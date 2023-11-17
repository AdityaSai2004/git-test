import os
import boto3
from git import Repo

# AWS credentials and SageMaker configuration
aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'
region_name = 'YOUR_REGION'
sagemaker_endpoint = 'YOUR_SAGEMAKER_ENDPOINT'

# Git SSH key configuration
ssh_key_path = '/path/to/your/private/key'  # Replace with the path to your private key
git_repo_url = 'git@github.com:your-username/your-repo.git'  # Replace with your Git repo URL

# Clone the Git repository using SSH key
repo_dir = 'model_repo'
Repo.clone_from(git_repo_url, repo_dir, env=dict(GIT_SSH_COMMAND=f'ssh -i {ssh_key_path}'))

# Create a SageMaker client
sagemaker = boto3.client('sagemaker', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)