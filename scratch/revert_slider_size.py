import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Pattern for the current slider
slider_pattern = r'<div className="flex overflow-x-auto gap-4 md:gap-6 snap-x snap-mandatory pb-8 \[&::-webkit-scrollbar\]:hidden \[-ms-overflow-style:none\] \[scrollbar-width:none\]">\s*\{\[\.\.\.allProducts\].*?\.map\(\(p\) => \(\s*<div key=\{p\.id\} className="min-w-\[calc\(60%-16px\)\] md:min-w-\[calc\(25%-18px\)\] snap-start flex-shrink-0\">\s*<ProductCard product=\{p\} />\s*</div>\s*\)\)\}\s*</div>'

slider_replacement = """<div className="flex overflow-x-auto gap-3 md:gap-5 snap-x snap-mandatory pb-2 [&::-webkit-scrollbar]:hidden [-ms-overflow-style:none] [scrollbar-width:none]">
          {[...allProducts]
            .sort((a, b) => b.bestSelling - a.bestSelling)
            .slice(0, 8)
            .map((p) => (
              <div key={p.id} className="w-[calc(50%-6px)] min-w-[calc(50%-6px)] md:w-[calc(25%-15px)] md:min-w-[calc(25%-15px)] snap-start flex-shrink-0">
                <ProductCard product={p} />
              </div>
            ))}
        </div>"""

text = re.sub(slider_pattern, slider_replacement, text, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Slider sizes reverted to exact original match")
