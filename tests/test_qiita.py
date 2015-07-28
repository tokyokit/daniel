# coding: utf-8

from __future__ import absolute_import, division, print_function

import json

from src.models import qiita



BASE_URI = "/daniel"


def test_qiita_post():
    params = {
      "model": "item",
      "action": "created",
      "item": {
        "id": 76,
        "uuid": "eac2523763f336b07020",
        "user": {
          "id": 2,
          "url_name": "qiitan",
          "profile_image_url": "user_image.jpg"
        },
        "title": "TestItem",
        "created_at": "2014-06-19 19:29:26 +0900",
        "updated_at": "2014-06-19 19:29:26 +0900",
        "created_at_in_words": "1分未満",
        "updated_at_in_words": "1分未満",
        "tags": [
            {
                "name": "JavaScript",
                "url_name": "javascript",
                "icon_url": "/icons/medium/missing.png",
                "versions": ["1.8"]
            },
            {
                "name": "test",
                "url_name": "test",
                "icon_url": "/icons/medium/missing.png",
                "versions": ["1.8"]
            },
        ],
        "stock_count": 0,
        "comment_count": 0,
        "url": "http://increments.qiita.com/qiitan/items/eac2523763f336b07020",
        "created_at_as_seconds": 1403173766,
        "team_url_name": "increments",
        "lgtm_count": 0,
        "private": False,
        "coediting": False,
        "raw_body": "this is a test item\n",
        "body": "<p>this is a test item</p>\n",
        "stock_users": []
      },
      "user": {
        "id": 2,
        "url_name": "qiitan",
        "profile_image_url": "user_image.jpg"
      }

    }
    #app = qiita.app.test_client()
    #result = app.post("/qiita", data=json.dumps(params))

