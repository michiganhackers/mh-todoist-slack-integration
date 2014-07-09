import json

import tornado.ioloop
import tornado.web
import tornado.httpserver

import conf
from parser import MessageParser


class MainHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.parser = MessageParser()

    def post(self):
        # Don't reply to our own bot
        if self.get_argument("user_name", conf.SLACK_USER) == conf.SLACK_USER:
            return

        msg = self.get_argument('text', '')
        room = self.get_argument('channel_name', '')

        result = self.parser.parse(room, msg)
        if not result:
            return

        if result["action"] == "list_group_todos":
            tasks = result["project"].get_uncompleted_tasks()
            self.write(self.__format_tasks_for_reply(result["project"], tasks))

    def __format_tasks_for_reply(self, project, tasks):
        reply = ""
        for task in tasks:
            reply += task.content + " _due " + task.due_date + "_\n"
        reply += "View at: https://todoist.com/app?v=301#project/" + project.id
        return json.dumps({"text": reply, "mrkdwn": True})

def main():
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    server = tornado.httpserver.HTTPServer(application)
    server.listen(conf.PORT)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
