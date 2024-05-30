import paramiko, os
from dotenv import load_dotenv
load_dotenv()
host = os.getenv("MC_HOST")
port = os.getenv("MC_PORT")
username = os.getenv("MC_USER")
private_key_path = os.getenv("MC_SSH_PATH")

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

private_key = paramiko.Ed25519Key(file_obj=open(private_key_path, 'r'))


def dockerComposeDown():
    ssh.connect(host, port, username, pkey=private_key)
    command1 = "docker-compose -f /app/docker-compose.yml down"
    stdin, stdout, stderr = ssh.exec_command(command1)
    print(stdout.read().decode('utf-8'))
    ssh.close()

def dockerComposeUp():
    ssh.connect(host, port, username, pkey=private_key)
    command2 = "docker-compose -f /app/docker-compose.yml up -d"
    stdin, stdout, stderr = ssh.exec_command(command2)
    print(stdout.read().decode('utf-8'))
    ssh.close()

