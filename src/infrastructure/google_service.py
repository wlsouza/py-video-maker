# !usr/bin/python
# -*- coding: UTF-8 -*-

from googleapiclient.discovery import build
from src.credentials import custom_search_credential as credential


class GoogleService:

    @staticmethod
    def fetch_google_images(query, max_results=2, **kwargs):
        """
        Search for a specific term in google images.
        :param query: Term that will be searched on google.
        :param max_results: Maximum amount of results
        :param kwargs: Parameters passed to the google API,
        for more details see: https://developers.google.com/custom-search/v1/cse/list#parameters
        :return: Returns a list of Image or Name URLs if the search does not provide results
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
        print(response)
        response_items = response.get('items')
        if response_items:
            url_list = [item.get('link') for item in response_items]
            return url_list
