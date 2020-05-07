#!/usr/bin/python3
import http.server
import socketserver

import rospy

class Node():
    def __init__(self,PORT):
        self.port = PORT
        self.Handler = http.server.SimpleHTTPRequestHandler
    
    def run(self):
        while not rospy.is_shutdown():
            with socketserver.TCPServer(("", self.port), self.Handler) as httpd:
                print("serving at port", self.port)
                httpd.serve_forever()

if __name__ == "__main__":
    rospy.init_node("website")
    port = rospy.get_param('~Port')
    Server = Node(port)
    Server.run()