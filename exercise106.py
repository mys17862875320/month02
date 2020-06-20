from socket import *
"""
Jame第一次修改
"""
from select import *

HOST="127.0.0.1"
PORT=12345
ADDR=(HOST,PORT)

def main():
    sock=socket()
    sock.bind(ADDR)
    sock.listen()
    sock.setblocking(False)

    p=poll()
    map={}
    p.register(sock,POLLIN)
    map[sock.fileno()]=sock

    while True:
        print("Waiting from connect")
        events=p.poll()

        for fd,event in events:
            if fd==sock.fileno():

                connfd,addr=map[fd].accept()
                print("Connect from",addr)
                connfd.setblocking(False)
                p.register(connfd, POLLIN)
                map[connfd.fileno()]=connfd
            elif event==POLLIN:
                data=map[fd].recv(1024).decode()
                if not data:
                    p.unregister(fd)

                    map[fd].close()
                    del map[fd]
                    continue
                print(data)
                map[fd].send(b"OK")


if __name__ == '__main__':
    main()


