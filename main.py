from colorama import Fore, Style
import colorama
import datetime
import os
import socket

PORT = "2003" # Can be changed


def __main__():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)