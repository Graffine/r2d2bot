# -*- coding: utf-8 -*-
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import json
import random, re

def formatted_reply(message, reply):
    client = message._client
    client.webapi.chat.post_message(message._body['channel'], reply, username="赵闽", icon_url=client.bot_icon)

@listen_to('hi', re.IGNORECASE)
def hi(message):
    # react with thumb up emoji
    message.react('100')

@respond_to('I love you')
def love(message):
    message.reply('I love you too!')

@listen_to('Can someone help me?')
def help(message):
    message.reply('Yes, I can!')

@listen_to(u"(為什麼|為何)")
def zmknowwhy(message, matcher):
    reply = "因為淡水阿嬤一句話"
    formatted_reply(message, reply)

@listen_to(u"(感恩|感謝)")
def zmwelcom(message, matcher):
    reply = "不客氣，穴蟹你~"
    formatted_reply(message, reply)

@listen_to(u"(妹紙|妹子|妹|正妹|外國妹)")
def zmcallfrank(message, matcher):
    reply = "快叫 <@{}> 過來看".format(message._client.find_user_by_name('franktseng'))
    formatted_reply(message, reply)

@listen_to(u"(下午)")
def zmafternoon(message, matcher):
    reply = "沒睡覺談什麼兒 afternoon 呢？"
    formatted_reply(message, reply)

@listen_to(u"(幹嘛的)")
def zmforwhat(message, matcher):
    candidate_replys = ["你問我？那我不是要去ㄅㄨㄚˇ杯？", "孩子，我怎麼會知道呢？"]
    reply = random.choice(candidate_replys)
    formatted_reply(message, reply)

@listen_to(u"(趙老師)")
def zmshowup(message, matcher):
    candidate_replys = ["我這不就來了嗎~",
                        "who is aron?",
                        "welcome",
                        "叫我幹嘛?",
                        "我人在印度呀！",
                        "這不科學呀!",
                        "there will be ~a~ indian on board this or next  month, so we need use english to talk",
                        "这周cms周会不开了",
                        "我这里断了",
                        "一天几次?平均"]
    reply = random.choice(candidate_replys)
    formatted_reply(message, reply)

# @listen_to(u"(中文|英文)")
# # @listen_to(u"[^\w~]+", re.IGNORECASE)
# # @listen_to(u"[^\w~]+", re.IGNORECASE)
# def zmsayenglish(message, matcher):
#     reply = "From now on, all members of ~backend~ cms team must talk in English on ~slack~ Wechat"
#     formatted_reply(message, reply)

# @respond_to('(.*)')
@respond_to(u"[\u4e00-\u9fa5]*")
def zmsay(message):
    client = message._client
    agree_keywords = [u"同意", u"審批", u"覺得", u"如何", u"怎麼樣", u"怎樣"]
    thanks_keywords = [u"做好", u"做滿", u"做完了"]
    findwho_keywords = [u"找誰處理"]

    if any(keyword in message.body[u'text'] for keyword in agree_keywords):
        candidate_replys = ["同意"] * 7 + ["不同意"] * 2 + ["做死呀？當然不同意"]
        reply = random.choice(candidate_replys)
    elif any(keyword in message.body[u'text'] for keyword in thanks_keywords):
        reply = "辛苦了"
    elif any(keyword in message.body[u'text'] for keyword in findwho_keywords):
        reply = "doreen 安排一下"
    else:
        reply = "朕聽不懂你說什麼，說清楚點!"
    client.webapi.chat.post_message(message._body['channel'], reply, username="赵闽", icon_url=client.bot_icon)

