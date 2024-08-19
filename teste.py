import re

string = 'eu nasci em 1994 e a michiko em 2000'

print(re.sub(r'[0-9]', 'a', string))
# print(string)
