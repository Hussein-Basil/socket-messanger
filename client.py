import socket, threading, pickle, os
HOST = '192.168.0.102'
PORT = 5050
FORMAT = 'utf-8'
HEADER = 1024
DISCONNECT_MESSAGE ='!DC'

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))

def send(string):
    client.sendall(bytes(string, FORMAT, 'ignore')) 

def start():
    print("~SocketApp v1.0\n WELCOME IN SOCKETAPP FOR MESSAGING ON LOCAL NETWORKS.")
    print("×"*30)
    name = input("Enter your name : ")
    send(name)
    print("×"*30)
    
    while True:
        message = input("Type a message : ")
        while not message:
            message = input()
        send(message)
        if message == DISCONNECT_MESSAGE:
            break

        os.system('cls')

start()
client.close()
