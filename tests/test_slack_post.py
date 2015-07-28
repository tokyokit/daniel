# coding: utf-8

from __future__ import absolute_import, division, print_function

from mock import patch, MagicMock

#from src.slack_post import SlackPost

dummy_config = {
    "SLACK_SUB_DOMAIN": "tokyokit",
    "WEBHOOK_TOKEN": {
        # channel名をキーにして格納
        "test": "xxxxxxxxxx",
    }
}


#@patch('google.appengine.api.urlfetch.fetch')
#def test_post(m):
#    result = MagicMock()
#    result.status_code = 200
#    m.return_value = result
#    post = "This is test"
#    slack = SlackPost(dummy_config, "test")
#    result = slack.post(post)
#    assert result.status_code == 200
#
#
#@patch('google.appengine.api.urlfetch.fetch')
#def test_batch_posts(m):
#    result = MagicMock()
#    result.status_code = 200
#    m.return_value = result
#
#    posts = [
#        "test",
#        "test2",
#    ]
#    slack = SlackPost(dummy_config, "test")
#    results = slack.batch_post(posts)
#    assert len(results) == 2
#    assert results[0].startswith("success")
#    assert results[1].startswith("success")
