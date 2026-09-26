import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Bestsellers grid with a horizontal slider
bestseller_pattern = r'<div className="grid grid-cols-2 gap-x-3 gap-y-10 md:grid-cols-4 md:gap-x-5">\s*\{\[\.\.\.allProducts\]\s*\.sort\(\(a, b\) => b\.bestSelling - a\.bestSelling\)\s*\.slice\(0, 4\)\s*\.map\(\(p\) => \(\s*<ProductCard key=\{p\.id\} product=\{p\} />\s*\)\)\}\s*</div>'

bestseller_replacement = """<div className="flex overflow-x-auto gap-4 md:gap-6 snap-x snap-mandatory pb-8 [&::-webkit-scrollbar]:hidden [-ms-overflow-style:none] [scrollbar-width:none]">
          {[...allProducts]
            .sort((a, b) => b.bestSelling - a.bestSelling)
            .slice(0, 8)
            .map((p) => (
              <div key={p.id} className="min-w-[calc(60%-16px)] md:min-w-[calc(25%-18px)] snap-start flex-shrink-0">
                <ProductCard product={p} />
              </div>
            ))}
        </div>"""

text = re.sub(bestseller_pattern, bestseller_replacement, text, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Bestsellers slider added")
