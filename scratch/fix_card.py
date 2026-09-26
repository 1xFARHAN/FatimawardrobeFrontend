import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r'<div className="flex items-start justify-between gap-3 pt-4">.*?</div>\s*</div>'

replacement = """<div className="flex flex-col items-center justify-center gap-3 pt-6 text-center">
        <Link
          href={`/product/${product.slug}`}
          className="font-display text-xl leading-tight hover:text-[#a74636]"
          data-testid={`link-product-${product.id}`}
        >
          {product.name}
        </Link>
        <div className="text-[13px] tracking-[0.15em] text-[#776b61]">
          {product.compareAt && (
            <del className="mr-3 text-[#9c8c7d]">
              {money(product.compareAt)}
            </del>
          )}
          <span className={product.compareAt ? "text-[#a74636]" : ""}>
            {money(product.price)}
          </span>
        </div>
      </div>"""

new_text = re.sub(pattern, replacement, text, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Done")
