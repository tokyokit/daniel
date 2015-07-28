# coding: utf-8

from __future__ import absolute_import, division, print_function

import logging

from google.appengine.api import urlfetch


class SlackPost():
    """ Slackに投稿するためのユーティリティクラス """
    def __init__(self, app_config, channel):
        # domain = app_config["SLACK_SUB_DOMAIN"]
        token = app_config["WEBHOOK_TOKEN"][channel]
        post_url = "https://hooks.slack.com/services/{0}"
        self.post_url = post_url.format(token)

    def post(self, post):
        logging.debug(post)
        result = urlfetch.fetch(
            url=self.post_url,
            method=urlfetch.POST,
            payload=post
        )
        return result

    def batch_post(self, posts):
        results = []
        for post in posts:
            result = self.post(post)
            if not result.status_code == 200:
                logging.error(result.status_code)
                results.append("failed:" + post)
            else:
                results.append("success:" + post)
        return results
