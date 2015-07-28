# coding: utf-8

from __future__ import absolute_import, division, print_function

from . import outgoing_fetch


BASE_URI = "/clap"


def test_clap_normal():
    result = outgoing_fetch(BASE_URI, {
        "text": "youcan - #42 Success after 4.5 sec (</job/youcan/42/|Open>)",
        "user_name": "slack_bot",
    })
    assert ":clap:" in result.data


def test_clap_back():
    result = outgoing_fetch(BASE_URI, {
        "text": "youcan - #30 Back to normal after 22 sec (</job/youcan/30/|Open>)",
        "user_name": "slack_bot",
    })
    assert ":clap:" in result.data

