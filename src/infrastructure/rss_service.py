# !/usr/bin/python
# -*- coding: UTF-8 -*-

import feedparser


class RssService:

    @staticmethod
    def get_google_trends_terms():
        try:
            trends = feedparser.parse("https://trends.google.com/trends/trendingsearches/daily/rss?geo=BR")
            return [entry.get('title') for entry in trends.entries]
        except Exception as error:
            raise Exception(f' Error occurred while searching for google trends -> {error}')
