# coding: utf-8

from __future__ import absolute_import, division, print_function

import datetime
import pytz

from flask import Flask, jsonify

from .models.slack_post import SlackPost
from .settings import config
from .bots.daniel import Daniel

app = Flask(__name__)


@app.route('/jihou')
def jihou():
    bot = Daniel()
    jst = pytz.timezone('Asia/Tokyo')
    now = datetime.datetime.now(jst)
    # 土日は動かさない
    if now.weekday() >= 5:
        return ""
    posts = bot.scheduled_posts(now)
    slack = SlackPost(config, "jihou")
    results = slack.batch_post(posts)
    return jsonify({
        "react": len(results),
        "result": results
    })


# post_target: slack channel to post
# app_id: iTunes app id
@app.route('/app_review/<post_target>/<int:app_id>')
def app_review(post_target, app_id):
    from .appreview import AppReview
    ar = AppReview(str(app_id))
    review = ar.checkNew()
    if not review:
        return "None"
    bot = Daniel()
    post = bot.format_post(str(review))
    slack = SlackPost(config, post_target)
    result = slack.post(post)
    if result.status_code == 200:
        return "success"
    return "false"
