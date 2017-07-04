#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Translate: A simple translator using the Google API
# Copyright (c) 2017 Pticon
#
# MIT License
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import urllib
import urllib2
import re
import HTMLParser


class Translate:

    def __init__(self):
        self.__base_uri = "http://translate.google.com/m?hl=%s&sl=%s&q=%s"
        self.__user_agent = {"User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0"}
        self.__rexpr = r'class="t0">(.*?)<'
        self.__html_parser = HTMLParser.HTMLParser()
        self.__lang = ('en', 'fr', 'nl', 'de', 'es')

    def set_user_agent(self, ua):
        """Replace the User Agent"""
        self.__user_agent ["User-Agent"] = ua

    def translate(self, txt, froml="auto", tol="auto"):
        """Returns the translated text using google translate"""

        txt = urllib.quote_plus(txt)
        link = self.__base_uri % (tol, froml, txt)
        request = urllib2.Request(link, headers=self.__user_agent)
        raw_data = urllib2.urlopen(request).read()

        data = raw_data.decode('utf-8')
        re_result = re.findall(self.__rexpr, data)

        if len(re_result) == 0:
            return ""

        return self.__html_parser.unescape(re_result[0])

    def parse_lang(self, code):
        """Parse the langage code and return a tuple (from, to)"""

        (froml, tol) = code.split("2")

        if not froml in self.__lang:
            froml = 'auto'

        if not tol in self.__lang:
            tol = 'auto'

        return (froml, tol)
