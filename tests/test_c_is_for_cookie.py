
from c_is_for_cookie import longest
from c_is_for_cookie.cli import main


def test_main():
    assert main([]) == 0


def test_longest():
    assert longest([b'a', b'bc', b'abc']) == b'abc'
