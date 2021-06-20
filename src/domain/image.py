# !usr/bin/python
# -*- coding: UTF-8 -*-


class Image:

    def __init__(self, name, path, url):
        self.name = name
        self.path = path
        self.url = url

    @property
    def full_path(self):
        return self.path + self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f' {{ Name: {self.name}, \nPath: {self.path}, \nURL:{self.url} }}'
