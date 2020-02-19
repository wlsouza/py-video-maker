# !usr/bin/python
# -*- coding: UTF-8 -*-


from src.infrastructure.google_service import GoogleService


class ImageRobot:

    def __init__(self, video):
        self.search_term = video.search_term
        self.sentences = video.sentences

    def run(self):
        self.fetch_imagens_of_sentences()

    def fetch_imagens_of_sentences(self):
        for sentence in self.sentences:
            query = f'{self.search_term} {sentence.keywords[0]}'
            sentence.images = GoogleService.fetch_google_images(query)
