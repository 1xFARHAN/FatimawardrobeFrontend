import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Pattern to find and remove the announcement bar
pattern = r'<div\s*className="bg-\[#b9ced5\] py-2 text-center text-\[10px\] tracking-\[\.08em\] text-\[#24383c\]"\s*data-testid="announcement-bar"\s*>.*?</div>'
replacement = ''

if re.search(pattern, text, re.DOTALL):
    text = re.sub(pattern, replacement, text, flags=re.DOTALL)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Announcement bar removed successfully!")
else:
    print("Could not find announcement bar.")
