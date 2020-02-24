# !usr/bin/python
# -*- coding: UTF-8 -*-


class Sentence:

    def __init__(self, text, keywords=[], image=None):
        self.text = text
        self.keywords = keywords
        self.image = image

    def __str__(self):
        return self.text

    def __repr__(self):
        return f' {{ Text: {self.text}, \nKeywords: {self.keywords}, \nImages:{self.images} }}'
