import re
import json

filepath_json = r'artifacts\fatima-wardrobe\src\data\banners.json'

with open(filepath_json, 'r', encoding='utf-8') as f:
    banners = json.load(f)

banners[0]['objectPosition'] = 'object-[85%_top] md:object-top'
banners[1]['objectPosition'] = 'object-center md:object-top'
banners[2]['objectPosition'] = 'object-center md:object-top'

with open(filepath_json, 'w', encoding='utf-8') as f:
    json.dump(banners, f, indent=2)

filepath_app = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath_app, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the className in Hero
pattern = r'className="absolute inset-0 h-full w-full object-cover object-top opacity-90"'
# In TSX, we'll construct the className dynamically
repl = 'className={`absolute inset-0 h-full w-full object-cover opacity-90 ${item.objectPosition || "object-top"}`}'

if re.search(pattern, text):
    text = re.sub(pattern, repl, text)
    with open(filepath_app, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Hero image position updated!")
else:
    print("Hero image pattern not found!")
