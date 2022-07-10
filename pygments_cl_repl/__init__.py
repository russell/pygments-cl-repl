# -*- coding: utf-8 -*-
import re
from io import StringIO
from string import whitespace

from pygments.lexer import Lexer, do_insertions
from pygments.lexers.functional import CommonLispLexer
from pygments.token import Generic

atom_end = set("()\"'") | set(whitespace)
line_re = re.compile(".*?\n")


class sexp_reader:
    """This is a dumb parser that will parse one sexp.

    based on Paul Bonser's example parser
    https://gist.github.com/pib/240957/
    """

    def __init__(self):
        self.stack = [[]]
        self.sexp_string = StringIO()
        self.rest_string = StringIO()

    def read(self, stream):
        """Will parse the stream until a complete sexp has been read.

        Returns True until state is complete.
        """
        stack = self.stack
        while True:
            if stack[0]:  # will be true once one sexp has been parsed
                self.rest_string = stream
                return False
            c = stream.read(1)
            if not c:
                # no more stream and no complete sexp
                return True
            reading = type(stack[-1])
            self.sexp_string.write(c)

            if reading == tuple:
                if c in atom_end:
                    atom = stack.pop()
                    stack[-1].append(atom)
                    reading = type(stack[-1])
            if reading == list:
                if c == "(":
                    stack.append([])
                elif c == ")":
                    stack[-2].append(stack.pop())
                elif c == '"':
                    stack.append("")
                elif c == "'":
                    continue
                elif c in whitespace:
                    continue
                else:
                    stack.append(tuple())
            elif reading == str:
                if c == '"':
                    stack.pop()
                # escaped char coming up, so read ahead
                elif c == "\\":
                    self.sexp_string.write(stream.read(1))

    def rest(self):
        """Return the unparsed remainder of the stream as a string."""
        return self.rest_string.read()

    def sexp(self):
        """Return the parsed sexp as a string."""
        self.sexp_string.seek(0)
        return self.sexp_string.read()


class CommonLispREPLLexer(Lexer):
    """Lexer for lisp REPL sessions that works with different command prompts.

    Currently supports: ECL, SBCL, CCL, SLIME and IELM
    """

    name = "Common Lisp REPL"
    aliases = ["common-lisp-repl"]
    filenames = ["*.common-lisp-repl"]
    mimetypes = ["text/x-common-lisp-repl"]

    def get_tokens_unprocessed(self, text):
        cl_lexer = CommonLispLexer(**self.options)

        pos = 0
        curcode = ""
        insertions = []
        iterator = line_re.finditer(text)

        while True:
            try:
                match = next(iterator)
                line = match.group()
                start = match.start()
            except StopIteration:
                # the line_re expression won't work in the case of the
                # string "a\nb" so make sure that the remainder of the
                # output is processed
                if match and match.end() < len(text):
                    start = match.end()
                    line = text[match.end() :]
                    match = None
                else:
                    return
            m = re.match(r"^((?:[^\s*?>:]*[*?>:]) )(.*\n?)", line)

            if m:
                line = ""
                # To support output lexers (say diff output), the output
                # needs to be broken by prompts whenever the output lexer
                # changes.
                if not insertions:
                    pos = start

                insertions.append((len(curcode), [(0, Generic.Prompt, m.group(1))]))

                # skip parser when line is empty
                if re.match(r"^\s*$", m.group(2)):
                    line = m.group(2)
                else:
                    # read out the whole sexp after the prompt, if it's a
                    # muliline expression then keep reading until there is
                    # a complete expression
                    string_stream = StringIO(m.group(2))
                    reader = sexp_reader()
                    while reader.read(string_stream):
                        try:
                            match = next(iterator)
                            string_stream = StringIO(match.group())
                        except StopIteration:
                            break
                    curcode += reader.sexp()
                    line = reader.rest()

            if insertions:
                if curcode:
                    toks = cl_lexer.get_tokens_unprocessed(curcode)
                for i, t, v in do_insertions(insertions, toks):
                    yield pos + i, t, v
            if line:
                yield start, Generic.Output, line
            insertions = []
            curcode = ""
