import json
from app.flex import generate_card
from linebot.models import FlexSendMessage

PUI_PUI = "PUIPUI"
GREETING_TEXT = "PUI PUI！\n現在，想來點小卡嗎？"
TUTORIAL = "這裡應該要放說明但我還沒寫好，你先自己玩玩看"
GREETING_FLEX = FlexSendMessage(
    alt_text=PUI_PUI,
    contents=generate_card(
        GREETING_TEXT,
        {"type": "postback", "data": json.dumps({"type": "greeting"})},
        {"type": "message", "text": TUTORIAL},
    ),
)
