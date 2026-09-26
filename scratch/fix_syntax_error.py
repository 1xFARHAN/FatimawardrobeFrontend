import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Fix the accidental backslashes
text = text.replace(r"isEven ? \'md:flex-row\' : \'md:flex-row-reverse\'", "isEven ? 'md:flex-row' : 'md:flex-row-reverse'")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Syntax error fixed!")
