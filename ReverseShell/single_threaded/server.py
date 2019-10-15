# Date Started 08.08.2019

import socket
import sys

# Create socket (allows two computer to connect)
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))

# Bind socket to port and wait for connection from client
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))
        s.bind((host, port))
        s.listen(5)     # 5 means number of bad connection which is refused before taking new connection
    except socket.error as msg:
         print("Socket Binding error: " + str(msg) + "\n" + "Retrying...")
         socket_bind()

# Establish a connection with client (socket must be listening from them)
def socket_accept():
    conn, address = s.accept()
    print("Connection has been Established | " + "IP " + address[0] + " | Port " + str(address[1]))
    send_commands(conn)
    conn.close()

# Send Commands
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8") # 1024 ~ buffer
            print(client_response, end="") # end="" is used to send cursor to new line


def main():
    socket_create()
    socket_bind()
    socket_accept()

main()
