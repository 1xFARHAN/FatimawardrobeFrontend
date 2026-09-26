import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Change object-center to object-top for the Hero image so the model's head isn't cropped
hero_img_pattern = r'className="absolute inset-0 h-full w-full object-cover object-center opacity-90"'
hero_img_replacement = r'className="absolute inset-0 h-full w-full object-cover object-top opacity-90"'

text = re.sub(hero_img_pattern, hero_img_replacement, text)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Hero image positioning fixed to object-top")
