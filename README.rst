================
pygments-cl-repl
================

Syntax coloring for Common Lisp REPL sessions
---------------------------------------------

Overview
========

This package provides a Pygments_ lexer for `Common Lisp REPL`_
sessions.  The lexer is published as an entry point and, once
installed, Pygments will pick it up automatically.

You can then use this lexer with Pygments::

    $ pygmentize -l common-lisp-repl pygments_cl_repl/test.common-lisp-repl

In Sphinx_ documents the lexer is selected with the ``highlight``
directive::

    .. highlight:: common-lisp-repl

.. _Common Lisp REPL: http://www.cliki.net/REPL
.. _Pygments: http://pygments.org/
.. _Sphinx: http://sphinx-doc.org/

Installation
============

Use your favorite installer to install pygments-cl-repl into the same
Python you have installed Pygments. For example::

    $ pip install pygments-cl-repl

To verify the installation run::

    $ pygmentize -L lexer | grep -i common-lisp-repl
    * common-lisp-repl:
        Common Lisp REPL (filenames *.common-lisp-repl)
