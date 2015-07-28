# coding: utf-8

from __future__ import absolute_import, division, print_function

import datetime

import pytest
import logging

from src.bots.daniel import Daniel


BASE_URI = "/scheduled"


@pytest.mark.parametrize("input_datetime, expected", [
        ('2014-01-01 09:00:10', None),
        ('2014-01-01 10:00:01', "10:00"),
        ('2014-01-01 10:01:10', None),
        ('2014-01-01 11:00:10', None),
])
def test_morning(input_datetime, expected):
    dt = datetime.datetime.strptime(input_datetime, '%Y-%m-%d %H:%M:%S')
    bot = Daniel()
    actual = bot.scheduled_morning(dt)
    logging.debug(actual) 
    if expected:
        assert expected in actual
    else:
        assert expected == actual


@pytest.mark.parametrize("input_datetime, expected", [
        ('2014-01-01 18:00:10', None),
        ('2014-01-01 19:00:01', "19:00"),
        ('2014-01-01 19:01:10', None),
])
def test_night(input_datetime, expected):
    dt = datetime.datetime.strptime(input_datetime, '%Y-%m-%d %H:%M:%S')
    bot = Daniel()
    actual = bot.scheduled_night(dt)
    logging.debug(actual) 
    if expected:
        assert expected in actual
    else:
        assert expected == actual
