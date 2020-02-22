# !/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
from src.domain.video import Video
from src.infrastructure.google_service import GoogleService
from src.application.orchestrator import Orchestrator


class Ui:

    def __init__(self):
        self.video = Video()

    def run(self):
        """
        It just executes the process calling the methods in sequence.
        :return: None
        """
        self._ask_search_term()
        self._ask_search_prefix()
        orchestrator = Orchestrator(self.video)
        orchestrator.run()

    def _ask_search_term(self):
        """
        Asks the user which search term they want to use to make the video.
        It also allows you to press G to search for the terms of google trends.
        After receiving the input, the method inserts the response in the video.search_term
        :return: None
        """
        response = None
        while not response:
            self.clear_screen()
            response = input(f'Type a Wikipedia search term or \'G\' to fetch google trends terms: ').strip()
            if response :
                if response.upper() == 'G':
                    response = self._ask_which_google_trend()
                self.video.search_term = response

    def _ask_which_google_trend(self):
        """
        Get a list of google trends and ask the user which search term they want
        :return: Return a title of google trend or None if the user choose CANCEL.
        """
        terms = GoogleService.get_google_trends_terms()
        terms_dict = {str(number+1): term for number, term in enumerate(terms)}
        terms_dict['0'] = 'CANCEL'  # adding an Cancel option
        response = None
        while response not in terms_dict.keys():
            self.clear_screen()
            for key, value in terms_dict.items():
                print(f'[{key}] - {value}')
            response = input(f'\nChoose one option {list(terms_dict.keys())}: ').strip()
        return terms_dict.get(response) if not response == '0' else None

    def _ask_search_prefix(self):
        """
        Asks the user which search prefix they want to use to make the video.
        After receiving the input, the method inserts the response in the video.search_prefix
        :return: None
        """
        options = {'1': 'Who is', '2': 'What is', '3': 'The history of', '0': 'CANCEL'}
        response = None
        while response not in options:
            print(f'The search term is: {self.video.search_term}')
            print(f'Now, you must inform the prefix for your video:\n')
            for key, value in options.items():
                print(f'[{key}] - {value}')
            response = input(f'\nChoose one option {list(options.keys())}: ').strip()
        if response == '0':
            sys.exit()
        else:
            self.video.search_prefix = options.get(response)

    @staticmethod
    def clear_screen():
        """
        Clear the console screen.
        :return: None
        """
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')


if __name__ == '__main__':
    app = Ui()
    app.run()
