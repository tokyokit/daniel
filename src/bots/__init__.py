# coding: utf-8

from __future__ import absolute_import, division, print_function

import json
import logging
import datetime

import types


class BaseBot(object):

    _ICON = ":slack:"
    _NAME = "Slack"

    def __init__(self, msg=None):
        self.msg = msg

    def say(self):
        # 関数を探す
        subclass_attrs = set(dir(self.__class__)) - set(dir(BaseBot))
        for key in subclass_attrs:
            if key.startswith("_") or key.startswith("scheduled_"):
                continue
            attr = getattr(self, key)
            if not isinstance(attr, types.MethodType):
                continue

            # 実行してみて結果があれば返す
            logging.debug("execute:" + key + "()")
            result = attr()
            if result:
                return json.dumps({
                    "text": result,
                    "username": self._NAME,
                    "icon_emoji": self._ICON
                })
        return ""

    def scheduled_posts(self, now):
        posts = []
        subclass_attrs = set(dir(self.__class__)) - set(dir(BaseBot))
        for key in subclass_attrs:
            if not key.startswith("scheduled_"):
                continue
            attr = getattr(self, key)
            if not isinstance(attr, types.MethodType):
                continue

            logging.debug("execute:" + key + "()")
            result = attr(now)
            if result:
                post = json.dumps({
                    "text": result,
                    "username": self._NAME,
                    "icon_emoji": self._ICON
                })
                posts.append(post)
        return posts

    def format_post(self, text):
        return json.dumps({
                "text": text,
                "username": self._NAME,
                "icon_emoji": self._ICON
        })
        

    @staticmethod
    def _format_dt(dt):
        WEEKDAY = ('月','火','水','木','金','土','日')
        wd = WEEKDAY[dt.weekday()]
        day = dt.strftime("%m/%d %H:%M")
        return "{0}({1}) ".format(day, wd)
