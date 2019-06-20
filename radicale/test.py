import re

with open('example.ics', 'r') as fp:
    content = fp.read()

regex = re.compile(r"(?:BEGIN:VEVENT).+?(?:END:VEVENT)", flags=re.S)
matches = re.findall(regex, content)
print(matches[0])
