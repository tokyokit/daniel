# coding: utf-8

from __future__ import absolute_import, division, print_function

from . import outgoing_fetch


BASE_URI = "/daniel"


def test_yo():
    result = outgoing_fetch(BASE_URI, {
        "text": "daniel yo",
    })
    assert "yo" in result.data


def test_echo():
    result = outgoing_fetch(BASE_URI, {
        "text": "daniel echo hogehoge"
    })
    assert "hogehoge" in result.data

