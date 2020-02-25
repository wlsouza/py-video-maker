# !/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import pickle
import urllib3
from PIL import Image

class StorageService:

    @staticmethod
    def save_video_state(video, path):
        """
        Save a pkl archive at src/storage containing a serialized instance of Video().
        :param video: Instance of Video()
        :param path: Path of the video.
        :return: None
        """
        try:
            if not os.path.exists(path):
                os.makedirs(path)
            file_name = f'{path}/video.pkl'
            with open(file_name, 'wb') as file:
                pickle.dump(video, file)
        except Exception as error:
            raise Exception(f'Error at StorageService() while dumping the video. -> {error}')

    @staticmethod
    def load_video_state(path):
        """
        Load a pkl archive containing a serialized instance of Video() from src/storage.
        :param path: path of the video.
        :return: None Return a instance of Video()
        """
        try:
            file_name = f'{path}/video.pkl'
            with open(file_name, 'rb') as file:
                stored_video = pickle.load(file)
            return stored_video
        except IOError as error:
            # raise Exception(f'Error at StateService() while loading the video. -> {error}')
            return None

    @staticmethod
    def download_image_from_url(url, name, path, automatic_extension=False):
        try:
            if not os.path.exists(path):
                os.makedirs(path)
            http = urllib3.PoolManager(headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) ..'})
            response = http.urlopen('GET', url)
            if automatic_extension:
                content_type = response.getheader('content-type')  # get content-type to find extension of file
                extension = content_type.split('/')[1]
                name = f'{name.split(".")[0]}.{extension}'
            file_name = f'{path}/{name}'
            image_data = response.data
            with open(file_name, "wb") as file:
                file.write(image_data)
        except Exception as error:
            raise Exception(f'Error at StorageService() while downloading the image. -> {error}')

    @staticmethod
    def save_image(image, path, name, format=None):
        """
        Save a image on storage.
        :param name: Image name.
        :param image: Image to be saved.
        :param path: Image path.
        :return: None
        """
        try:
            if not os.path.exists(path):
                os.makedirs(path)
            file_name = f'{path}/{name}'
            image.save(file_name, format)
        except Exception as error:
            raise Exception(f'Error at StorageService() while dumping the video. -> {error}')


if __name__ == '__main__':
    StorageService.download_image_from_url(url='https://www.pngfind.com/pngs/m/655-6556314_pica-pau-do-filme-png-download-pica-pau.png', name='picapau', path='teste')
