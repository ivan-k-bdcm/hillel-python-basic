import string


def is_palindrome(s: str) -> bool:
    if len(s) == 0 or len(s) == 1:
        return True

    start = 0
    end = 0
    for idx, i in enumerate(s):
        if i.isalnum():
            start = idx
            break

    for idx, i in enumerate(s[::-1]):
        if i.isalnum():
            end = len(s) - 1 - idx
            break

    if s[start].lower() == s[end].lower():
        return is_palindrome(s[start + 1:end])
    return False


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
