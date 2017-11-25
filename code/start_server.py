#!/usr/bin/env python3

from server import Server
import select
from user import User

def main(debug=True):
    # test stub
    welcome_msg = 'Connected to Go Server \o/ \n'
    master = Server('localhost', 8888)
    
    while 1:
        # get the lst sockets which are rad to be read trough select
        # 4th arg, time_out = 0 : poll and never block
        ready_to_read,ready_to_write,in_error = select.select(master.socket_lst,[],[],0)

        for sock in ready_to_read:
            # a new connection request recieved
            if sock == master.sock:
                sockfd, addr = master.sock.accept()
                master.socket_lst.append(sockfd)
                
                # Get username 
                username = master.set_username(sockfd).strip()
                master.users[sock.getsockname()] = username

                # Debug
                if debug:
                    print('Client {0} connected with username {1}'.format(
                            addr, master.users[sock.getsockname()]))

                # Welcome msg
                sockfd.sendto(welcome_msg.encode('utf-8'), sockfd.getsockname())
                master.broadcast(master.sock, sockfd, 
                        '{0} has joined the server\n'.format(master.users[sock.getsockname()].strip()))
            
            # a msg from client no a new connection
            else:
                # process data recieved
                try:
                    # receiving data from the socket
                    data = sock.recv(master.recv_buffer).decode('utf-8')
                    if data:
                        uname = master.users[sock.getsockname()]
                        msg = '{}: {}'.format(uname, data)
                        master.broadcast(master.sock, sock, msg)
                    else:
                        # remove socket it's broken
                        if sock in master.socket_lst:
                            master.socket_lst.remove(sock)
                        # at this stage, no data mean probable connection break
                        master.broadcast(master.sock, sock, \
                                           "Client (%s, %s) is offline\n % addr")
                except Exception as e:
                    print(e)
                    master.broadcast(master.sock, sock, "Client (%s, %s) is offline\n" % addr)
                    continue
    master.sock.close()

if __name__ == '__main__':
    main(True)
