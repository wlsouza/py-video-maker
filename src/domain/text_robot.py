# !usr/bin/python
# -*- coding: UTF-8 -*-

import nltk
from src.infrastructure.wikipedia_service import WikipidiaService


class TextRobot():

    def __init__(self, search_term=None, search_prefix=None):
        self.search_term = search_term
        self.original_page = None
        self.treated_text = None

    def run(self):
        self.fetch_content_from_wikipedia()
        self.split_contents_to_sentences()

    def fetch_content_from_wikipedia(self):
        try:
            self.original_page = WikipidiaService.get_page(title=self.search_term, prefix_lang='pt')
        except Exception as error:
            raise Exception(f' Error while fetching text from wikipedia -> {error}')

    def split_contents_to_sentences(self):
        summary = self.original_page.summary
        self.treated_text = nltk.sent_tokenize(summary)
