import json

import tornado.ioloop
import tornado.web
import tornado.httpserver

import conf
from parser import MessageParser

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        if self.get_argument("user_name", conf.USERNAME) != conf.USERNAME:
            m = MessageParser()
            result = m.parse(self.get_argument('text', 'Hello, World!'))
            if result["action"] == "list_group_todos":
                self.write(json.dumps({"text": "Do me! Do me!"}))

def main():
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    server = tornado.httpserver.HTTPServer(application)
    server.listen(conf.PORT)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
