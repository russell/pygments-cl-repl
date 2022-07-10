python_sources(
    name="lib",
    sources=["pygments_cl_repl/__init__.py"],
)

resources(
    name="docs",
    sources=[
        "README.rst",
        "CHANGELOG.rst",
        "LICENSE",
    ]
)

python_distribution(
    name="pygments-cl-repl",
    dependencies=[
        ":lib",
        ":docs",
    ],
    provides=python_artifact(
        name="pygments-cl-repl",
        version="0.2.1",
        description="Pygments lexer for Common Lisp REPL",

        requires_python = ">=3.7",
        license = "GPLv3+",
        readme = { "file": "README.rst", "content_type": "text/x-rst" },
        authors = [
            { "name": "Russell Sim", "email": "russell.sim@gmail.com" }
        ],
        home_page = "https://github.com/russell/pygments-cl-repl",
        classifiers = [
            'Development Status :: 4 - Beta',
            'Environment :: Plugins',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],

        urls = {
            "documentation": "https://russell.github.io/pygments-cl-repl/",
            "source": "https://github.com/russell/pygments-cl-repl",
            "tracker": "https://github.com/russell/pygments-cl-repl/issues",
        },
        entry_points={
            'pygments.lexers': ['common-lisp-repl=pygments_cl_repl:CommonLispREPLLexer'],
        }
    ),
    wheel_config_settings={"--global-option": ["--python-tag", "py37.py38.py39"]},
)
