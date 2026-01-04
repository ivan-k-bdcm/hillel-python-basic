import string


def is_palindrome(text: str) -> bool:
    """Check if string is palindrome"""

    text = text.lower()
    text = [ch for ch in text if ch not in string.punctuation and ch != ' ']

    return text == text[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
