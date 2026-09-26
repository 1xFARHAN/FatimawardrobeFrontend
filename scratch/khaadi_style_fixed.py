import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Instead of complex regex, let's use string splitting or a very reliable regex
# Find start of ListingPage
start_idx = text.find('function ListingPage({')
if start_idx == -1:
    print("ListingPage not found")
    exit(1)

# Find the start of ProductDetail (which comes immediately after)
end_idx = text.find('function ProductDetail() {')
if end_idx == -1:
    print("ProductDetail not found")
    exit(1)

listing_replacement = """function ListingPage({
  mode,
  title,
  description,
  forcedCollection,
  forcedSubcategory,
}: {
  mode: string;
  title: string;
  description?: string;
  forcedCollection?: string;
  forcedSubcategory?: string;
}) {
  const [filterOpen, setFilterOpen] = useState(false);
  const [sort, setSort] = useState("featured");
  const [filters, setFilters] = useState({
    category: "",
    fabric: "",
    color: "",
    size: "",
    availability: "",
  });
  const base = allProducts.filter((p) =>
    forcedCollection
      ? p.collection === forcedCollection
      : forcedSubcategory
        ? p.category === mode && slugify(p.subcategory) === forcedSubcategory
        : mode === "new-in"
          ? true
          : mode === "sale"
            ? !!p.compareAt
            : p.category === mode,
  );
  const values = (key: keyof Product) => [
    ...new Set(
      base.flatMap((p) =>
        Array.isArray(p[key]) ? (p[key] as string[]) : [String(p[key])],
      ),
    ),
  ];
  const shown = useMemo(() => {
    let out = base.filter(
      (p) =>
        (!filters.fabric || p.fabric === filters.fabric) &&
        (!filters.color || p.colors.includes(filters.color)) &&
        (!filters.size || p.sizes.includes(filters.size)) &&
        (!filters.availability || p.availability === filters.availability),
    );
    if (sort === "newest")
      out = [...out].sort((a, b) => b.date.localeCompare(a.date));
    if (sort === "price-low") out = [...out].sort((a, b) => a.price - b.price);
    if (sort === "price-high") out = [...out].sort((a, b) => b.price - a.price);
    if (sort === "best")
      out = [...out].sort((a, b) => b.bestSelling - a.bestSelling);
    return out;
  }, [base, filters, sort]);

  const subCategories = useMemo(() => {
    return [
      { name: "Studio: The New Formal", img: allProducts[0]?.images[0] },
      { name: "Urban The Nomad", img: allProducts[1]?.images[0] },
      { name: "Studio: Becoming Her", img: allProducts[2]?.images[0] },
      { name: "Artisanal Gold Impressions", img: allProducts[3]?.images[0] },
      { name: "Basics: Prints On Repeat", img: allProducts[4]?.images[0] },
      { name: "Best Sellers", img: allProducts[5]?.images[0] || allProducts[0]?.images[0] },
    ].filter((x) => x.img);
  }, []);

  const FilterContent = () => (
    <div className="space-y-5">
      {[
        ["fabric", "Fabric"],
        ["color", "Colour"],
        ["size", "Size"],
        ["availability", "Availability"],
      ].map(([key, label]) => (
        <label key={key} className="block">
          <span className="mb-2 block text-xs uppercase tracking-widest">
            {label}
          </span>
          <select
            value={filters[key as keyof typeof filters]}
            onChange={(e) => setFilters({ ...filters, [key]: e.target.value })}
            className="w-full border border-[#cfc1b1] bg-transparent px-3 py-2.5 text-sm"
            data-testid={`select-filter-${key}`}
          >
            <option value="">All {label.toLowerCase()}</option>
            {values(key as keyof Product).map((v) => (
              <option value={v} key={v}>
                {v}
              </option>
            ))}
          </select>
        </label>
      ))}
    </div>
  );

  return (
    <div className="pb-20">
      <div className="mx-auto max-w-[1440px] px-5 py-4 md:px-12">
        <p className="text-xs text-[#776b61]">
          <Link href="/">Home</Link> <span className="mx-2">›</span> <span className="font-medium text-[#2f2925]">{title}</span>
        </p>
      </div>

      <div className="mx-auto max-w-[1440px] px-5 md:px-12 py-6 overflow-x-auto scrollbar-hide">
        <div className="flex items-start justify-center gap-6 md:gap-10 min-w-max mx-auto">
          {subCategories.map((sub, idx) => (
            <div key={idx} className="flex flex-col items-center gap-3 w-20 md:w-24 cursor-pointer group">
              <div className="w-20 h-20 md:w-24 md:h-24 rounded-full overflow-hidden border-2 border-transparent group-hover:border-[#2f2925] transition-colors p-[2px]">
                <img src={sub.img} alt={sub.name} className="w-full h-full object-cover rounded-full" />
              </div>
              <span className="text-[10px] md:text-[11px] text-center leading-tight text-[#776b61] group-hover:text-[#2f2925]">{sub.name}</span>
            </div>
          ))}
        </div>
      </div>

      <div className="mx-auto max-w-[1440px] px-5 md:px-12 mt-6">
        <div className="flex items-center justify-between border-b border-[#ded2c4] pb-4">
          <div className="flex items-center gap-3 md:gap-4">
            <button
              onClick={() => setFilterOpen(true)}
              className="flex items-center justify-between min-w-[120px] md:min-w-[160px] border border-[#cfc1b1] bg-transparent px-3 py-2 text-xs text-[#2f2925] rounded-sm"
              style={{ padding: '0.5rem 0.75rem', outline: 'none' }}
              data-testid="button-open-filters"
            >
              Filter by <ChevronDown size={14} className="ml-2" />
            </button>
            <div className="relative">
              <select
                value={sort}
                onChange={(e) => setSort(e.target.value)}
                className="appearance-none flex items-center justify-between min-w-[140px] md:min-w-[180px] border border-[#cfc1b1] bg-transparent px-3 py-2 pr-8 text-xs text-[#2f2925] outline-none cursor-pointer rounded-sm"
                data-testid="select-sort"
              >
                <option value="featured">Recommended</option>
                <option value="newest">New arrivals</option>
                <option value="price-low">Price: low to high</option>
                <option value="price-high">Price: high to low</option>
                <option value="best">Most loved</option>
              </select>
              <ChevronDown size={14} className="absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none text-[#2f2925]" />
            </div>
          </div>
          
          <div className="hidden md:block text-center flex-1">
            <p className="text-xs text-[#776b61] leading-tight">
              <span className="block font-medium text-[#2f2925] text-sm">{shown.length}</span>
              items
            </p>
          </div>

          <div className="flex items-center gap-2 md:gap-3 text-[#cfc1b1]">
            <div className="hidden md:flex gap-1 h-5 cursor-pointer hover:text-[#2f2925]"><div className="w-2 h-full border border-current"></div><div className="w-2 h-full border border-current"></div></div>
            <div className="hidden md:flex gap-1 h-5 cursor-pointer hover:text-[#2f2925]"><div className="w-1.5 h-full border border-current"></div><div className="w-1.5 h-full border border-current"></div><div className="w-1.5 h-full border border-current"></div></div>
            <div className="flex gap-[2px] h-5 cursor-pointer text-[#2f2925]"><div className="w-[6px] h-full border border-current"></div><div className="w-[6px] h-full border border-current"></div><div className="w-[6px] h-full border border-current"></div><div className="w-[6px] h-full border border-current"></div></div>
          </div>
        </div>
      </div>
      
      <div className="mx-auto max-w-[1440px] px-5 md:px-12 pt-6">
        <div className="grid grid-cols-2 gap-2 md:grid-cols-4 md:gap-3">
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
              className="mt-9 w-full bg-[#2f2925] py-4 text-xs uppercase tracking-widest text-white"
              data-testid="button-apply-filters"
            >
              Show {shown.length} pieces
            </button>
          </aside>
        </div>
      )}
    </div>
  );
}
"""

