# coding: utf-8

from __future__ import absolute_import, division, print_function

import logging

from . import oauth
from .settings import config


class TweetPost:

    def __init__(self):
        self.CK = config["TWITTER_OAUTH"]["client_key"]
        self.CS = config["TWITTER_OAUTH"]["client_secret"]
        self.AT = config["TWITTER_OAUTH"]["application_key"]
        self.AS = config["TWITTER_OAUTH"]["application_secret"]
        self.POST_URL = "https://api.twitter.com/1.1/statuses/update.json"

    def post(self, message):
        params = {"status": message}
        client = oauth.TwitterClient(self.CK, self.CS, None)
        result = client.make_request(
            self.POST_URL,
            token=self.AT,
            secret=self.AS,
            additional_params=params,
            protected=True,
            method="POST"
        )
        logging.debug(result)
        logging.debug(result.status_code)
        logging.debug(result.content)
        return result.status_code == 200
