import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. EditorialBanner image
text = text.replace(
    'className="absolute inset-0 h-full w-full object-cover opacity-100"',
    'className="absolute inset-0 h-full w-full object-cover object-top opacity-100"'
)

# 2. PromoTile image
text = text.replace(
    'className="aspect-[1.15] h-full w-full object-cover transition duration-700 group-hover:scale-[1.04]"',
    'className="aspect-[1.15] h-full w-full object-cover object-top transition duration-700 group-hover:scale-[1.04]"'
)

# 3. CollectionPage header banner image
text = text.replace(
    'className="absolute inset-0 h-full w-full object-cover"',
    'className="absolute inset-0 h-full w-full object-cover object-top"'
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed object-top positioning on all banners and promo tiles")