text = text[:start_idx] + listing_replacement + text[end_idx:]

# Also replace ProductCard exactly
pc_start_idx = text.find('function ProductCard({')
pc_end_idx = text.find('function SectionHeading({', pc_start_idx)

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
  
  return (
    <article
      className={`group ${compact ? "" : "reveal"} flex flex-col`}
      data-testid={`card-product-${product.id}`}
    >
      <div className="relative overflow-hidden bg-[#f0e2d4]">
        <Link
          href={`/product/${product.slug}`}
          aria-label={`View ${product.name}`}
        >
          <img
            src={product.images[0]}
            alt={product.name}
            loading="lazy"
            className="aspect-[3/4] w-full object-cover transition duration-500 group-hover:scale-[1.03]"
          />
        </Link>
        <button
          onClick={toggle}
          aria-label={wish ? `Remove from wishlist` : `Add to wishlist`}
          className="absolute right-3 top-3 flex h-8 w-8 items-center justify-center rounded-full bg-white/85 text-[#2f2925] shadow-sm transition-colors hover:bg-white"
          data-testid={`button-wishlist-${product.id}`}
        >
          <Heart
            size={16}
            strokeWidth={1.5}
            fill={wish ? "#2f2925" : "none"}
            color="#2f2925"
          />
        </button>
      </div>
      <div className="mt-3 flex flex-col items-start gap-1">
        <Link
          href={`/product/${product.slug}`}
          className="text-[13px] text-[#2f2925] hover:underline"
          data-testid={`link-product-${product.id}`}
        >
          {product.name}
        </Link>
        <div className="text-[13px] font-medium text-[#2f2925]">
          {product.compareAt && (
            <del className="mr-2 font-normal text-[#9c8c7d]">
              {money(product.compareAt)}
            </del>
          )}
          <span>
            {money(product.price)}
          </span>
        </div>
      </div>
    </article>
  );
}
"""

text = text[:pc_start_idx] + product_card_replacement + text[pc_end_idx:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("ListingPage and ProductCard replaced!")
