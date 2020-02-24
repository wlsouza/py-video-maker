# !usr/bin/python
# -*- coding: UTF-8 -*-

from src.domain.image import Image
from src.infrastructure.google_service import GoogleService
from src.infrastructure.storage_service import StorageService


class ImageRobot:

    def __init__(self, video):
        self.video = video
        self.path = f'{self.video.path}/images'

    def run(self):
        self.fetch_images_of_sentences()
        self.download_and_save_images()

    def fetch_images_of_sentences(self):
        saved_images = []  # list to avoid repeated images.
        for sentence_index, sentence in enumerate(self.video.sentences):
            query = f'{self.video.search_term} {sentence.keywords[0]}'
            sentence_images = GoogleService.fetch_google_images(query)
            for image in sentence_images:
                if image.get('link') not in saved_images:
                    image_extension = image.get('fileFormat').split('/')[1]
                    image_name = f'{sentence_index}-original.{image_extension}'
                    image_path = f'{self.video.path}/images/'
                    sentence.image = Image(name=image_name, path=image_path, url=image.get('link'))
                    saved_images.append(image.get('link'))
                    break

    def download_and_save_images(self):
        for sentence in self.video.sentences:
            image = sentence.image
            StorageService.download_image_from_url(url=image.url, name=image.name, path=image.path, automatic_extension=False)
            print(f'Image {image.name} downloaded with success.')
