from socket import *
from multiprocessing import Process
import sys,signal

HOST="127.0.0.1"
PORT=12345
ADDR=(HOST,PORT)

def func(connfd):
    while True:
        data=connfd.recv(1024).decode()
        if not data:
            connfd.close()
            break
        print("来自客户端消息",data)
        connfd.send(b"OK")


def main():
    s=socket()
    s.bind(ADDR)
    s.listen()

    while True:
        try:
            connfd,addr=s.accept()
            print("Connect from",addr)
        except:
            s.close()
            sys.exit("系统退出")
        p=Process(target=func,args=(connfd,))
        p.daemon=True
        p.start()


if __name__ == '__main__':
    main()
