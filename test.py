# filename: ssh_script.py
import paramiko
import os

# Replace these variables with your actual values
hostname = '13.126.13.44'
port = 22
username = 'ec2-user'
private_key_path = 'private_key.pem'

# Create an SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Load the private key for authentication
private_key = paramiko.RSAKey(filename=private_key_path)

# Connect to the server
client.connect(hostname, port=port, username=username, pkey=private_key)

# Run a command on the server
stdin, stdout, stderr = client.exec_command('ls')

# Print the output
print("Output:")
print(stdout.read().decode())

# Close the connection
client.close()
