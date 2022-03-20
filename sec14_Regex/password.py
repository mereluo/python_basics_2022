import re

password = input("type your password here: ")
pattern = re.compile(r"[A-Za-z0-9$%#@]{7,}\d$")

a = pattern.search(password)

if a is None:
    print("your password is not valid.")
else:
    print("your password is recorded.")
