import json
import cherrypy
import sys
import socket
from register import register

register(3001)

class Server:
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
        routemove = cherrypy.request.json
        route = json.loads(routemove)
        print(route)
    @cherrypy.expose
    def ping(self):
        return "pong"

if __name__ == "__main__":
 '''   if len(sys.argv) > 1:
        port=int(sys.argv[1])
    else:
        port=8080'''
    cherrypy.quickstart(Server(),'', 'server.conf')