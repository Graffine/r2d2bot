This is a bot plugin based on [lins05/slackbot](https://github.com/lins05/slackbot) for funny usage.

### Configure your robot ###

You should create a `slackbot_settings.py` to set some environment for you bot.

Here is an example:
```
#!bash
API_TOKEN = "Your slack bot token"
default_reply = "Sooooooorry what are you talking about?"
BOT_ICON = "Your bot icon"

PLUGINS = [ 
    'slackbot.plugins',
    'plugins',
]

```