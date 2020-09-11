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

    def __init__(self):
        """
        """
        pass

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

        with open(
                os.path.join(
                    os.path.dirname(self._file_path),
                    __provider + '.html'),
                'w') as __file:
            __file.write(__text)

        return item
