# filename: ssh_script.py
import paramiko
import os
from base64 import b64decode

# Replace these variables with your actual values
hostname = '65.1.225.4'
port = 22
username = 'ec2-user'
private_key_path = 'private_key.pem'

# private_key_content = b64decode(private_key_path).decode()

# print(private_key_content)

# Create an SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Load the private key for authentication
private_key = paramiko.RSAKey(filename=private_key_path)

# Connect to the server
client.connect(hostname, port=port, username=username, pkey=private_key)

# # Run a command on the server
# stdin, stdout, stderr = client.exec_command('ls')

# # Print the output
# print("Output:")
# print(stdout.read().decode())

# # Close the connection
# client.close()

try:
    # Run multiple commands on the server
    commands = [
        'git clone https://github.com/aruneer007/git-test.git ',
        'cd git-test',
        'python hello.py',
        # Add more commands as needed
    ]

    for command in commands:
        print(f"Executing command: {command}")
        stdin, stdout, stderr = client.exec_command(command)
        
        # Print the command output
        print(stdout.read().decode())

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the connection
    client.close()


# with open(private_key_path, 'r') as file:
#     pem_contents = file.read()
#     print("PEM Contents:")
#     print(len(pem_contents))
