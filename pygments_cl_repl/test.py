# -*- coding: utf-8 -*-
# Based on the pygments test_examplefiles.py

# Copyright (c) 2006-2013 by the respective authors (see AUTHORS file).
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:

# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.

# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in
#   the documentation and/or other materials provided with the
#   distribution.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from os import path
import difflib
import unittest

from pygments.token import Error
from pygments.util import b
from pygments_cl_repl import CommonLispREPLLexer

DIR = path.dirname(__file__)


class CLREPLTestCase(unittest.TestCase):
    def test_with_example_file(self):
        filename = path.join(DIR, 'test.common-lisp-repl')
        lexer = CommonLispREPLLexer()
        fp = open(filename, 'rb')
        try:
            text = fp.read()
        finally:
            fp.close()
        text = text.replace(b('\r\n'), b('\n'))
        text = text.strip(b('\n')) + b('\n')
        try:
            text = text.decode('utf-8')
            if text.startswith(u'\ufeff'):
                text = text[len(u'\ufeff'):]
        except UnicodeError:
            text = text.decode('latin1')
        ntext = []
        tokens = []
        for type, val in lexer.get_tokens(text):
            ntext.append(val)
            self.assertNotEqual(
                type, Error,
                'error %r at position %d' % (val, len(u''.join(ntext))))
            tokens.append((type, val))
        self.assertEqual(
            u''.join(ntext), text,
            '\n'.join(difflib.unified_diff(u''.join(ntext).splitlines(),
                                           text.splitlines())))


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(CLREPLTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
