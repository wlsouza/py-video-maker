# !usr/bin/python
# -*- coding: UTF-8 -*-

from src.domain.text_robot import TextRobot


class Orchestrator:

    def __init__(self, video):
        self.text_robot = TextRobot(video)

    def run(self):
        """
        It just executes the process calling the robots in sequence.
        :return: None
        """
        self.text_robot.run()
