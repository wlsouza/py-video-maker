# !usr/bin/python
# -*- coding: UTF-8 -*-

from src.domain.text_robot import TextRobot


class Orchestrator:

    def __init__(self, video):
        self.text_robot = TextRobot(video)

    def run(self):
        self.text_robot.run()
