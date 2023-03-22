from greeting import greeting


def test_greeting_with_person():
    assert greeting("John") == "Hello, John!"


def test_greeting_without_person():
    assert greeting() == "Hello, World!"
