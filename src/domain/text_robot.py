# !usr/bin/python
# -*- coding: UTF-8 -*-

import nltk
import re
from src.infrastructure.wikipedia_service import WikipidiaService


class TextRobot:

    def __init__(self, search_term=None, search_prefix=None):
        self.search_term = search_term
        self.original_page = None
        self.treated_summary = None
        self.summary_sentences = []

    def run(self):
        self.fetch_page_from_wikipedia()
        self.sanitize_content()
        self.split_contents_into_sentences()

    def fetch_page_from_wikipedia(self):
        try:
            self.original_page = WikipidiaService.get_page(title=self.search_term, prefix_lang='pt')
        except Exception as error:
            raise Exception(f' Error while fetching text from wikipedia -> {error}')

    def sanitize_content(self):
        self.treated_summary = re.sub(r'\((?:\([^()]*\)|[^()])*\)', '', self.original_page.summary)

    def split_contents_into_sentences(self):
        summary = self.treated_summary
        self.summary_sentences = nltk.sent_tokenize(summary)
