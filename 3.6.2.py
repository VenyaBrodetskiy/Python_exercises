import requests
with open('input.txt', 'r') as file:
    link = file.read().strip()
print(link)

folder = 'https://stepic.org/media/attachments/course67/3.6.3/'

file_text = requests.get(link).text
print(file_text)
while file_text[:2] != 'We':
    link = file_text
    file_text = requests.get(folder+link).text
    print(file_text)
with open('output.txt', 'w') as file:
    file.write(file_text)