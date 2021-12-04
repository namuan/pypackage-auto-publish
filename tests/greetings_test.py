from pypackage_auto_publish.greetings import greet


def test_should_greet_user() -> None:
    assert greet("Bob") == "Hello Bob"
