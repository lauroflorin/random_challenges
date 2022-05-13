import socket
from _thread import *
import threading
import random


textWhenSolved="Remember, you can't differentiate <true randomness> (whatever that is) from pseudorandomness, just on output alone. \n"
flag="TDCNET{<insert your flag here>}"
seed=int(time.time()) #eg 1570543099  
i=0

# thread fuction 
def threaded(c):
    global i
    while True:

        # data received from client 
        data = c.recv(1024)
        if not data:
             print('Bye')
             break

        #data = data[::-1]
        rand=str(random.randrange(10E9,10E9 +  2**37−1))
#        if data.decode('utf-8')[:-1]==rand:
        if data.decode('utf-8')==rand:
            c.send((textWhenSolved + flag).encode('utf-8'))
        else:
            sendingData="id: {}\nrand: {}\nWhat's the next random number?".format(i,rand)
            c.send(sendingData.encode('utf-8'))
        i+=1
    # connection closed 
    c.close()


def Main():
    random.seed(seed)
    host = ""
    port = 31337
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("Socket bound to port", port)

    # put the socket into listening mode 
    s.listen()
    print("socket is listening")

    # a forever loop until client wants to exit 
    while True:

        # establish connection with client 
        c, addr = s.accept()

        # lock acquired by client 
        #print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier 
        start_new_thread(threaded, (c,))
    s.close()


if __name__ == '__main__':
    Main()
