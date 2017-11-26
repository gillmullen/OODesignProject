import socket
import sys
import select

class User:
    def __init__(self, username='Annon', host='localhost', port=8888, win_count=0):
        '''Initialises user 
           username: Username the user chooses (str)
           win_count: The number of games the user has won (int)
           return None
        '''
        self.win_count = win_count
        self.host = host
        self.port = port
     
        self._connect()
        self.set_screen()
        self._request_username()


    def _connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(2)
 
        try:
            self.sock.connect((self.host, self.port))
        except:
            print('Failed to connect')
            sys.exit(1)

    def _request_username(self):
        name_set = False
        while not name_set:
            socket_lst = [sys.stdin, self.sock]
            ready_to_read,ready_to_write,in_error = select.select(socket_lst, [], [])
            for sock in ready_to_read:
                if sock == self.sock:
                    serv_msg = sock.recv(4096).decode().strip() # change 4096 to var
                    if not serv_msg:
                        print('Error occured')
                        sys.exit()
                    if serv_msg.split(':')[0] == '!set':
                        self.username = serv_msg.split(':')[1]
                        sys.stdout.write('Username set to {}\n'.format(self.username))
                        sys.stdout.flush()
                        name_set = True
                        break
                    else:
                        sys.stdout.write(serv_msg + '\n')
                        sys.stdout.write('-> ')
                        sys.stdout.flush()
                        rqst_name = sys.stdin.readline()
                        self.sock.sendto(rqst_name.encode('utf-8'),
                                            (self.host, self.port))


    def set_screen(self):
        '''Refactor to game class
        '''
        print('\n' * 100)
        print('Welcome to Go')

