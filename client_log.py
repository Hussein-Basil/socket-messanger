import socket
import datetime
import threading
import pickle


HOST = '192.168.0.102'
PORT = 5050
FORMAT = 'utf-8'
HEADER = 1024
DISCONNECT_MESSAGE = '!DC'
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))



def now():
    now = datetime.datetime.now()
    time_now = f'{str(now.hour).zfill(2)}:{str(now.minute).zfill(2)}'
    return time_now


while True:
    recv_data = client.recv(HEADER)
    data = pickle.loads(recv_data)
    if data['message'] == DISCONNECT_MESSAGE:
        print(1)
        print(f"\n@  [System] Today at {now()} \n   {data['name']} left the chat")
        break
    print(f"\n@  [{data['name']}] Today at {now()} \n   {data['message']}")

client.close()