# coding: utf-8

from __future__ import absolute_import, division, print_function

import logging

from flask import Flask, request, render_template

from .models.message import Message
from .models.slack_post import SlackPost
from .bots.daniel import Daniel
from .bots.clap import Clap
from .settings import config

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello Daniel"


@app.route('/daniel_post', methods=['GET', 'POST'])
def daniel_post():
    """ DanielとしてPOSTできる投稿フォーム """
    if request.method == 'POST':
        msg = request.form['message']
        channel = request.form['channel']
        bot = Daniel()
        post = bot.format_post(msg)
        slack = SlackPost(config, channel)
        result = slack.post(post)
        if result.status_code == 200:
            return "success"
        return "error"
    channels = config["WEBHOOK_TOKEN"].keys()
    return render_template('daniel_form.html', channels=channels)


@app.route('/daniel', methods=['POST'])
def daniel():
    """ `daniel xxx` のようにslackで投稿された時のエントリポイント """
    msg = Message.parse(request)
    logging.debug(msg)
    # 無限ループ回避
    if msg.user_name == "slackbot":
        return ''
    bot = Daniel(msg)
    return bot.say()


@app.route('/clap', methods=['POST'])
def clap():
    """ Jenkinsに反応して拍手するアクションのエントリポイント """
    msg = Message.parse(request)
    logging.debug(msg)
    # jenkinsはslackbot扱い
    bot = Clap(msg)
    return bot.say()
