# !/usr/bin/python
# -*- coding: UTF-8 -*-

import pickle


class StateService:

    @staticmethod
    def save_video_state(video):
        """
        Save a pkl archive at src/storage containing a serialized instance of Video().
        :param video: Instance of Video()
        :return: None
        """
        try:
            file_name = f'../storage/{video.title} {video.language_prefix}.pkl'.replace(' ', '_')
            with open(file_name, 'wb') as file:
                pickle.dump(video, file)
        except Exception as error:
            raise Exception(f'Error at StateService() while dumping the video. -> {error}')

    @staticmethod
    def load_video_state(video):
        """
        Load a pkl archive containing a serialized instance of Video() from src/storage.
        :param video: Instance of Video()
        :return: None Return a instance of Video()
        """
        try:
            file_name = f'../storage/{video.title} {video.language_prefix}.pkl'.replace(' ', '_')
            with open(file_name, 'rb') as file:
                stored_video = pickle.load(file)
            return stored_video
        except IOError as error:
            # raise Exception(f'Error at StateService() while loading the video. -> {error}')
            return None
