python_sources()


resources(
    name="test-fixtures",
    sources=[
        "test.common-lisp-repl",
    ]
)


python_tests(
    name="tests0",
    dependencies=[
        "//:lib",
        ":test-fixtures",
    ],
)
