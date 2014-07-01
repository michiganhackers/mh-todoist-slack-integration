import tornado.ioloop
import tornado.web
import stripe
import os

import conf

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        pass


def main():
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    server = tornado.httpserver.HTTPServer(application)
    server.listen(conf.PORT)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
