# !usr/bin/python
# -*- coding: UTF-8 -*-

from src.domain.text_robot import TextRobot
from src.domain.image_robot import ImageRobot
from src.infrastructure.state_service import StateService


class Orchestrator:

    def __init__(self, video):
        self.video = self.check_stored_video(video)
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
                if self.video.state < state:
                    robot.run()
                    self.video.state = state
                    StateService.save_video_state(self.video)
        except Exception as error:
            raise Exception(f'Error at Orchestrator() while run the robots. -> {error}')


    def check_stored_video(self, video):
        """
        Check if this video already exists in a pkl file and if yes, return it.
        :param video: instance of Video()
        :return: Return a instance of Video()
        """
        stored_video = StateService.load_video_state(video)
        return stored_video if stored_video else video
