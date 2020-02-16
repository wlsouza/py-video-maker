#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Ui:

    def __init__(self):
        self._search_data = {}

    def run(self):
        self.ask()

    def ask(self):
        response = input(f'Type a Wikipedia search term of \'G\' to fetch google trends terms: ')
        if response:
            if response.upper() == 'G':
                print(f'I\'m sorry, this function is not yet implemented.')
                # To Do: implement the search google trends method.
            else:
                self._search_data['search_term'] = response
                # print(self._search_data['search_term'])
        else:
            self.ask()


if __name__ == '__main__':
    app = Ui()
    app.run()
