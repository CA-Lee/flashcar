from typing import Dict


def generate_card(
    title: str,
    ok: Dict = {"type": "message", "text": "OK"},
    wtf: Dict = {"type": "message", "text": "WTF"},
):
    return {
        "type": "bubble",
        "size": "giga",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "image",
                    "size": "full",
                    "aspectMode": "cover",
                    "aspectRatio": "1:1.2",
                    "gravity": "center",
                    "url": "https://oishdsdahgfkfg.syf",
                    "position": "relative",
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": title,
                                    "size": "4xl",
                                    "adjustMode": "shrink-to-fit",
                                    "wrap": True,
                                    "align": "center",
                                }
                            ],
                            "flex": 7,
                            "justifyContent": "center",
                            "alignItems": "center",
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "WTF",
                                            "size": "xxl",
                                            "align": "center",
                                        }
                                    ],
                                    "height": "100%",
                                    "justifyContent": "center",
                                    "backgroundColor": "#FF7373",
                                    "action": wtf,
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "OK",
                                            "align": "center",
                                            "size": "xxl",
                                        }
                                    ],
                                    "backgroundColor": "#44C444",
                                    "justifyContent": "center",
                                    "action": ok,
                                },
                            ],
                            "flex": 1,
                        },
                    ],
                    "width": "100%",
                    "height": "100%",
                    "position": "absolute",
                },
            ],
            "paddingAll": "0px",
        },
    }
