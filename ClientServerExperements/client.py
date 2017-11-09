#!/usr/bin/env python3.6

import select
import socket
import sys

USERNAME = '#'

def set_screen():
    # Create new blank screen
    for i in range(100):
        print()
    print('    Welcome To Go.    ')

def go_client():
    if(len(sys.argv) < 2) :
        print('Usage : GO hostname')
        sys.exit()
    host = sys.argv[1]
    if len(sys.argv) > 2:
        port = int(sys.argv[2])
    else:
        port = 8888
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print('Unable to connect')
        sys.exit()
    
    set_screen()
    
    # request and set username (Should be in a function this was easier for experements)
    name_set = False
    while not name_set:
        socket_list = [sys.stdin, s]
        ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
        for sock in ready_to_read:
            if sock == s:
                server_msg = sock.recv(4096).decode().strip()
                if not server_msg:
                    print(f'error occured')
                    sys.exit()
                if server_msg.split(':')[0] == '!Set':
                    USERNAME = server_msg.split(':')[1]
                    sys.stdout.write(f'Username set to {USERNAME}\n'); sys.stdout.flush()
                    name_set = True
                    break
                else:
                    sys.stdout.write(server_msg)
                    sys.stdout.write('->'); sys.stdout.flush()
                    requested_name = sys.stdin.readline()
                    s.sendto(requested_name.encode('utf-8'), (host, port))
    
    # Actual GO game start
    while 1:
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
         
        for sock in ready_to_read: 
            if sock == s:
                # incoming message from remote server, s
                data = sock.recv(4096).decode()
                if not data:
                    print('\nDisconnected from chat server')
                    sys.exit()
                else :
                    #print(data)
                    sys.stdout.write(data)
                    sys.stdout.write(f'{USERNAME}: '); sys.stdout.flush()     
            
            else :
                # user entered a message
                sys.stdout.write(f'{USERNAME}: '); sys.stdout.flush() 
                msg = sys.stdin.readline()
                s.sendto(msg.encode('utf-8'), (host, port))
                sys.stdout.write(f'{USERNAME}: '); sys.stdout.flush() 

if __name__ == "__main__":
    go_client()
