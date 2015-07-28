# coding: utf-8

from __future__ import absolute_import, division, print_function

import random
from . import BaseBot


class Daniel(BaseBot):

    _NAME = "daniel"
    _ICON = ":penguin:"

    def help(self):
        if self.msg.command != u"help":
            return ""
        return """Hello! :penguin:

yo
  - Daniel says yo.
echo $1 
  - Daniel echo back $1.
omikuji
  - Daniel tells your fortunes.
"""

    def echo(self):
        """オウム返しをする"""
        if self.msg.command != u"echo":
            return ""
        return " ".join(self.msg.args[2:])

    def yo(self):
        """YO"""
        if self.msg.command != "yo":
            return ""
        return "yo"

    def omikuji(self):
        """Omikuji"""
        if self.msg.command != "omikuji":
            return ""
        text = self.msg.user_name.encode("utf-8") + "の運勢は…\n\n"
        text += random.choice([
            "「大吉」です。",
            "「大吉」です。",
            "「中吉」です。",
            "「中吉」です。",
            "「小吉」です。",
            "「末吉」です。",
            "「吉」です。",
            "……。",
        ])
        return text

    def tweet(self):
        """tweet"""
        if self.msg.command != "tweet":
            return ""
        from ..tweet_post import TweetPost
        tw = TweetPost()
        msg = " ".join(self.msg.args[2:])
        result = tw.post(msg)
        if result:
            return "ツイートしたよ!"
        return "..."

    def scheduled_morning(self, dt):
        if dt.hour == 10 and dt.minute == 0:
            text = self._format_dt(dt)
            text += random.choice([
                "おはようございます。",
            ])
            return text

    def scheduled_night(self, dt):
        if dt.hour == 19 and dt.minute == 0:
            text = self._format_dt(dt)
            text += random.choice([
                "困ってますか？",
            ])
            return text

    def scheduled_lunch(self, dt):
        if dt.hour == 12 and dt.minute == 00:
            text = "お昼です。"
            return text
