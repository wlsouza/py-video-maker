# !usr/bin/python
# -*- coding: UTF-8 -*-

import nltk
import re
from multi_rake import Rake
from src.domain.sentence import Sentence
from src.infrastructure.wikipedia_service import WikipidiaService


class TextRobot:

    def __init__(self, search_term=None, search_prefix=None, prefix_lang='en'):
        self.search_term = search_term
        self.prefix_lang = prefix_lang
        self._original_page = None
        self._treated_summary = None
        self.sentences = []

    def run(self):
        self._fetch_page_from_wikipedia()
        self._sanitize_text()
        self._split_contents_into_sentences()
        self._fetch_all_sentences_keywords()

    def _fetch_page_from_wikipedia(self):
        try:
            self._original_page = WikipidiaService.get_page(title=self.search_term, prefix_lang=self.prefix_lang)
        except Exception as error:
            raise Exception(f' Error while fetching text from wikipedia -> {error}')

    def _sanitize_text(self):
        text = self._original_page.summary
        self._treated_summary = re.sub(r'\((?:\([^()]*\)|[^()])*\)', '', text)

    def _split_contents_into_sentences(self):
        text = self._treated_summary
        sentences = nltk.sent_tokenize(text)
        for sentence_text in sentences:
            sentence = Sentence(text=sentence_text)
            self.sentences.append(sentence)

    def _fetch_all_sentences_keywords(self):
        rake = Rake()
        for sentence in self.sentences:
            keywords_result = rake.apply(sentence.text, text_for_stopwords=None)
            keywords = [keyword[0] for keyword in keywords_result]  # Getting just keywords, without accuracy
            sentence.keywords = keywords
