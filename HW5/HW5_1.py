import string
import keyword

user_str = input("Enter string: ").strip()

user_str_is_valid = True

if user_str in keyword.kwlist:
    user_str_is_valid = False
elif user_str.count(' ') != 0:
    user_str_is_valid = False
elif user_str[0].isdigit():
    user_str_is_valid = False
elif user_str.lower() != user_str:
    user_str_is_valid = False
elif user_str.count('_') == len(user_str) and len(user_str) > 1:
    user_str_is_valid = False
else:
    for ch in user_str:
        if ch == '_':
            continue
        if ch in string.punctuation:
            user_str_is_valid = False
            break

print(user_str_is_valid)
