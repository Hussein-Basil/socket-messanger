import socket
import threading
import pickle

# global variables
HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
HEADER = 1024
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DC'

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind((HOST,PORT))


clients = []

def handle_client(conn,addr):

    name = conn.recv(HEADER).decode()
    message = f'{name} joined the chat on port {addr[1]}'
    print('[CONNECTED] '+ message)
    d = {'name':name,'message':message}
    msg = pickle.dumps(d)
    broadcast(msg)

    while True:

        message = conn.recv(HEADER).decode()

        if message == DISCONNECT_MESSAGE:
            d['message'] = message
            msg = pickle.dumps(d)
            broadcast(msg)
            break

        d = {'name':name,'message':message}
        msg = pickle.dumps(d)
        print(f"\n{name} : {pickle.loads(msg)['message']}")
        broadcast(msg)
    
    client_ip = conn.getpeername()[0]
    
    for client in clients:
        if client[1] == client_ip and client[0] != conn:
            client[0].close()
            clients.remove(client)
    clients.remove((conn,addr[0]))
    conn.close()
    

def broadcast(msg):
    for client in clients:    
        client[0].sendall(msg)

        
def start():
    socket.listen()
    print(f"[LISTENING] Server is listening on {HOST}")
    while True:
        conn , addr = socket.accept()
        clients.append((conn,addr[0]))
        print(len(clients))
        print(f"[ACCEPTED] Connection accepted on port {addr[1]}")
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        
        
print("[STARTING] Server is starting..")
start()