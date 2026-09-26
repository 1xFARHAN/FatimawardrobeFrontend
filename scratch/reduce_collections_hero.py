import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('min-h-[500px] md:min-h-[700px]', 'min-h-[400px] md:min-h-[550px]')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Hero height reduced!")
