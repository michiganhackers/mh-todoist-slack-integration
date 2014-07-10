mh-todoist-slack-integration
============================

Hooks up Todoist and Slack for much awesome

## Installing

You need to run this on a server, then point a Slack outgoing webhook integration at it.

You should set the bot to run on a single channel (with a very similar name to the Todoist project)

## Usage

Slack messages containing the tag `#todo` will be parsed and a list of outstanding tasks will be returned by the slackbot.

## Caveats

- Slack channels and Todoist projects are compared by levenshtein distance, there is some flexibility in naming, but try to name them similarly
- Right now todos aren't filtered or formatted very well, it is not a good idea to type `#todo` if there are a lot of outstanding tasks
- Things are a little slow, going to look into that soon
- More commands coming soon!

