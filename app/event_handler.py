import json
import random
from typing import List

from linebot import LineBotApi, WebhookHandler
from linebot.models import FlexSendMessage, MessageEvent
from linebot.models.events import FollowEvent, PostbackEvent
from linebot.models.messages import TextMessage

from app.config import LINE_SECRET, LINE_TOKEN
from app.const import GREETING_FLEX, PUI_PUI
from app.flex import generate_card

handler = WebhookHandler(LINE_SECRET)


@handler.add(MessageEvent, TextMessage)
def handle_text_message(event: MessageEvent):
    if event.source.type != "user":
        # TODO: key word toggle
        pass
    else:
        api = LineBotApi(LINE_TOKEN)
        api.reply_message(event.reply_token, GREETING_FLEX)


@handler.add(FollowEvent)
def handle_follow_event(event: FollowEvent):
    api = LineBotApi(LINE_TOKEN)
    api.reply_message(event.reply_token, GREETING_FLEX)


@handler.add(PostbackEvent)
def handle_postback_event(event: PostbackEvent):
    data = json.loads(event.postback.data)
    data_type = data.get("type")
    if data_type:
        title = None
        ok = None
        wtf = None
        if data_type == "greeting":
            words = json.load(open("app/words.json"))
            word = random.choice(words)
            title = f"{word.get('Word')} (lv.{word.get('Level')})"
            ok = {
                "type": "postback",
                "data": json.dumps({"type": "ok", "last_five": [word.get("Word")]}),
            }

            wtf = {
                "type": "uri",
                "uri": f"https://dictionary.cambridge.org/dictionary/english-chinese-traditional/{word.get('Word')}",
            }

        elif data_type == "ok":
            words: List = json.load(open("app/words.json"))
            last_five: List = data.get("last_five")

            word = random.choice(words)
            while word.get("Word") in last_five:
                word = random.choice(words)

            if len(last_five) > 4:
                last_five.pop(0)
            last_five.append(word.get("Word"))

            title = f"{word.get('Word')} (lv.{word.get('Level')})"
            ok = {
                "type": "postback",
                "data": json.dumps({"type": "ok", "last_five": last_five}),
            }
            wtf = {
                "type": "uri",
                "uri": f"https://dictionary.cambridge.org/dictionary/english-chinese-traditional/{word.get('Word')}",
            }

        if title and ok and wtf:
            api = LineBotApi(LINE_TOKEN)
            api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text=PUI_PUI,
                    contents=generate_card(
                        title,
                        ok,
                        wtf,
                    ),
                ),
            )
