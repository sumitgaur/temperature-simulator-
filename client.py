import socket

HOST = '127.0.0.1'
PORT = 8220


def main():
    address = (HOST, PORT)
    while True:
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(address)
            output = client_socket.recv(2048)
            if output:
                print "Temperature alert from server:"
                print output
        except Exception as msg:
            print msg
        finally:
            client_socket.close()


if __name__ == '__main__':
    main()
