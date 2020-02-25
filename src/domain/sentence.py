# !usr/bin/python
# -*- coding: UTF-8 -*-


class Sentence:

    def __init__(self, text, keywords=[], raw_image=None, treated_image=None):
        self.text = text
        self.keywords = keywords
        self.raw_image = raw_image
        self.treated_image = treated_image

    def __str__(self):
        return self.text

    def __repr__(self):
        return f' {{ Text: {self.text}, \nKeywords: {self.keywords}, \nRaw_images:{self.raw_image}, \nRaw_images:{self.treated_image} }}'
