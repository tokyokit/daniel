# coding: utf-8

from __future__ import absolute_import, division, print_function

from . import BaseBot


class Clap(BaseBot):

    _NAME = "daniel"
    _ICON = ":penguin:"

    def clap(self):
        """jenkinsが通ったら拍手をする"""
        if ("Success after" in self.msg.text) or ("Back to normal" in self.msg.text):
            return ":clap:"

