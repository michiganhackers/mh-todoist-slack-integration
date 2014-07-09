import re
import todoist

class MessageParser(object):
    def __init__(self):
        self.todo_api = todoist.Todoist()

    def _find_hashtags(self, msg):
        return re.findall(r"#(\w+)", msg)

    def parse(self, room, msg):
        project = self.todo_api.find_project(room)
        if not project:
            return None

        tags = self._find_hashtags(msg)
        for tag in tags:
            if tag == "todo":
                return {"action": "list_group_todos", "project": project }

        return None
