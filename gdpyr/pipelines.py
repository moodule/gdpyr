# -*- coding: utf-8 -*-

"""
=========
Pipelines
=========

Exporting data.
"""

from __future__ import division, print_function, absolute_import

import os

from scrapy.crawler import Crawler
from scrapy.item import Item
from scrapy.spiders import Spider

#####################################################################
# RAW
#####################################################################

class RawPipeline(object):

    def __init__(self, path: str) -> None:
        """
        Direct the output to the folder matching the type of
        legal document that is being scraped.

        Parameters
        ----------
        path: str.
            The path to the parent folder of the output files.

        Returns
        -------
        out: None.
        """
        self._path = path

    @classmethod
    def from_crawler(
            cls,
            crawler: Crawler):
        """
        Get the export path from the settings.

        Parameters
        ----------
        cls: Class.
        crawler: Crawler.
            The current crawling handler.

        Returns
        -------
        out: RawPipeline.
        """
        return cls(
            path=os.path.realpath(crawler.settings.get(
                'EXPORT_FOLDER_PATH',
                './documents/')))

    def process_item(
            self,
            item: Item,
            spider: Spider) -> Item:
        """
        Save the whole html page to a text file.

        Parameters
        ----------
        item: Item.
            The scraped item, ie the full web page + meta data.
        spider: Spider.
            The spider, one per document type.

        Returns
        -------
        out: Item.
            The input item, unscathed.
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
