import string

user_range = input("Enter alphabetic range: ").strip()

start, end = user_range.split("-")
start_index = string.ascii_letters.index(start)
end_index = string.ascii_letters.index(end)

print(string.ascii_letters[start_index:end_index + 1])
