# !usr/bin/python
# -*- coding: UTF-8 -*-


class Video:

    def __init__(self, search_prefix='None', search_term='None', language_prefix='en', sentences=[]):
        self.search_prefix = search_prefix
        self.search_term = search_term
        self.language_prefix = language_prefix
        self.sentences = sentences

