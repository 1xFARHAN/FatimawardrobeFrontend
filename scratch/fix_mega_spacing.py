import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace padding
text = text.replace('className="mx-auto w-full px-8 py-10"', 'className="mx-auto w-full px-6 py-6"')
# Replace gap
text = text.replace('className="flex items-start justify-center gap-6"', 'className="flex items-start justify-center gap-4"')
# Replace width
text = text.replace('className="group text-center flex flex-col items-center w-[220px]"', 'className="group text-center flex flex-col items-center w-[160px]"')
# Replace margin bottom
text = text.replace('className="aspect-square w-full overflow-hidden bg-[#f0e2d4] mb-5"', 'className="aspect-square w-full overflow-hidden bg-[#f0e2d4] mb-3"')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Mega menu spacing fixed!")
