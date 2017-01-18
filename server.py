import random
import socket
import time

import connection
import simulator_server

_server_socket = None


def getServerSocket():
    global _server_socket
    if not _server_socket:
        _server_socket = connection.getConnection()
    return _server_socket


def notifyClient(data):
    try:
        print "Listening for client . . ."
        s = getServerSocket()
        conn, address = s.accept()
        print "Connected to client at ", address
        # output = conn.recv(2048);
        print 'send to client: ' + data
        conn.sendall(data)

    except socket.error:
        print "NO CLIENT "


def main():
    data = simulator_server.Data('Temperature')
    simulation_server = simulator_server.SimulationServer()
    data.attach(simulation_server)
    while True:
        # observer pattern whenever there's a change in data (which is accomplished by setting the data object),
        # it calls notifyClient routine on Simulation Server
        data.setData(simulation_server.getTemperature())
        randomDelay = random.randint(1, 5)
        time.sleep(randomDelay)


if __name__ == '__main__':
    main()
