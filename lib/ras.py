__author__ = 'Dominik Jungowski'

import socket

class RasPi:
    __address = None
    __port = None
    __socket = None

    def __init__(self, address, port):
        self.__address = address
        self.__port = port

    def update(self, status):
        self.__connect()
        self.__send(status)
        self.__disconnect()

    def __connect(self):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.connect((self.__address, self.__port))

    def __disconnect(self):
        self.__socket.close()

    def __send(self, status):
        self.__socket.send(bytes(status, 'utf-8'))