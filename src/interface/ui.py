#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os


class Ui:

    def __init__(self):
        self._search_data = {}

    def run(self):
        self.ask_search_term()
        self.ask_search_prefix()

    def ask_search_term(self):
        self.clear_screen()
        response = input(f'Type a Wikipedia search term of \'G\' to fetch google trends terms: ').strip()
        if response:
            if response.upper() == 'G':
                print(f'I\'m sorry, this function is not yet implemented.')
                # To Do: implement the search google trends method.
            else:
                self._search_data['search_term'] = response
        else:
            self.ask_search_term()

    def ask_search_prefix(self):
        self.clear_screen()
        options = {'1': 'Who is', '2': 'What is', '3': 'The history of', '0': 'CANCEL'}
        print(f'The search term is: {self._search_data.get("search_term")}')
        print(f'You must inform the prefix for your video:\n')
        for key, value in options.items():
            print(f'[{key}] - {value}')
        response = input(f'\nChoose one option {list(options.keys())}: ').strip()
        if response:
            if response in options:
                self._search_data['search_prefix'] = response
            else:
                self.ask_search_prefix()
        else:
            self.ask_search_prefix()

    @staticmethod
    def clear_screen():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')


if __name__ == '__main__':
    app = Ui()
    app.run()
