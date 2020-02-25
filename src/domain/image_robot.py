# !usr/bin/python
# -*- coding: UTF-8 -*-

from PIL import Image as PilImg
from PIL import ImageFilter
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
        self.treats_image_to_video()

    def fetch_images_of_sentences(self):
        saved_images = []  # list to avoid repeated images.
        for sentence_index, sentence in enumerate(self.video.sentences):
            # Search image on google
            query = f'{self.video.search_term} {sentence.keywords[0]}'
            fetched_image = GoogleService.fetch_google_images(query)
            for image in fetched_image:
                # Save raw_image into sentence
                if image.get('link') not in saved_images:
                    image_extension = image.get('fileFormat').split('/')[1]
                    image_name = f'{sentence_index}-original.{image_extension}'
                    image_path = f'{self.video.path}/images/original/'
                    sentence.raw_image = Image(name=image_name, path=image_path, url=image.get('link'))
                    saved_images.append(image.get('link'))
                    break

    def download_and_save_images(self):
        for sentence in self.video.sentences:
            image = sentence.raw_image
            StorageService.download_image_from_url(url=image.url, name=image.name, path=image.path, automatic_extension=False)
            print(f'Image {image.name} downloaded with success.')

    def treats_image_to_video(self):
        # Define target width and height
        video_width = self.video.video_width
        video_height = self.video.video_height

        for sentence_index, sentence in enumerate(self.video.sentences):
            # Open Original Image
            image = sentence.raw_image
            original_image = PilImg.open(f'{image.path}/{image.name}')

            # Resize but maintain the aspect ratio.
            resized_image = ImageRobot.resize_with_aspect_ratio(original_image, video_width, video_height)

            # Create the background
            background_image = original_image.filter(ImageFilter.GaussianBlur(radius=20))
            background_image = background_image.resize((1920, 1080))

            # Calculate position and compose the treated image
            position = (int((video_width - resized_image.width) / 2), int((video_height - resized_image.height) / 2))
            treated_image = background_image.copy()
            treated_image.paste(resized_image, position)

            # Save treated_image into sentence
            treated_image_extension = 'JPEG'
            treated_image_name = f'{sentence_index}-treated.{treated_image_extension}'
            treated_image_path = f'{self.video.path}/images/treated/'
            sentence.treated_image = Image(name=treated_image_name, path=treated_image_path, url=image.url)

            # Save treated image on storage
            StorageService.save_image(image=treated_image, path=treated_image_path, name=treated_image_name, format=treated_image_extension)

    @staticmethod
    def resize_with_aspect_ratio(image, target_width, target_height):
        """
        Resize but maintain the aspect ratio.
        :param image: Instance of image to be resized.
        :param target_width: Desired height (pixels)
        :param target_height: Desired height (pixels)
        :return: Instance of resized_image.
        """
        # calculate aspect ratio
        target_ratio = target_height / target_width
        img_ratio = image.height / image.width
        if target_ratio > img_ratio:
            # It must be fixed by width
            resize_width = target_width
            resize_height = round(resize_width * img_ratio)
        else:
            # Fixed by height
            resize_height = target_height
            resize_width = round(resize_height / img_ratio)
        # resize
        image_resized = image.resize((resize_width, resize_height), PilImg.LANCZOS)
        return image_resized
