import socket, subprocess
sock = socket.socket()
sock.bind(('',5006))
sock.listen(10)

data2 = "RobotControl_base_stop.py"
path = "python "+os.path.join(os.path.dirname(os.path.abspath(__file__)),data2)
p = subprocess.Popen(path.split(' '))

while True:
    cli, info = sock.accept()
    data1 = cli.recv(1024)
    data1 = data.split(":::")[0]
    print data1
    if data2 != data1:
        path = "kill -9 "+str(p.pid)
        path = "python "+os.path.join(os.path.dirname(os.path.abspath(__file__)),data1)
        p = subprocess.Popen(path.split(' '))
    