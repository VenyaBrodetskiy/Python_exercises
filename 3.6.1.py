import requests
with open('input.txt', 'r') as file:
    s = file.read().strip()
print(s)
s = requests.get(s)
print(len(s.text.splitlines()))