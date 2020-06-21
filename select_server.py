from socket import *
from select import *

HOST="127.0.0.1"
PORT=12345
ADDR=(HOST,PORT)

def main():
    s=socket()
    s.bind(ADDR)
    s.listen()

    s.setblocking(False)

    rlist=[s]
    wlist=[]
    xlist=[]

    while True:
        rs,ws,xs=select(rlist,wlist,xlist)
        for i in rs:
            if i is s:
                connfd,addr=i.accept()
                print("Connect from",addr)
                connfd.setblocking(False)
                rlist.append(connfd)
            else:
                data=i.recv(1024).decode()
                if not data:
                    rlist.remove(i)
                    i.close()
                    continue
                print(data)
                i.send(b"OK")





if __name__ == '__main__':
    main()