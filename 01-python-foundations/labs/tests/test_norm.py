from norm import normalize


# Wrap our asserts inside functions that start with 'test_'
def test_standard_name():
    assert normalize("John") == "john"


def test_messy_name():
    assert normalize(" hElLo ") == "hello"


def test_edge_case():
    assert normalize(" ABC ") == "abc"
