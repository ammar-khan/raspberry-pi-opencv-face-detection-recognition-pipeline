##
# Copyright 2018, Ammar Ali Khan
# Licensed under MIT.
##

import socketserver
from http import server


##
# Server class - inherits socketserver.ThreadingMixIn and server.HTTPServer
# This class provides HTTP server
##
class Server(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True
