import json
import random
from datetime import datetime, timedelta

collections = ["the-everyday-edit", "gulbahar", "noor", "rangrez", "rooh"]
categories = {
    "ready-to-wear": ["Kurtas", "Shirts", "Dresses", "Co-ords", "Occasion"],
    "unstitched": ["Printed Lawn", "Embroidered", "Cambric"],
    "accessories": ["Dupattas", "Bags", "Jewellery"]
}

adjectives = ["Classic", "Elegant", "Festive", "Floral", "Embroidered", "Raw Silk", "Cotton", "Velvet", "Signature", "Luxe", "Minimal", "Opulent", "Vibrant"]
nouns = ["Kurta", "Dress", "Tunic", "Shirt", "Suit", "Set", "Dupatta", "Clutch", "Earrings", "Necklace", "Tote", "Wrap"]

images = [
    "/images/ready-to-wear-editorial.png",
    "/images/unstitched-editorial.png",
    "/images/accessories-editorial.png",
    "/images/occasion-editorial.png",
    "/images/hero-luxury-courtyard.png",
    "/images/luxury_accessories_gold_1790427717901.jpg",
    "/images/luxury_formal_burgundy_1790427684372.jpg",
    "/images/luxury_formal_emerald_1790427707411.jpg",
    "/images/luxury_unstitched_flatlay_1790427695988.jpg"
]

products = []
pk_names = ["Zara", "Maira", "Bela", "Darya", "Neelam", "Sitara", "Aangan", "Sahar", "Kiran", "Sadaf", "Rooh", "Zoya", "Aisha", "Haya", "Meher", "Rani", "Nadia", "Sana", "Alina", "Laila"]

count = 1
for cat, subcats in categories.items():
    for subcat in subcats:
        for _ in range(random.randint(3, 5)):
            name = f"{random.choice(pk_names)} {random.choice(adjectives)} {subcat.split(' ')[-1]}"
            slug = name.lower().replace(" ", "-") + f"-{count}"
            price = random.randint(30, 250) * 100
            is_sale = random.random() < 0.3
            compareAt = price + (random.randint(20, 50) * 100) if is_sale else None
            badge = "Sale" if is_sale else random.choice([None, "New in", "Bestseller", "Limited", None, None])
            
            p = {
                "id": f"fw-{count:03d}",
                "slug": slug,
                "name": name,
                "category": cat,
                "subcategory": subcat,
                "collection": random.choice(collections),
                "price": price,
                "compareAt": compareAt,
                "badge": badge,
                "sizes": ["S", "M", "L"] if cat == "ready-to-wear" else ["3-piece"] if cat == "unstitched" else ["One size"],
                "colors": random.sample(["Rose", "Gold", "Ivory", "Teal", "Onyx", "Pearl", "Ruby", "Jade", "Silver", "Plum"], random.randint(1, 3)),
                "fabric": random.choice(["Cotton", "Silk", "Lawn", "Cambric", "Velvet", "Chiffon", "Organza"]),
                "availability": random.choice(["in-stock", "low-stock"]),
                "bestSelling": random.randint(10, 100),
                "date": (datetime.now() - timedelta(days=random.randint(1, 90))).strftime("%Y-%m-%d"),
                "images": random.sample(images, 2),
                "description": f"A beautiful {name.lower()} crafted for the modern wardrobe."
            }
            products.append(p)
            count += 1

with open(r'artifacts\fatima-wardrobe\src\data\products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=2)

print(f"Generated {len(products)} strictly ULTRA LUXURY eastern products!")
