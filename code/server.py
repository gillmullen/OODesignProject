from game import Game
from user import User
import socket

class Server:
    def __init__(self, host, port, users={}, wait_list=[], recv_buffer=4096):
        '''Initialises server
           user_list: Contains users known to server
           wait_list: Contains users waiting for a game
           return None
        '''
        self.users = users
        self.wait_list = wait_list
        self.host = host
        self.port = port
        self.recv_buffer = recv_buffer
        self.socket_lst = []

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)

        # add server socket to lst of connections
        self.socket_lst.append(self.sock)

    def _add_user(self, username):
        '''Adds new user to system
           username: Username the user chooses (str)
           return None
        '''
    
    def broadcast(self, server_socket, sock, message):
        for socket in self.socket_lst:
            # Don't send message to server or who it came from
            if socket != server_socket and socket != sock:
                try:
                    print('sending msg')
                    socket.sendto(message.encode('utf-8'), socket.getsockname())
                    print('sent', end='')
                except:
                    # socket broken
                    socket.close()
                    # broken sockets removed
                    if socket in self.socket_lst:
                        self.socket_lst.remove(socket) 

    def set_username(self, sockfd):
        usr_msg = 'Please enter username: '
        set_msg = '!set:'
        sockfd.sendto(usr_msg.encode('utf-8'), sockfd.getsockname())
        while 1:
            name = sockfd.recv(self.recv_buffer).decode()
            if name:
                for each in self.users:
                    if self.users[each] == name:
                        print('Username {} is taken, choose another'.format(name))
                        name = ''
                        continue
                set_msg += name
                sockfd.sendto(set_msg.encode('utf-8'), sockfd.getsockname())
                return name

    def join_server(self, username):
        '''Logs user onto server, creating a new account if necessary
           username: Username the user chooses (str)
           return None
        '''
        if username not in self.user_list:
            self._add_user(username)

    def join_game(self, username, size):
        '''Adds user to game
           username: Username for user (str)
           size: Size user wants for game (int)
           return player number and piece (str)
        '''
        pass 

    def generate_game(self, user1, user2, size=9):
        '''Generates a game for two users
           user1: First user (User)
           user2: Second user (User)
           size: Size of board required for game (int)
           return None
        '''
        pass

    def pair_waiting_players(self):
        '''Checks wait list. If there's more than one user in
           the wait list generate a game
           return None
        '''
        pass

    def request_move(self, user):
        '''Requests a user to make their next move
           user: User to make move (User)
           return None
        '''
        pass

    def user_play(self, user, command):
        '''Calls the Game with the users command
           user: User making command (User)
           command: Play user wants to make (list)
           return bool determining if an error occured
        '''
        pass

    def _game_over(self, game, user1, user2):
        '''Game has ended. Increments win_count for winner.
           game: Game which has ended (Game)
           user1: First user (User)
           user2: Second user (User)
           return win/lose message (str)
        '''
        pass
