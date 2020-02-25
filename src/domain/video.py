# !usr/bin/python
# -*- coding: UTF-8 -*-

import copy

class Video:

    def __init__(self, search_prefix=None, search_term=None, language_prefix='en', state=0, resolution=(1920, 1080), sentences=[]):
        self.search_prefix = search_prefix
        self.search_term = search_term
        self.language_prefix = language_prefix
        self.state = state
        self.resolution = resolution
        self.sentences = sentences

    @property
    def title(self):
        return f'{self.search_prefix} {self.search_term}'

    @property
    def path(self):
        return f'../storage/{self.title} {self.language_prefix}'

    @property
    def video_width(self):
        return self.resolution[0]

    @property
    def video_height(self):
        return self.resolution[1]
