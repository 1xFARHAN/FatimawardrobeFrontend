import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Remove the component usage
text = re.sub(r'<InstagramGallery\s*/>', '', text)

# Remove the component definition
comp_pattern = r'function InstagramGallery\(\) \{.*?\n\s*\)\;\s*\}'
text = re.sub(comp_pattern, '', text, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Section removed")
