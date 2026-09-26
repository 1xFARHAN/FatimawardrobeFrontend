import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update ProductCard
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
            className="aspect-[3/4] w-full object-cover transition duration-[1.2s] ease-out group-hover:scale-[1.05] group-hover:opacity-0"
          />
          <img
            src={product.images[1]}
            alt=""
            loading="lazy"
            className="absolute inset-0 aspect-[3/4] w-full object-cover opacity-0 transition duration-[1.2s] ease-out group-hover:scale-[1.05] group-hover:opacity-100"
            aria-hidden="true"
          />
        </Link>
        {product.badge && (
          <span className="absolute left-4 top-4 font-mono-ui text-[10px] uppercase tracking-widest text-[#2f2925]">
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
          className={`absolute right-4 top-4 transition-all duration-500 ${wish ? 'opacity-100' : 'opacity-0 group-hover:opacity-100'}`}
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
      <div className="mt-5 flex items-baseline justify-between px-1">
        <Link
          href={`/product/${product.slug}`}
          className="font-display text-lg tracking-wide text-[#2f2925] hover:text-[#a74636]"
          data-testid={`link-product-${product.id}`}
        >
          {product.name}
        </Link>
        <div className="font-mono-ui text-[10px] tracking-[0.15em] text-[#776b61]">
          {product.compareAt && (
            <del className="mr-3 text-[#b0a498]">
              {money(product.compareAt)}
            </del>
          )}
          <span className={product.compareAt ? "text-[#a74636]" : ""}>
            {money(product.price)}
          </span>
        </div>
      </div>
    </article>
  );
}"""

new_text = re.sub(product_card_pattern, product_card_replacement, text, flags=re.DOTALL)

# 2. Update ListingPage grid
grid_pattern = r'<div className="grid grid-cols-1 gap-y-20 md:grid-cols-2 md:gap-x-12 md:gap-y-24">'
grid_replacement = '<div className="grid grid-cols-2 gap-x-2 gap-y-12 md:grid-cols-3 md:gap-x-10 md:gap-y-24">'
new_text = new_text.replace(grid_pattern, grid_replacement)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Done")
