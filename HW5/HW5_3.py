import string

user_str = input("Enter string: ").strip()

cleand_str = ''.join(ch for ch in user_str if ch not in string.punctuation)

hash_tag_str = '#' + ''.join(cleand_str.title().split())

hash_tag_str = hash_tag_str[:140]

print(hash_tag_str)
