# !usr/bin/python
# -*- coding: UTF-8 -*-

import feedparser
from googleapiclient.discovery import build
from src.credentials import custom_search_credential as credential


class GoogleService:

    @staticmethod
    def get_google_trends_terms():
        """
        Get the google trends in brazil
        :return: List of google trends (just the titles)
        """
        try:
            trends = feedparser.parse("https://trends.google.com/trends/trendingsearches/daily/rss?geo=BR")
            return [entry.get('title') for entry in trends.entries]
        except Exception as error:
            raise Exception(f' Error occurred while searching for google trends -> {error}')

    @staticmethod
    def fetch_google_images(query, max_results=4, **kwargs):
        """
        Search for a specific term in google images.
        :param query: Term that will be searched on google.
        :param max_results: Maximum amount of results
        :param kwargs: Parameters passed to the google API,
        for more details see: https://developers.google.com/custom-search/v1/cse/list#parameters
        :return: Returns a list of "images" if the search does not provide results
        """
        custom_search = build(serviceName='customsearch', version='v1', developerKey=credential.get('api_key')).cse()
        params = {
            'q': query,
            'cx': credential.get('search_engine_id'),
            'num': max_results,
            'searchType': 'image'
            # 'imgType': 'photo',
            # 'imgSize': 'large',
            # 'safe': 'medium'
        }
        if kwargs:
            params.update(kwargs)
        response = custom_search.list(**params).execute()
        response_items = response.get('items')
        return response_items

if __name__ == '__main__':
    teste = GoogleService.fetch_google_images('O homem aranha', 3)
    print(teste)