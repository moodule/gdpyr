# -*- coding: utf-8 -*-

"""
=========
Pipelines
=========

Exporting data.
"""

from __future__ import division, print_function, absolute_import

import os

#####################################################################
# RAW
#####################################################################

class RawPipeline(object):

    def __init__(self, path: str) -> None:
        """
        Initiate the output according to the calling spider.
        """
        self._path = path

    @classmethod
    def from_crawler(
            cls,
            crawler):
        """
        """
        return cls(
            path=os.path.realpath(crawler.settings.get(
                'EXPORT_FOLDER_PATH',
                './documents/')))

    def process_item(
            self,
            item,
            spider):
        """
        """
        __provider = ''.join(item.get(
            'provider',
            ['none']))
        __text = ''.join(item.get(
            'text',
            ['']))
        __file_path = os.path.join(
            self._path,
            getattr(spider, 'name', 'default'),
            __provider + '.html')

        with open(__file_path, 'w') as __file:
            __file.write(__text)

        return item
