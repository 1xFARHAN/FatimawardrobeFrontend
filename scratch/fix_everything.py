import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the entire ListingPage return statement to guarantee perfect layout
listing_pattern = r'return \(\s*<div className="pb-20">.*?\}\s*</div>\s*\);\s*\}'

listing_replacement = """return (
    <div className="pb-20">
      <header className="pt-8 pb-4 md:pt-12 md:pb-6 border-b border-[#ded2c4]">
        <div className="mx-auto flex max-w-[1440px] items-end justify-between gap-6 px-5 md:px-12">
          <div>
            <p className="font-mono-ui text-[10px] uppercase tracking-[.25em] text-[#776b61]">THE COLLECTION</p>
            <h1 className="mt-4 font-display text-4xl md:text-6xl text-[#2f2925] tracking-tight">{title}</h1>
          </div>
          <p className="hidden font-mono-ui text-[10px] uppercase tracking-[.2em] text-[#776b61] sm:block">
            {shown.length} PIECES
          </p>
        </div>
      </header>
      <div className="mx-auto max-w-[1440px] px-5 pt-6 md:px-12 md:pt-8">
        <div className="mb-10 flex items-center justify-between py-2 border-b border-transparent">
          <button
            onClick={() => setFilterOpen(true)}
            className="flex items-center gap-2 text-xs uppercase tracking-widest text-[#2f2925] hover:text-[#a74636] transition-colors"
            style={{ border: 'none', padding: 0 }}
            data-testid="button-open-filters"
          >
            <SlidersHorizontal size={15} /> REFINE
          </button>
          <label className="ml-auto flex items-center gap-3 text-xs uppercase tracking-widest text-[#2f2925]">
            SORT
            <select
              value={sort}
              onChange={(e) => setSort(e.target.value)}
              className="bg-transparent font-mono-ui text-[10px] uppercase tracking-[.15em] text-[#776b61] outline-none cursor-pointer border-none"
              style={{ border: 'none', outline: 'none' }}
              data-testid="select-sort"
            >
              <option value="featured">The edit</option>
              <option value="newest">New arrivals</option>
              <option value="price-low">Price: low to high</option>
              <option value="price-high">Price: high to low</option>
              <option value="best">Most loved</option>
            </select>
          </label>
        </div>
        <div className="grid grid-cols-2 gap-x-3 gap-y-12 md:grid-cols-4 md:gap-x-5 md:gap-y-16">
          {shown.map((p) => (
            <ProductCard key={p.id} product={p} />
          ))}
          {shown.length === 0 && (
            <div className="col-span-full">
              <EmptyState
                title="A quiet corner"
                copy="No pieces match those filters. Try opening the edit back up."
                link={`/${mode}`}
                label="Reset filters"
              />
            </div>
          )}
        </div>
      </div>
      {filterOpen && (
        <div className="fixed inset-0 z-50 bg-[#2f2925]/30">
          <button
            onClick={() => setFilterOpen(false)}
            className="absolute inset-0"
            aria-label="Close filters"
          />
          <aside className="absolute right-0 top-0 h-full w-full max-w-md bg-[#f6f1e8] p-7 shadow-2xl">
            <div className="mb-10 flex items-center justify-between border-b border-[#ded2c4] pb-5">
              <span className="font-display text-3xl">Refine the edit</span>
              <button
                onClick={() => setFilterOpen(false)}
                aria-label="Close filters"
              >
                <X size={20} />
              </button>
            </div>
            <FilterContent />
            <button
              onClick={() => setFilterOpen(false)}
              className="mt-9 w-full bg-[#a74636] py-4 text-xs uppercase tracking-widest text-[#f6f1e8]"
              data-testid="button-apply-filters"
            >
              Show {shown.length} pieces
            </button>
          </aside>
        </div>
      )}
    </div>
  );
}"""

text = re.sub(listing_pattern, listing_replacement, text, flags=re.DOTALL)


# Let's also fix ProductCard to be extremely polished
product_card_pattern = r'function ProductCard\(\{.*?\}\) \{.*?return \(\s*<article.*?</article>\s*\);\s*\}'
product_card_replacement = """function ProductCard({
  product,
  compact = false,
}: {
  product: Product;
  compact?: boolean;
}) {
  const store = useStore();
  const wish = store.wishlist.includes(product.id);
  const toggle = () => store.toggleWish(product.id);
  const discount = product.compareAt
    ? Math.round((1 - product.price / product.compareAt) * 100)
    : 0;
  return (
    <article
      className={`group ${compact ? "" : "reveal"} flex flex-col`}
      data-testid={`card-product-${product.id}`}
    >
      <div className="relative overflow-hidden bg-[#e6ded3]">
        <Link
          href={`/product/${product.slug}`}
          aria-label={`View ${product.name}`}
        >
          <img
            src={product.images[0]}
            alt={product.name}
            loading="lazy"
            className="aspect-[.78] w-full object-cover transition duration-[1.2s] ease-out group-hover:scale-[1.05] group-hover:opacity-0"
          />
          <img
            src={product.images[1]}
            alt=""
            loading="lazy"
            className="absolute inset-0 aspect-[.78] w-full object-cover opacity-0 transition duration-[1.2s] ease-out group-hover:scale-[1.05] group-hover:opacity-100"
            aria-hidden="true"
          />
        </Link>
        {product.badge && (
          <span className="absolute left-3 top-3 font-mono-ui text-[10px] uppercase tracking-[.15em] text-[#2f2925]">
            {discount ? `${discount}% off` : product.badge}
          </span>
        )}
        <button
          onClick={toggle}
          aria-label={
            wish
              ? `Remove ${product.name} from wishlist`
              : `Add ${product.name} to wishlist`
          }
          className={`absolute right-3 top-3 transition-opacity duration-300 ${wish ? 'opacity-100' : 'opacity-0 group-hover:opacity-100'}`}
          data-testid={`button-wishlist-${product.id}`}
        >
          <Heart
            size={18}
            strokeWidth={1}
            fill={wish ? "#a74636" : "none"}
            color={wish ? "#a74636" : "#2f2925"}
          />
        </button>
      </div>
      <div className="mt-4 flex flex-col items-start gap-1">
        <Link
          href={`/product/${product.slug}`}
          className="font-display text-[17px] leading-tight text-[#2f2925] hover:text-[#a74636]"
          data-testid={`link-product-${product.id}`}
        >
          {product.name}
        </Link>
        <div className="flex w-full items-center justify-between text-[11px] font-mono-ui tracking-widest text-[#776b61] mt-1">
          <span className="uppercase text-[#9c8c7d]">
            {product.colors.length > 1 ? `+ ${product.colors.length} Colours` : product.colors[0]}
          </span>
          <div>
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
      </div>
    </article>
  );
}"""

text = re.sub(product_card_pattern, product_card_replacement, text, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Done")
