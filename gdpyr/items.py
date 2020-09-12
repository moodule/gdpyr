# -*- coding: utf-8 -*-

"""
==============
Legal Document
==============

Base class for all the specific legal documents.
"""

from __future__ import division, print_function, absolute_import

from itemloaders.processors import Identity, Join, MapCompose, TakeFirst
from scrapy.item import Field, Item
from scrapy.loader import ItemLoader

from gdpyr._wrangling import prettify_html

#####################################################################
# GENERIC AD
#####################################################################

class LegalDocument(Item):
    """
    In our case a legal documents is actually a whole html page.
    Data collectors usually isolate their legal engagements in
    dedicated web pages on their website.

    So there is no field to extract from the raw html, we just keep
    the provider's name (web domain) and url of the document for
    indexing.
    """
    # Source
    url = Field()
    title = Field()
    provider = Field()
    last_updated = Field()

    # Document
    text = Field()

class LegalDocumentLoader(ItemLoader):
    """
    Process the scraped data.

    The raw html is formatted so that opening tags are on new lines
    and their content indented.

    This allows line-by-line diff across versions.
    """

    default_output_processor = TakeFirst()

    url_in = Identity()
    url_out = Join()

    title_in = Identity()
    title_out = Join()

    provider_in = Identity()
    provider_out = Join()

    last_updated_in = Identity()
    last_updated_out = Join()

    text_in = MapCompose(prettify_html) # break lines
    text_out = Join()
