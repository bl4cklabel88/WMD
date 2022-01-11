import socket
import threading
class server:
    def __init__(self):
        self.socket = socket.socket()
        self.socket.bind(("0.0.0.0", 2565))
        self.socket.listen(5)
        self.addrList = []
    def handlerAccept(self):
        while(1):
            addr, con = self.socket.accept()
            self.addrList.append(addr)
    def run(self):
        threading.Thread(target=self.handlerAccept).start()
        while(1):
            try:
                print("conn ->", len(self.addrList))
                command = input(":->")
                for x in self.addrList:
                    try:
                        x.send(command.encode())
                    except:
                        self.addrList.remove(x)
            except KeyboardInterrupt:
                exit(1)
serv = server()
serv.run()