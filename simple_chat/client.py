from socket import socket, AF_INET, SOCK_STREAM
import logging


class ChatClient:
    def __init__(self):
        self.logger = self._setup_logger()
        self.sock = self._setup_socket(host, port)

    @staticmethod
    def _setup_logger():
        logger = logging.getLogger('chat_server')
        logger.addHandler(logging.StreamHandler())
        logger.setLevel(logging.DEBUG)
        return logger

    @staticmethod
    def _setup_socket(host, port):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.bind((host, port))
        sock.listen()
        return sock
