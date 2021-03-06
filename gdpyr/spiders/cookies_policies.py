# -*- coding: utf-8 -*-

"""
==============
Cookies Policy
==============

Scrape and version the cookies policies of web providers.

Cookies have some important implications on the privacy and anonymity
of web users. Web providers are expected to state the use they make of
cookies.
"""

from __future__ import division, print_function, absolute_import

from gdpyr.spiders._legaldocuments import LegalDocumentsSpider

#####################################################################
# SPIDER
#####################################################################

class CookiesPoliciesSpider(LegalDocumentsSpider):
    name = 'cookies_policies'

    #################################################################
    # CRAWLING METHODS
    #################################################################

    def __init__(
            self,
            *args: str,
            **kwargs: str) -> None:
        """
        List the cookies policy's urls.

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
        super(CookiesPoliciesSpider, self).__init__(*args, **kwargs)

        #############################################################
        # URLS
        #############################################################

        self.providers = {
            'airbnb': 'https://www.airbnb.com/terms/cookie_policy',
            'amazon': 'https://www.amazon.fr/gp/help/customer/display.html/?nodeId=201890250',
            'facebook': 'https://www.facebook.com/policies/cookies/',
            'google': 'https://policies.google.com/technologies/cookies',
            'linkedin': 'https://www.linkedin.com/legal/preview/cookie-policy',
            'stackoverflow': 'https://stackoverflow.com/legal/cookie-policy',
            'wikimedia': 'https://foundation.wikimedia.org/wiki/Cookie_statement',}
