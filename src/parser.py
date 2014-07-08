import re

class MessageParser(object):
    def _find_hashtags(self, msg):
        return re.findall(r"#(\w+)", msg)

    def parse(self, msg):
        tags = self._find_hashtags(msg)
        for tag in tags:
            if tag == "todo":
                return {"action": "list_group_todos" }

        return {"action": "none"}
