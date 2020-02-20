# !usr/bin/python
# -*- coding: UTF-8 -*-

import copy

class Video:

    def __init__(self, search_prefix=None, search_term=None, language_prefix='en', state=0,  sentences=[]):
        self.search_prefix = search_prefix
        self.search_term = search_term
        self.language_prefix = language_prefix
        self.state = state
        self.sentences = sentences

    @property
    def title(self):
        return f'{self.search_prefix} {self.search_term}'
