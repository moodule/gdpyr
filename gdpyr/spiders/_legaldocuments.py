# -*- coding: utf-8 -*-

"""
===============
Legal Documents
===============

Scrape and version the explicit commitments of companies.

Especially the commitments regarding personal privacy, put into
light by the European GDPR.
"""

from __future__ import division, print_function, absolute_import

from typing import Iterator

from scrapy.http import Request, Response
from scrapy.item import Item
from scrapy.spiders import Spider

from gdpyr.items import LegalDocument, LegalDocumentLoader

#####################################################################
# SPIDER
#####################################################################

class LegalDocumentsSpider(Spider):
    name = 'legal_documents'
    project = 'gdpr'

    #################################################################
    # CRAWLING METHODS
    #################################################################

    def __init__(
            self,
            *args: str,
            **kwargs: str) -> None:
        """
        Initiate the scraping env.
        It is meant to be subclassed by each specific spider.

        Parameters
        ----------
        args: str.
            Command line arguments, passed by the scrapy shell.
        kwargs: str.
            Command line arguments, passed by the scrapy shell.

        Returns
        -------
        out: None.
        """
        super(LegalDocumentsSpider, self).__init__(*args, **kwargs)

        # enable specific pipelines
        self._pipelines = ['RawPipeline']

        #############################################################
        # URLS
        #############################################################

        self.providers = {}

    def start_requests(
            self) -> Iterator:
        """
        Queue all the legal document's urls.

        Parameters
        ----------

        Returns
        -------
        out: Iterator.
            An iterator on successive http requests.
        """
        # forge the search urls & queue the requests
        for __provider, __url in self.providers.items():
            self.log('[{provider}] requesting...'.format(
                provider=__provider))
            yield Request(
                url=__url,
                callback=self.parse,
                meta={'provider': __provider})

    def parse(
            self,
            response: Response) -> Item:
        """
        Extract the whole html code from the queried web page.

        Parameters
        ----------
        response: Response.
            The server response to the scraping request.

        Returns
        -------
        out: Item.
            An item representing the webpage: full markup + metadata.
        """
        __provider = response.meta.get(
            'provider',
            'none')

        self.log('[{provider}] parsing...'.format(
            provider = __provider))

        __loader = LegalDocumentLoader(
            item=LegalDocument(),
            response=response)

        __loader.add_value('url', response.url)
        __loader.add_value('provider', __provider)
        __loader.add_xpath('text', '//body')

        return __loader.load_item()
