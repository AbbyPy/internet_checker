import socket
from time import sleep


def check(host="8.8.8.8", port=53, timeout=10):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as err:
        print(err)
        return False

delay = 5
while True:
    sleep(delay)
    print(check())
