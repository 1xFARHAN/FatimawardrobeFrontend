import json

filepath = r'artifacts\fatima-wardrobe\src\data\products.json'

with open(filepath, 'r', encoding='utf-8') as f:
    products = json.load(f)

# Filter out the product that uses hero-luxury-courtyard.png
filtered_products = [p for p in products if p['images'][0] != '/images/hero-luxury-courtyard.png']

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(filtered_products, f, indent=2)

print(f"Removed product. Total products remaining: {len(filtered_products)}")
