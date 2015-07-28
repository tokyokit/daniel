# coding: utf-8

from __future__ import absolute_import, division, print_function

import json

from google.appengine.ext import db
from google.appengine.api import urlfetch

import logging


class ReviewPostedKey(db.Model):
    appid = db.StringProperty()
    uid = db.StringProperty()


class Review:
    uid = ""
    author = ""
    rating = 5
    title = ""
    content = ""

    def __str__(self):
        return (
            u"新着レビュー\n"
            + u"(★" + self.rating + ") " + self.author + "\n"
            + self.title + "\n"
            + self.content
        ).encode("utf-8")


class AppReview:

    def __init__(self, appid):
        self.appid = appid
        pass

    def checkNew(self):
        data = self._fetch()
        review = self._parseLatest(data)
        if not review:
            return None
        if self._checkDuplicate(review):
            return review
        return None

    def _fetch(self):
        url = "https://itunes.apple.com/jp/rss/customerreviews/id=" + str(self.appid) + "/json"
        logging.debug(url)
        result = urlfetch.fetch(url, headers={
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2)'
        })
        if result.status_code == 200:
            logging.debug(result.content)
            return result.content
        logging.error(result.status_code)
        return "{}"

    def _parseLatest(self, data):
        feed = json.loads(data)
        if "entry" not in feed["feed"]:
            return None
        if len(feed["feed"]["entry"]) < 2:
            return None
        review_data = feed["feed"]["entry"][1]
        review = Review()
        review.uid = review_data["id"]["label"]
        review.author = review_data["author"]["name"]["label"]
        review.rating = review_data["im:rating"]["label"]
        review.title = review_data["title"]["label"]
        review.content = review_data["content"]["label"]
        return review

    def _checkDuplicate(self, review):
        savedKeys = ReviewPostedKey.all().filter("appid =", self.appid).fetch(1) 
        if not savedKeys:
            savedKey = ReviewPostedKey()
            savedKey.appid = self.appid
        else:
            savedKey = savedKeys[0]
        if savedKey.uid == review.uid:
            return False
        savedKey.uid = review.uid
        savedKey.save()
        return True


if __name__ == '__main__':
    review = AppReview()
    review.checkNew()
