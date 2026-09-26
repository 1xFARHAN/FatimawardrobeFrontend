import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Header
header_pattern = r'<header className="border-b border-\[#ded2c4\]">\s*<div className="mx-auto flex max-w-\[1440px\] items-end justify-between gap-6 px-5 py-6 md:px-12">\s*<div>\s*<p className="eyebrow text-\[#a74636\]">The collection</p>\s*<h1 className="mt-2 font-display text-4xl md:text-5xl">\{title\}</h1>\s*</div>\s*<p className="hidden font-mono-ui text-\[10px\] uppercase tracking-\[\.16em\] text-\[#806142\] sm:block">\s*\{shown\.length\} pieces\s*</p>\s*</div>\s*</header>'

header_replacement = """<header className="pt-10 pb-8 md:pt-24 md:pb-16 text-center">
        <div className="mx-auto max-w-[1440px] px-5 md:px-12 flex flex-col items-center">
          <p className="font-mono-ui text-[10px] uppercase tracking-[.25em] text-[#a74636]">The collection</p>
          <h1 className="mt-4 font-display text-5xl md:text-7xl text-[#2f2925] tracking-tight">{title}</h1>
          <p className="mt-6 font-mono-ui text-[10px] uppercase tracking-[.16em] text-[#776b61]">
            {shown.length} pieces
          </p>
        </div>
      </header>"""

text = re.sub(header_pattern, header_replacement, text, flags=re.DOTALL)

# 2. Update Filter Bar
filter_pattern = r'<div className="mb-8 flex items-center justify-between border-b border-\[#ded2c4\] pb-4">\s*<button\s*onClick=\{\(\) => setFilterOpen\(true\)\}\s*className="flex items-center gap-2 text-xs uppercase tracking-widest"\s*data-testid="button-open-filters"\s*>\s*<SlidersHorizontal size=\{15\} /> Refine\s*</button>\s*<label className="ml-auto flex items-center gap-2 text-xs uppercase tracking-widest">\s*Sort\s*<select\s*value=\{sort\}\s*onChange=\{\(e\) => setSort\(e\.target\.value\)\}\s*className="bg-transparent font-mono-ui text-\[10px\] normal-case tracking-normal outline-none"\s*data-testid="select-sort"\s*>'

filter_replacement = """<div className="sticky top-0 z-40 mb-10 flex items-center justify-between bg-background/95 backdrop-blur-sm py-5 border-b border-transparent transition-all duration-300">
          <button
            onClick={() => setFilterOpen(true)}
            className="text-[11px] font-medium uppercase tracking-[0.2em] text-[#2f2925] hover:text-[#a74636] transition-colors"
            data-testid="button-open-filters"
          >
            Filters
          </button>
          <label className="ml-auto flex items-center gap-3 text-[11px] font-medium uppercase tracking-[0.2em] text-[#2f2925]">
            Sort
            <select
              value={sort}
              onChange={(e) => setSort(e.target.value)}
              className="bg-transparent font-mono-ui text-[10px] uppercase tracking-widest text-[#776b61] outline-none cursor-pointer"
              data-testid="select-sort"
            >"""

text = re.sub(filter_pattern, filter_replacement, text, flags=re.DOTALL)

# 3. Update Product Card Text Section
card_text_pattern = r'<div className="mt-5 flex items-baseline justify-between px-1">\s*<Link\s*href=\{`/product/\$\{product\.slug\}`\}\s*className="font-display text-lg tracking-wide text-\[#2f2925\] hover:text-\[#a74636\]"\s*data-testid=\{`link-product-\$\{product\.id\}`\}\s*>\s*\{product\.name\}\s*</Link>\s*<div className="font-mono-ui text-\[10px\] tracking-\[0\.15em\] text-\[#776b61\]">\s*\{product\.compareAt && \(\s*<del className="mr-3 text-\[#b0a498\]">\s*\{money\(product\.compareAt\)\}\s*</del>\s*\)\}\s*<span className=\{product\.compareAt \? "text-\[#a74636\]" : ""\}>\s*\{money\(product\.price\)\}\s*</span>\s*</div>\s*</div>'

card_text_replacement = """<div className="mt-5 px-1">
        <div className="flex items-baseline justify-between">
          <Link
            href={`/product/${product.slug}`}
            className="font-display text-lg tracking-wide text-[#2f2925] hover:text-[#a74636]"
            data-testid={`link-product-${product.id}`}
          >
            {product.name}
          </Link>
          <div className="font-mono-ui text-[10px] tracking-[0.15em] text-[#776b61]">
            {product.compareAt && (
              <del className="mr-2 text-[#b0a498]">
                {money(product.compareAt)}
              </del>
            )}
            <span className={product.compareAt ? "text-[#a74636]" : ""}>
              {money(product.price)}
            </span>
          </div>
        </div>
        {product.colors && product.colors.length > 0 && (
          <div className="mt-2">
            <span className="text-[9px] font-mono-ui uppercase tracking-widest text-[#b0a498]">
              {product.colors.length > 1 ? `+ ${product.colors.length} Colours` : product.colors[0]}
            </span>
          </div>
        )}
      </div>"""

text = re.sub(card_text_pattern, card_text_replacement, text, flags=re.DOTALL)


with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Done")
