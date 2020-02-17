# !usr/bin/python
# -*- coding: UTF-8 -*-

from src.domain.text_robot import TextRobot

class Orchestrator:

    def __init__(self, search_term=None, search_prefix=None):
        self.search_term = search_term
        self.search_prefix = search_prefix
        self.text_robot = TextRobot(self.search_term, self.search_prefix)

    def run(self):
        self.text_robot.run()
