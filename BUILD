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

resource(name="pyproject", source="pyproject.toml")

python_distribution(
    name="pygments-cl-repl",
    dependencies=[
        ":lib",
        ":docs",
    ],
    provides=python_artifact(
        name="pygments-cl-repl",
        version="0.2.1",

        entry_points={
            'pygments.lexers': ['common-lisp-repl=pygments_cl_repl:CommonLispREPLLexer'],
        }
    ),
)
