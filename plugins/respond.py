# -*- coding: utf-8 -*-
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import datetime
import logging
import logging.config
import random, re

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s [%(levelname)s] %(name)s, line %(lineno)d: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'class':'logging.StreamHandler',
            'level':'INFO',
            'formatter': 'default'
        },
        'file': {
            'class' : 'logging.handlers.TimedRotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'default',
            'filename': '/tmp/r2d2bot.log',
            'when': 'D',
            'interval': 1,
            'backupCount': 30,
            'encoding': 'utf8',
            'utc': True
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
}

logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)
not_english_only = re.compile(u'.*[^\x00-\x7F]')
english_hour_start = datetime.time(7)
english_hour_end = datetime.time(8)

def formatted_reply(message, reply, attachments=[]):
    if (english_hour_start < datetime.datetime.utcnow().time() < english_hour_end) and \
       not_english_only.match(message.body['text']):
        message.reply("there will be ~a~ indian on board this or next  month, so we need use english to talk")
    else:
        client = message._client
        if type(reply) == list:
            reply = random.choice(reply)
        client.webapi.chat.post_message(message._body['channel'], reply, username="赵闽", icon_url=client.bot_icon, attachments=attachments)

@listen_to(u"(為什麼|為何)")
def zm_knowwhy(message, matcher):
    reply = "因為淡水阿嬤一句話"
    formatted_reply(message, reply)

@listen_to(u"(感恩|感謝)")
def zm_welcom(message, matcher):
    reply = "不客氣，穴蟹你~"
    formatted_reply(message, reply)

@listen_to(u"(妹紙|妹子|妹|正妹|外國妹)")
def zm_callfrank(message, matcher):
    reply = "快叫 <@{}> 過來看".format(message._client.find_user_by_name('franktseng'))
    formatted_reply(message, reply)

@listen_to(u"(幹嘛的)")
def zm_forwhat(message, matcher):
    candidate_replys = ["你問我？那我不是要去ㄅㄨㄚˇ杯？", "孩子，我怎麼會知道呢？"]
    formatted_reply(message, candidate_replys)

@listen_to(u"(可以嗎|客以嗎|克以嗎)")
def rita_say_yes(message, matcher):
    reply = "何樂而不為呢"
    client = message._client
    client.webapi.chat.post_message(message._body['channel'], reply, username="Rita", icon_url="https://googledrive.com/host/0BxX58iZJR2ZHNXo3TWYtVFhaRlk")

@listen_to(u"(趙老師)")
def zm_showup(message, matcher):
    candidate_replys = ["好~吧  繼續吧  反正你說的我都不懂",
                        "我人在印度呀！",
                        "标记了一个骚扰电话，一点成就感都没有。。。",
                        "和荣誉无关",
                        "這不科學呀!",
                        "一天几次?平均",
                        "<@{}> 看妳把所有视频会议室全占了?".format(message._client.find_user_by_name('yilinglin')),
                        "我估計這個量不高"]
    formatted_reply(message, candidate_replys)

@respond_to(u"(.*?(同意|審批|覺得|如何|怎麼樣|怎樣|同意嗎))")
def zm_agree_or_not(message, sentence, keyword):
    reply = ["同意"] * 7 + ["不同意"] * 2 + ["做死呀？當然不同意"]
    formatted_reply(message, reply)

@respond_to(u"(.*?(做好|做滿|做完了))")
def zm_thank_you(message, sentence, keyword):
    reply = "辛苦了"
    formatted_reply(message, reply)

@respond_to(u"(.*?(找誰處理))")
def zm_dispatch(message, sentence, keyword):
    reply = "doreen 安排一下"
    formatted_reply(message, reply)

# @listen_to(u"abc|中文")
# def zm_test(message):
#     logger.debug(message.body['text'])
#     reply = "english hour now"
#     formatted_reply(message, reply)
