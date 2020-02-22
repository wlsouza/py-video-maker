# !usr/bin/python
# -*- coding: UTF-8 -*-

from src.domain.text_robot import TextRobot
from src.domain.image_robot import ImageRobot
from src.infrastructure.storage_service import StorageService


class Orchestrator:

    def __init__(self, video):
        self.video = self._check_stored_video(video=video)
        self.robots = {
            1: TextRobot(self.video),
            2: ImageRobot(self.video)
        }

    def run(self):
        """
        Calls the robots and executes it if the video has not yet been processed by that robot.
        :return: None
        """
        try:
            for state, robot in self.robots.items():
                self.video.state = 1
                if self.video.state < state:
                    robot.run()
                    self.video.state = state
                    StorageService.save_video_state(video=self.video, path=self.video.path)
        except Exception as error:
            raise Exception(f'Error at Orchestrator() while run the robots. -> {error}')

    def _check_stored_video(self, video):
        """
        Check if this video already exists in a pkl file and if yes, return it.
        :param video: instance of Video()
        :return: Return a instance of Video()
        """
        stored_video = StorageService.load_video_state(path=video.path)
        return stored_video if stored_video else video
