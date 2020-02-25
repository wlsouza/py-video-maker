# !usr/bin/python
# -*- coding: UTF-8 -*-


import re
import nltk
from multi_rake import Rake
from src.domain.sentence import Sentence
from src.infrastructure.wikipedia_service import WikipediaService
from src.config import text_robot as config


class TextRobot:

    def __init__(self, video):
        self.video = video
        self._original_wiki_page = None
        self._treated_summary = None

    def run(self):
        """
        It just executes the process calling the methods in sequence.
        :return: None
        """
        self._fetch_wikipedia_page()
        self._sanitize_text()
        self._split_contents_into_sentences()
        self._fetch_all_sentences_keywords()

    def _fetch_wikipedia_page(self):
        """
        Fetch on wikipedia the search term.
        After get the page, the method inserts it in the _original_wiki_page variable.
        :return: None
        """
        try:
            self._original_wiki_page = WikipediaService.get_page(title=self.video.search_term, prefix_lang=self.video.language_prefix)
        except Exception as error:
            raise Exception(f' Error while fetching text from wikipedia -> {error}')

    def _sanitize_text(self):
        """
        Remove dates from the wikipedia summary and inserts it in the _treated_summary variable.
        :return: None
        """
        text = self._original_wiki_page.summary
        self._treated_summary = re.sub(r'\((?:\([^()]*\)|[^()])*\)', '', text)

    def _split_contents_into_sentences(self):
        """
        Tokenize the sentences of _treated_summary variable.
        After that, the method create a Sentence() object with the
        sentence text for each sentence in the _treated_summary variable.
        :return: None
        """
        text = self._treated_summary
        sentences = nltk.sent_tokenize(text)
        for sentence_index, sentence_text in enumerate(sentences):
            if sentence_index < config.get('max_sentences', 0):
                sentence = Sentence(text=sentence_text)
                self.video.sentences.append(sentence)

    def _fetch_all_sentences_keywords(self):
        """
        For each sentence object in self.video.sentences, the method gets the keywords and saves them in sentence.keywords
        :return: None
        """
        rake = Rake()
        for sentence in self.video.sentences:
            keywords_result = rake.apply(sentence.text, text_for_stopwords=None)
            keywords = [keyword[0] for keyword in keywords_result]  # Getting just keywords, without accuracy
            sentence.keywords = keywords
