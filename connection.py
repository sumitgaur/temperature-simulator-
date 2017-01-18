import socket

HOST = '127.0.0.1'
PORT = 8220


def getConnection():
    address = (HOST, PORT)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((address))
    server_socket.listen(5)
    return server_socket
