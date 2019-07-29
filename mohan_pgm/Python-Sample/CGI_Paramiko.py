import paramiko


nbytes = 4096
hostname = '192.168.1.26'
port = 22
username = 'admin' 
password = '12345'
command = 'show ip int brief'

client = paramiko.Transport((hostname, port))
client.connect(username=username, password=password)

print("connection made in the ip")
      

stdout_data = []
stderr_data = []
session = client.open_channel(kind='session')
session.exec_command(command)
while True:
    if session.recv_ready():
        print("one")
        stdout_data.append(session.recv(nbytes))
        var= session.recv(nbytes)
        var2 = var.decode("utf-8")
        print(var)
        print(var2)
        print("tow")
        print(stdout_data)

print(stdout_data)
session.close()
client.close()

