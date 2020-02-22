# !usr/bin/python
# -*- coding: UTF-8 -*-


from src.infrastructure.google_service import GoogleService
from src.infrastructure.storage_service import StorageService


class ImageRobot:

    def __init__(self, video):
        self.video = video
        self.path = f'{self.video.path}/images'

    def run(self):
        # self.fetch_images_of_sentences()
        self.download_and_save_images()

    def fetch_images_of_sentences(self):
        for sentence in self.video.sentences:
            query = f'{self.video.search_term} {sentence.keywords[0]}'
            sentence.images = GoogleService.fetch_google_images(query)

    def download_and_save_images(self):
        downloaded_images = []
        for sentence_index, sentence in enumerate(self.video.sentences):
            for image_index, image_url in enumerate(sentence.images):
                if image_url in downloaded_images:
                    print(f'Image[{sentence_index}|{image_index}] already downloaded to another sentence.')
                    continue
                else:
                    image_name = f'{sentence_index}-original'
                    StorageService.download_image_from_url(url=image_url, name=image_name, path=self.path)
                    print(f'Image[{sentence_index}|{image_index}] downloaded with success.')
                    break
