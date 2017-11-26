from user import User
from server import Server
import sys
import select

def main():
    usrOne = User()

    while 1:
        socket_list = [sys.stdin, usrOne.sock]
        ready_to_read,ready_to_write,in_error = select.select(socket_list,[],[])
        for sock in ready_to_read:
            if sock == usrOne.sock:
                data = sock.recv(4096).decode().strip()
                if not data:
                    print('Disconnected from server')
                    sys.exit(1)
                else:
                    sys.stdout.write('\n')
                    sys.stdout.write(str(data))
                    sys.stdout.write('\n{}: '.format(usrOne.username))
                    sys.stdout.flush()
            else:
                msg = sys.stdin.readline()
                usrOne.sock.sendto(msg.encode('utf-8'), (usrOne.host, usrOne.port))
                sys.stdout.write('{}: '.format(usrOne.username))
                sys.stdout.flush()


if __name__ == '__main__':
    main()
