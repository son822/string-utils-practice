def reverse_words(sentence):
    """Reverse the order of words in a sentence."""
    return " ".join(sentence.split()[::-1])


def is_palindrome(text):
    """Check whether text reads the same forwards and backwards, ignoring case and spaces."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def count_vowels(text):
    """Count the number of vowels (a, e, i, o, u) in text, case-insensitive."""
    return sum(1 for ch in text.lower() if ch in "aeiou")


def title_case(text):
    """Capitalize the first letter of every word in text."""
    return " ".join(word.capitalize() for word in text.split())
