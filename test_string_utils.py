from string_utils import reverse_words, is_palindrome, count_vowels, title_case


def test_reverse_words():
    assert reverse_words("hello world") == "world hello"


def test_is_palindrome():
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("hello") is False


def test_count_vowels():
    assert count_vowels("Hello World") == 3
