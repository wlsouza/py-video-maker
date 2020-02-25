# !usr/bin/python
# -*- coding: UTF-8 -*-

import wikipediaapi


class WikipediaService:

    @staticmethod
    def get_page(title, prefix_lang='en'):
        wiki_wiki = wikipediaapi.Wikipedia(prefix_lang)
        result_page = wiki_wiki.page(title=title)
        if result_page.exists():
            return result_page
        else:
            raise Exception('No page founded')
