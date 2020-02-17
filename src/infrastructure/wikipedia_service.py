# !usr/bin/python
# -*- coding: UTF-8 -*-

import wikipediaapi


class WikipidiaService:

    @staticmethod
    def get_page(self, title, prefix_lang='en'):
        wiki_wiki = wikipediaapi.Wikipedia(prefix_lang)
        result_page = wiki_wiki.page(title)
        return result_page