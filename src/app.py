import json

import tornado.ioloop
import tornado.web
import tornado.httpserver

import conf

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        if self.get_argument("user_name", conf.USERNAME) != conf.USERNAME:
            self.write(json.dumps({"text": self.get_argument('text', 'Hello, World!')}))

def main():
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    server = tornado.httpserver.HTTPServer(application)
    server.listen(conf.PORT)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
