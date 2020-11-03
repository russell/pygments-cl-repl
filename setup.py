from setuptools import setup, find_packages
from os import path

changelog_header = """
Changelog
=========

"""

desc_file = path.join(path.dirname(__file__), "README.rst")
changelog_file = path.join(path.dirname(__file__), "CHANGELOG.rst")
description = (open(desc_file).read()
               + changelog_header
               + open(changelog_file).read())

version = '0.2'

setup(
    name='pygments-cl-repl',
    version=version,
    description="Pygments lexer for Common Lisp REPL",
    long_description=description,
    license='GPLv3+',
    author='Russell Sim',
    author_email='russell.sim@gmail.com',
    url='https://github.com/russell/pygments-cl-repl',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite='pygments_cl_repl.test.suite',
    install_requires=[
        # -*- Extra requirements: -*-
        'pygments',
    ],
    entry_points={
        'pygments.lexers':
        'common-lisp-repl=pygments_cl_repl:CommonLispREPLLexer'}
)
