import os

# Start
PORT=int(os.environ.get("PORT", 5000))
SLACK_USER=os.environ.get("SLACK_USER", "slackbot")
TODOIST_USER=os.environ.get("TODOIST_USER", "")
TODOIST_PASSWORD=os.environ.get("TODOIST_PASSWORD", "")
