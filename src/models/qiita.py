# coding: utf-8

from __future__ import absolute_import, division, print_function

import logging
import json

from flask import Flask, jsonify, request

from .settings import config
from .slack_post import SlackPost

app = Flask(__name__)


@app.route('/qiita', methods=['POST'])
def qiita():
    """ QiitaのWebHookを受けてSlackにポストする"""
    params = json.loads(request.data)

    if params["action"] != "created":
        # created 以外だったら何もしない
        return ""

    post_to = determinPostChanel(params)
   
    # Qiita通常投稿をパース
    if params["model"] == "item":
        user = params["user"]["url_name"]
        url = params["item"]["url"]
        title = ""
        body = params["item"]["raw_body"][:400] 
        post_text = "New: <" + url + "|" + params["item"]["title"] + ">"
    
    # Qiitaコメントをパース
    elif params["model"] == "comment":
        user = params["comment"]["user"]["url_name"]
        title = ""
        url = params["item"]["url"]
        body = params["comment"]["raw_body"][:400]
        post_text = "New Comment: <" + url + "|" + params["item"]["title"] + ">"

    post = json.dumps({
        "attachments": [{
            "failback": post_text,
            "pretext": post_text,
            "color": "#60c90d",
            "mrkdwn_in": ["fields"],
            "fields": [{
                "title": title,
                "value": body,
                "short": False,
            }],
        }],
        "username": "Qiitan (by " + user + ")",
        "icon_emoji": ":qiita:",
    })
    logging.debug(post)

    slack = SlackPost(config, post_to)
    result = slack.post(post)
    return jsonify(result)


def determinPostChanel(params):
    """ 投稿するチャンネルを決定する
    ここのチャンネルはSettingsに登録してある必要がある
    """
    for tag_data in params["item"]["tags"]:
        if tag_data["name"] == "test":
            return "test"
    return "qiita"


