# -*- coding: utf-8 -*-

"""
===
CLI
===

Console script.
"""

from __future__ import absolute_import, division, print_function

import argparse

#####################################################################
# CLI
#####################################################################

def main():
    """
    An alternative to the scrapy shell / scrapy crawl.
    Allows to launch several scraping jobs at once.

    Parameters
    ----------

    Returns
    -------
    out: None.
    """
    parser = argparse.ArgumentParser(
        description='GDPyR monitors legal commitments of data-processors.')
    parser.add_argument(
        '-u',
        '--url',
        help='Url to a legal document.',
        required=False)

    args = parser.parse_args()

if __name__ == "__main__":
    main()
