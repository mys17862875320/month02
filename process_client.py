from socket import *
from multiprocessing import Process

HOST="127.0.0.1"
PORT=12345
ADDR=(HOST,PORT)

def main():
    s=socket()
    s.connect(ADDR)
    while True:
        msg=input("请输入消息:")
        if not msg:
            break
        s.send(msg.encode())
        data=s.recv(1024).decode()
        print("从客户端接收到:",data)



if __name__ == '__main__':
    main()