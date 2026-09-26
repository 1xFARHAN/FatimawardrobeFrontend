import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { useEffect, useMemo, useState, useRef } from "react";
import {
  Link,
  Route,
  Router as WouterRouter,
  Switch,
  useLocation,
  useParams,
} from "wouter";
import {
  ArrowLeft,
  ArrowRight,
  Check,
  ChevronDown,
  ChevronLeft,
  ChevronRight,
  Heart,
  Menu,
  Minus,
  Plus,
  Search,
  ShoppingBag,
  SlidersHorizontal,
  X,
  ZoomIn,
} from "lucide-react";
import { ErrorBoundary } from "@/components/error-boundary";
import { Toaster } from "@/components/ui/toaster";
import { TooltipProvider } from "@/components/ui/tooltip";
import products from "@/data/products.json";
import categories from "@/data/categories.json";
import collections from "@/data/collections.json";
import banners from "@/data/banners.json";
import navigation from "@/data/navigation.json";
import { StoreProvider, useStore, type BagItem } from "@/lib/store";

type Product = (typeof products)[number];
const queryClient = new QueryClient();
const money = (n: number) => `PKR ${n.toLocaleString("en-PK")}`;
const allProducts = products as Product[];
const slugify = (value: string) => value.toLowerCase().replaceAll(" ", "-");
const menuHref = (section: string, _item: string) =>
  section === "Collections" ? "/collections" : `/${slugify(section)}`;

function Shell({ children }: { children: React.ReactNode }) {
  const store = useStore();
  const [location, setLocation] = useLocation();
  const [menu, setMenu] = useState(false);
  const [search, setSearch] = useState(false);
  const [activeMega, setActiveMega] = useState<string | null>(null);
  useEffect(() => {
    if (!menu && !search && !store.bagOpen) return;
    const previousOverflow = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    return () => {
      document.body.style.overflow = previousOverflow;
    };
  }, [menu, search, store.bagOpen]);
  const bagCount = store.bag.reduce((sum, item) => sum + item.quantity, 0);
  const cartTotal = store.bag.reduce((sum, item) => {
    const p = allProducts.find((x) => x.id === item.id);
    return sum + (p?.price || 0) * item.quantity;
  }, 0);
  const navigate = (href: string) => {
    setMenu(false);
    setActiveMega(null);
    setLocation(href);
  };
  return (
    <div className="noise min-h-[100dvh]">
      
      <header className="sticky top-0 z-40 border-b border-[#ded2c4] bg-[#f6f1e8]/95 backdrop-blur-md">
        <div className="mx-auto flex h-[72px] max-w-[1440px] items-center justify-between px-5 md:px-8 lg:h-[84px] lg:px-12">
          <button
            onClick={() => setMenu(true)}
            aria-label="Open menu"
            className="p-2 lg:hidden"
            data-testid="button-open-menu"
          >
            <Menu size={20} strokeWidth={1.4} />
          </button>
          <Link href="/" className="flex items-center gap-3" data-testid="link-logo">
            <img src="/Fatima_logo.png" alt="Fatima Wardrobe Logo" className="h-10 md:h-12 w-auto object-contain" />
            <div className="flex flex-col items-center md:items-start leading-none text-[#2f2925]">
              <span className="block text-[15px] md:text-[19px] font-semibold tracking-[.34em]">
                FATIMA
              </span>
              <span className="mt-[2px] md:mt-1 block text-center md:text-left font-mono-ui text-[7px] md:text-[8px] tracking-[.48em]">
                WARDROBE
              </span>
            </div>
          </Link>
          <nav
            className="hidden items-center gap-7 lg:flex"
            aria-label="Primary navigation"
          >
            {navigation.links.map((link) => (
              <div
                key={link.href}
                onMouseEnter={() =>
                  setActiveMega(link.menu ? link.label : null)
                }
                className="relative py-8"
              >
                <Link
                  href={link.href}
                  className={`eyebrow transition-colors hover:text-[#a74636] ${link.label === "Sale" ? "text-[#a74636]" : ""}`}
                  data-testid={`link-nav-${link.label.toLowerCase().replaceAll(" ", "-")}`}
                >
                  {link.label}
                </Link>
              </div>
            ))}
          </nav>
          <div className="flex items-center gap-1.5">
            <button
              onClick={() => setSearch(true)}
              aria-label="Search"
              className="rounded-full p-2 hover:bg-[#ebe1d5]"
              data-testid="button-open-search"
            >
              <Search size={19} strokeWidth={1.3} />
            </button>
            <Link
              href="/wishlist"
              aria-label="Wishlist"
              className="relative rounded-full p-2 hover:bg-[#ebe1d5]"
              data-testid="link-wishlist"
            >
              <Heart size={19} strokeWidth={1.3} />
              {store.wishlist.length > 0 && (
                <span className="absolute right-0 top-0 flex h-3.5 min-w-3.5 items-center justify-center rounded-full bg-[#a74636] px-1 font-mono-ui text-[8px] text-[#f6f1e8]">
                  {store.wishlist.length}
                </span>
              )}
            </Link>
            <button
              onClick={store.openBag}
              aria-label="Shopping bag"
              className="relative rounded-full p-2 hover:bg-[#ebe1d5]"
              data-testid="button-open-bag"
            >
              <ShoppingBag size={19} strokeWidth={1.3} />
              {bagCount > 0 && (
                <span className="absolute right-0 top-0 flex h-3.5 min-w-3.5 items-center justify-center rounded-full bg-[#a74636] px-1 font-mono-ui text-[8px] text-[#f6f1e8]">
                  {bagCount}
                </span>
              )}
            </button>
          </div>
        </div>
        {activeMega && (
          <div
            onMouseLeave={() => setActiveMega(null)}
            className="absolute left-1/2 -translate-x-1/2 top-[100%] w-fit mt-[1px] bg-[#ffffff] shadow-[0_20px_50px_rgba(47,38,32,0.2)] border border-[#ded2c4] transition-opacity duration-200 rounded-sm"
          >
            <div className="mx-auto w-full px-6 py-6">
              <div className="flex items-start justify-center gap-4">
                {(
                  navigation.links.find((x) => x.label === activeMega)?.menu ||
                  ["Ready to wear", "Unstitched", "Accessories", "Sale"]
                ).slice(0, 4).map((item, i) => (
                  <button
                    key={item}
                    onClick={() => navigate(menuHref(activeMega, item))}
                    className="group text-center flex flex-col items-center w-[160px]"
                  >
                    <div className="aspect-square w-full overflow-hidden bg-[#f0e2d4] mb-3">
                      <img 
                        src={
                          (allProducts.find(p => 
                            p.category.toLowerCase().replace(/-/g, ' ') === activeMega.toLowerCase().replace(/-/g, ' ') && 
                            p.subcategory.toLowerCase() === item.toLowerCase()
                          ) || allProducts.find(p => 
                            p.category.toLowerCase().replace(/-/g, ' ') === activeMega.toLowerCase().replace(/-/g, ' ')
                          ) || allProducts[i % allProducts.length])?.images[0]
                        } 
                        alt={item} 
                        className="w-full h-full object-cover object-top transition duration-700 group-hover:scale-[1.03]"
                      />
                    </div>
                    <span className="text-[13px] font-medium uppercase tracking-[0.1em] text-[#2f2925] group-hover:text-[#a74636]">
                      {item}
                    </span>
                  </button>
                ))}
              </div>
            </div>
          </div>
        )}
      </header>
      <main className="site-main">{children}</main>
      <Footer />
      {menu && <MobileMenu close={() => setMenu(false)} navigate={navigate} />}
      {search && <SearchOverlay close={() => setSearch(false)} />}
      {store.bagOpen && (
        <BagDrawer
          close={store.closeBag}
          bag={store.bag}
          total={cartTotal}
          remove={store.removeFromBag}
          change={store.changeQuantity}
        />
      )}
    </div>
  );
}

function MobileMenu({
  close,
  navigate,
}: {
  close: () => void;
  navigate: (x: string) => void;
}) {
  const [open, setOpen] = useState<string | null>(null);
  return (
    <div
      className="fixed inset-0 z-50 bg-[#f6f1e8] lg:hidden"
      role="dialog"
      aria-label="Mobile menu"
    >
      <div className="flex items-center justify-between border-b border-[#ded2c4] px-5 py-6">
        <Link href="/" onClick={close} className="flex items-center">
          <img src="/Fatima_logo.png" alt="Fatima Wardrobe" className="h-10 w-auto object-contain" />
        </Link>
        <button
          onClick={close}
          aria-label="Close menu"
          data-testid="button-close-menu"
        >
          <X size={23} strokeWidth={1.3} />
        </button>
      </div>
      <div className="px-5 py-7">
        {navigation.links.map((link) => (
          <div key={link.href} className="border-b border-[#ded2c4]">
            <div className="flex items-center justify-between">
              <button
                onClick={() => navigate(link.href)}
                className="py-4 font-display text-3xl"
              >
                {link.label}
              </button>
              {link.menu && (
                <button
                  onClick={() =>
                    setOpen(open === link.label ? null : link.label)
                  }
                  className="p-3"
                  aria-label={`Expand ${link.label}`}
                >
                  <ChevronDown
                    size={18}
                    className={open === link.label ? "rotate-180" : ""}
                  />
                </button>
              )}
            </div>
            {open === link.label && (
              <div className="pb-4 pl-3">
                {link.menu?.map((item) => (
                  <button
                    key={item}
                    onClick={() => navigate(menuHref(link.label, item))}
                    className="block py-1 font-mono-ui text-[11px] uppercase tracking-widest text-[#776b61]"
                  >
                    {item}
                  </button>
                ))}
              </div>
            )}
          </div>
        ))}
      </div>
      <div className="absolute bottom-8 left-5 font-mono-ui text-[10px] uppercase tracking-widest text-[#776b61]">
        Lahore · Pakistan
      </div>
    </div>
  );
}

function SearchOverlay({ close }: { close: () => void }) {
  const [query, setQuery] = useState("");
  const matches = allProducts
    .filter((p) =>
      `${p.name} ${p.category} ${p.collection} ${p.fabric} ${p.colors.join(" ")}`
        .toLowerCase()
        .includes(query.toLowerCase()),
    )
    .slice(0, 6);
  return (
    <div
      className="fixed inset-0 z-50 overflow-y-auto bg-[#f6f1e8]"
      role="dialog"
      aria-label="Search"
    >
      <div className="mx-auto max-w-[1100px] px-5 py-8 md:px-10 md:py-14">
        <div className="flex justify-between">
          <span className="eyebrow text-[#a74636]">Search Fatima Wardrobe</span>
          <button
            onClick={close}
            aria-label="Close search"
            data-testid="button-close-search"
          >
            <X size={24} strokeWidth={1.3} />
          </button>
        </div>
        <div className="mt-16 flex items-center border-b-2 border-[#2f2925]">
          <Search size={25} strokeWidth={1.2} />
          <input
            autoFocus
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Try “cotton”, “noor” or “kurta”"
            className="w-full bg-transparent px-4 py-5 font-display text-3xl outline-none placeholder:text-[#b7aa9b] md:text-5xl"
            data-testid="input-search-overlay"
          />
        </div>
        {query ? (
          <div className="mt-10">
            {matches.length ? (
              <>
                <p className="eyebrow mb-5 text-[#776b61]">
                  {matches.length} results for “{query}”
                </p>
                <div className="grid grid-cols-2 gap-x-4 gap-y-8 md:grid-cols-3">
                  {matches.map((p) => (
                    <ProductCard key={p.id} product={p} compact />
                  ))}
                </div>
              </>
            ) : (
              <EmptyState
                title="Nothing by that name"
                copy="Try a different word or browse the new season."
                link="/new-in"
                label="Browse new in"
              />
            )}
          </div>
        ) : (
          <div className="mt-10">
            <p className="eyebrow mb-5 text-[#776b61]">Popular searches</p>
            <div className="flex flex-wrap gap-2">
              {["Cotton", "New in", "Noor", "Printed lawn", "Accessories"].map(
                (x) => (
                  <button
                    key={x}
                    onClick={() => setQuery(x)}
                    className="border border-[#cfc1b1] px-4 py-2 text-sm hover:border-[#a74636]"
                  >
                    {x}
                  </button>
                ),
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

function BagDrawer({
  close,
  bag,
  total,
  remove,
  change,
}: {
  close: () => void;
  bag: BagItem[];
  total: number;
  remove: (id: string, size: string) => void;
  change: (id: string, size: string, by: number) => void;
}) {
  return (
    <div
      className="fixed inset-0 z-50 bg-[#2f2925]/30"
      role="dialog"
      aria-label="Shopping bag"
    >
      <button
        onClick={close}
        className="absolute inset-0 cursor-default"
        aria-label="Close shopping bag"
        data-testid="button-close-bag"
      />
      <aside className="absolute right-0 top-0 flex h-full w-full max-w-[480px] flex-col bg-[#f6f1e8] shadow-2xl">
        <div className="flex items-center justify-between border-b border-[#ded2c4] px-6 py-6">
          <span className="font-display text-2xl">
            Your bag{" "}
            <sup className="font-mono-ui text-[10px]">{bag.length}</sup>
          </span>
          <button
            onClick={close}
            aria-label="Close"
            data-testid="button-close-bag-icon"
          >
            <X size={21} strokeWidth={1.3} />
          </button>
        </div>
        <div className="flex-1 overflow-y-auto px-6">
          {bag.length ? (
            bag.map((item) => {
              const p = allProducts.find((x) => x.id === item.id);
              if (!p) return null;
              return (
                <div
                  className="flex gap-4 border-b border-[#ded2c4] py-5"
                  key={`${item.id}-${item.size}`}
                >
                  <img
                    src={p.images[0]}
                    alt={p.name}
                    className="h-32 w-24 object-cover"
                  />
                  <div className="flex flex-1 flex-col">
                    <Link
                      href={`/product/${p.slug}`}
                      onClick={close}
                      className="font-display text-lg"
                    >
                      {p.name}
                    </Link>
                    <span className="mt-1 text-xs text-[#776b61]">
                      Size: {item.size}
                    </span>
                    <span className="mt-auto text-sm">{money(p.price)}</span>
                    <div className="mt-3 flex items-center justify-between">
                      <div className="flex items-center border border-[#cfc1b1]">
                        <button
                          onClick={() => change(item.id, item.size, -1)}
                          className="p-1.5"
                          aria-label="Decrease quantity"
                          data-testid={`button-decrease-${item.id}`}
                        >
                          <Minus size={12} />
                        </button>
                        <span className="w-7 text-center text-xs">
                          {item.quantity}
                        </span>
                        <button
                          onClick={() => change(item.id, item.size, 1)}
                          className="p-1.5"
                          aria-label="Increase quantity"
                          data-testid={`button-increase-${item.id}`}
                        >
                          <Plus size={12} />
                        </button>
                      </div>
                      <button
                        onClick={() => remove(item.id, item.size)}
                        className="text-xs underline underline-offset-4"
                        data-testid={`button-remove-${item.id}`}
                      >
                        Remove
                      </button>
                    </div>
                  </div>
                </div>
              );
            })
          ) : (
            <div className="py-20 text-center">
              <ShoppingBag
                className="mx-auto mb-5 text-[#b7aa9b]"
                size={32}
                strokeWidth={1}
              />
              <p className="font-display text-2xl">Your bag is quiet.</p>
              <p className="mt-2 text-sm text-[#776b61]">
                Pieces you love will appear here.
              </p>
            </div>
          )}
        </div>
        {bag.length > 0 && (
          <div className="border-t border-[#ded2c4] px-6 py-6">
            <div className="flex justify-between font-display text-xl">
              <span>Subtotal</span>
              <span>{money(total)}</span>
            </div>
            <p className="mt-2 text-xs text-[#776b61]">
              Shipping calculated at checkout. Complimentary over PKR 5,000.
            </p>
            <Link
              href="/cart"
              onClick={close}
              className="mt-6 block bg-[#a74636] py-4 text-center text-xs uppercase tracking-[.16em] text-[#f6f1e8] hover:bg-[#87382c]"
              data-testid="link-view-bag"
            >
              View bag
            </Link>
            <Link
              href="/checkout"
              onClick={close}
              className="mt-3 block border border-[#a74636] py-4 text-center text-xs uppercase tracking-[.16em] text-[#a74636]"
              data-testid="link-drawer-checkout"
            >
              Checkout
            </Link>
          </div>
        )}
      </aside>
    </div>
  );
}

function Hero() {
  const [slide, setSlide] = useState(0);
  const item = banners[slide];
  return (
    <section className="relative h-[calc(100dvh-118px)] min-h-[570px] max-h-[820px] overflow-hidden bg-[#c6b8a8] text-[#f8f1e7]">
      <picture>
        <source media="(max-width: 767px)" srcSet={item.mobileImage} />
        <img
          src={item.desktopImage}
          alt={item.title.replace("<br/>", " ")}
          className="absolute inset-0 h-full w-full object-cover object-top opacity-90"
        />
      </picture>
      <div className="absolute inset-0 bg-gradient-to-r from-[#2f2925]/60 via-[#2f2925]/15 to-transparent" />
      <div className="relative flex h-full max-w-[1440px] items-end px-6 pb-14 md:px-12 md:pb-20 lg:pb-24">
        <div className="max-w-xl reveal">
          <p className="eyebrow mb-5">{item.eyebrow}</p>
          <h1
            className="font-display text-5xl leading-[.98] md:text-7xl lg:text-[86px]"
            dangerouslySetInnerHTML={{ __html: item.title }}
          />
          <p className="mt-5 text-sm tracking-wide opacity-90 md:text-base">
            {item.copy}
          </p>
          <Link
            href={item.href}
            className="mt-8 inline-flex items-center gap-4 border-b border-[#f8f1e7] pb-2 text-xs uppercase tracking-[.17em]"
            data-testid="link-hero-cta"
          >
            {item.cta}
            <ArrowRight size={16} strokeWidth={1.2} />
          </Link>
        </div>
      </div>
      <div className="absolute bottom-8 right-6 flex items-center gap-4 md:right-12">
        <button
          onClick={() =>
            setSlide((slide + banners.length - 1) % banners.length)
          }
          aria-label="Previous slide"
          data-testid="button-hero-prev"
        >
          <ChevronLeft size={19} />
        </button>
        <div className="flex gap-2">
          {banners.map((b, i) => (
            <button
              key={b.id}
              onClick={() => setSlide(i)}
              aria-label={`Go to slide ${i + 1}`}
              className={`h-px transition-all ${i === slide ? "w-12 bg-[#f8f1e7]" : "w-5 bg-[#f8f1e7]/50"}`}
              data-testid={`button-hero-dot-${i}`}
            />
          ))}
        </div>
        <button
          onClick={() => setSlide((slide + 1) % banners.length)}
          aria-label="Next slide"
          data-testid="button-hero-next"
        >
          <ChevronRight size={19} />
        </button>
      </div>
    </section>
  );
}

function ProductCard({
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
function SectionHeading({
  eyebrow,
  title,
  link,
  href,
}: {
  eyebrow: string;
  title: string;
  link?: string;
  href?: string;
}) {
  return (
    <div className="mb-8 flex items-end justify-between gap-5">
      <div>
        <p className="eyebrow text-[#a74636]">{eyebrow}</p>
        <h2 className="mt-2 font-display text-4xl md:text-5xl">{title}</h2>
      </div>
      {link && href && (
        <Link
          href={href}
          className="hidden items-center gap-3 border-b border-[#a74636] pb-2 text-xs uppercase tracking-[.15em] text-[#a74636] sm:flex"
          data-testid={`link-section-${href.replace("/", "")}`}
        >
          {link}
          <ArrowRight size={15} strokeWidth={1.2} />
        </Link>
      )}
    </div>
  );
}

function Home() {
  const sliderRef = useRef<HTMLDivElement>(null);
  
  useEffect(() => {
    const interval = setInterval(() => {
      if (sliderRef.current) {
        const slider = sliderRef.current;
        const maxScroll = slider.scrollWidth - slider.clientWidth;
        if (slider.scrollLeft >= maxScroll - 10) {
          slider.scrollTo({ left: 0, behavior: 'smooth' });
        } else {
          slider.scrollBy({ left: slider.clientWidth / (window.innerWidth > 768 ? 4 : 2), behavior: 'smooth' });
        }
      }
    }, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <>
      <Hero />
      <div className="border-b border-[#ded2c4] px-5 py-5 text-center font-mono-ui text-[9px] uppercase tracking-[.16em] text-[#776b61] md:px-12">
        Crafted in Lahore <span className="mx-4">·</span> Complimentary delivery
        over PKR 5,000 <span className="mx-4">·</span> Made to be kept
      </div>
      <div className="mx-auto max-w-[1440px] px-5 py-20 md:px-12 md:py-28">
        <SectionHeading
          eyebrow="The Fatima Wardrobe edit"
          title="Pieces with presence."
          link="Shop all new"
          href="/new-in"
        />
        <div className="grid gap-4 md:grid-cols-3">
          {categories.map((cat, i) => (
            <Link
              href={`/category/${cat.slug}`}
              key={cat.slug}
              className={`group relative overflow-hidden ${i === 1 ? "md:mt-12" : ""}`}
              data-testid={`link-category-${cat.slug}`}
            >
              <img
                src={cat.image}
                alt={cat.name}
                className="aspect-[.84] w-full object-cover transition duration-700 group-hover:scale-[1.04]"
              />
              <div className="absolute inset-x-0 bottom-0 bg-gradient-to-t from-[#2f2925]/70 to-transparent p-5 pt-20 text-[#f8f1e7]">
                <p className="font-display text-3xl">{cat.name}</p>
                <span className="mt-2 inline-flex items-center gap-2 text-xs uppercase tracking-widest opacity-0 transition group-hover:opacity-100">
                  Explore <ArrowRight size={14} />
                </span>
              </div>
            </Link>
          ))}
        </div>
      </div>
      <div className="bg-[#ded8c9] px-5 py-20 md:px-12 md:py-28">
        <div className="mx-auto max-w-[1440px]">
          <SectionHeading
            eyebrow="The latest chapter"
            title="New arrivals"
            link="See new in"
            href="/new-in"
          />
          <div className="grid grid-cols-2 gap-x-3 gap-y-10 md:grid-cols-4 md:gap-x-5">
            {allProducts.slice(0, 4).map((p) => (
              <ProductCard key={p.id} product={p} />
            ))}
          </div>
        </div>
      </div>
      <EditorialBanner />
      <div className="mx-auto max-w-[1440px] px-5 py-20 md:px-12 md:py-28">
        <SectionHeading
          eyebrow="Most loved"
          title="Bestsellers"
          link="Shop bestsellers"
          href="/new-in"
        />
        <div ref={sliderRef} className="flex overflow-x-auto gap-3 md:gap-5 snap-x snap-mandatory pb-2 [&::-webkit-scrollbar]:hidden [-ms-overflow-style:none] [scrollbar-width:none]">
          {[...allProducts]
            .sort((a, b) => b.bestSelling - a.bestSelling)
            .slice(0, 8)
            .map((p) => (
              <div key={p.id} className="w-[calc(50%-6px)] min-w-[calc(50%-6px)] md:w-[calc(25%-15px)] md:min-w-[calc(25%-15px)] snap-start flex-shrink-0">
                <ProductCard product={p} />
              </div>
            ))}
        </div>
      </div>
      <div className="grid md:grid-cols-2">
        <PromoTile
          image="/images/ready-to-wear-editorial.png"
          title="Ready to wear"
          copy="For moments worth dressing for."
          href="/ready-to-wear"
        />
        <PromoTile
          image="/images/unstitched-editorial.png"
          title="Unstitched"
          copy="Start with cloth. Make it yours."
          href="/unstitched"
        />
      </div>
      
      <Newsletter />
    </>
  );
}

function EditorialBanner() {
  return (
    <section className="relative min-h-[400px] overflow-hidden bg-[#5c6657] text-[#f8f1e7]">
      <img
        src="/images/hero-luxury-courtyard.png"
        alt="Gulbahar collection"
        className="absolute inset-0 h-full w-full object-cover object-top opacity-100"
      />
      <div className="absolute inset-0 bg-gradient-to-r from-[#2f2925]/70 via-[#2f2925]/25 to-transparent" />
      <div className="relative flex min-h-[400px] items-end px-5 pb-14 md:px-12 md:pb-16">
        <div className="w-full max-w-[1440px]">
          <p className="eyebrow">The Gulbahar collection</p>
          <h2 className="mt-4 font-display text-5xl italic md:text-7xl">
            An evening in bloom.
          </h2>
          <p className="mt-4 max-w-sm text-sm leading-6">
            Soft embroidery, garden colour and a little ceremony for the moments
            that matter.
          </p>
          <Link
            href="/collection/gulbahar"
            className="mt-7 inline-flex items-center gap-3 border-b border-[#f8f1e7] pb-2 text-xs uppercase tracking-widest"
            data-testid="link-editorial-collection"
          >
            Discover Gulbahar <ArrowRight size={15} />
          </Link>
        </div>
      </div>
    </section>
  );
}

function PromoTile({
  image,
  title,
  copy,
  href,
}: {
  image: string;
  title: string;
  copy: string;
  href: string;
}) {
  return (
    <Link
      href={href}
      className="group relative overflow-hidden"
      data-testid={`link-promo-${title.toLowerCase().replaceAll(" ", "-")}`}
    >
      <img
        src={image}
        alt={title}
        className="aspect-[1.15] h-full w-full object-cover object-top transition duration-700 group-hover:scale-[1.04]"
      />
      <div className="absolute inset-0 bg-gradient-to-t from-[#2f2925]/65 to-transparent" />
      <div className="absolute bottom-8 left-7 text-[#f8f1e7] md:bottom-12 md:left-12">
        <p className="eyebrow">{title}</p>
        <p className="mt-2 font-display text-4xl">{copy}</p>
        <span className="mt-5 inline-flex items-center gap-2 text-xs uppercase tracking-widest">
          Explore <ArrowRight size={15} />
        </span>
      </div>
    </Link>
  );
}



function Newsletter() {
  const [email, setEmail] = useState("");
  const [done, setDone] = useState(false);
  return (
    <section className="bg-[#b8c9bf] px-5 py-20 md:px-12 md:py-24">
      <div className="mx-auto flex max-w-[1060px] flex-col justify-between gap-8 md:flex-row md:items-end">
        <div>
          <p className="eyebrow text-[#2d5145]">A little letter</p>
          <h2 className="mt-3 max-w-md font-display text-5xl leading-[1.05]">
            Good things,
            <br />
            <i>occasionally.</i>
          </h2>
          <p className="mt-4 max-w-sm text-sm leading-6 text-[#466158]">
            New collections, studio notes and a reason to dress up. No noise.
          </p>
        </div>
        {done ? (
          <div className="flex items-center gap-3 border-b border-[#2d5145] pb-3 text-sm text-[#2d5145]">
            <Check size={18} /> You’re on the list.
          </div>
        ) : (
          <form
            onSubmit={(e) => {
              e.preventDefault();
              if (email.includes("@")) setDone(true);
            }}
            className="flex w-full max-w-md border-b border-[#2d5145] pb-3"
          >
            <input
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              type="email"
              required
              placeholder="Your email address"
              className="flex-1 bg-transparent text-sm outline-none placeholder:text-[#466158]"
              aria-label="Email address"
              data-testid="input-newsletter-email"
            />
            <button
              className="text-xs uppercase tracking-widest text-[#2d5145]"
              data-testid="button-newsletter-submit"
            >
              Sign me up <ArrowRight className="ml-2 inline" size={15} />
            </button>
          </form>
        )}
      </div>
    </section>
  );
}

function Footer() {
  return (
    <footer className="bg-[#2f2925] px-5 py-14 text-[#e9dfd2] md:px-12 md:py-20">
      <div className="mx-auto max-w-[1440px]">
        <div className="grid gap-12 md:grid-cols-[1.4fr_1fr_1fr_1fr]">
          <div>
            <img src="/Fatima_logo.png" alt="Fatima Wardrobe" className="h-16 w-auto object-contain brightness-0 invert opacity-90" />
            <p className="mt-8 max-w-xs text-sm leading-6 text-[#aa9e91]">
              A modern Pakistani label for clothes with a life ahead of them.
            </p>
          </div>
          <div>
            <p className="eyebrow mb-5 text-[#b8c9bf]">Shop</p>
            {[
              "New in",
              "Ready to wear",
              "Unstitched",
              "Collections",
              "Sale",
            ].map((x) => (
              <Link
                key={x}
                href={`/${x.toLowerCase().replaceAll(" ", "-")}`}
                className="mb-3 block text-sm text-[#d2c6ba] hover:text-[#f6f1e8]"
              >
                {x}
              </Link>
            ))}
          </div>
          <div>
            <p className="eyebrow mb-5 text-[#b8c9bf]">Help</p>
            {[
              ["Shipping", "/shipping"],
              ["Returns", "/returns"],
              ["Size guide", "/size-guide"],
              ["Contact", "/contact"],
            ].map(([x, h]) => (
              <Link
                key={h}
                href={h}
                className="mb-3 block text-sm text-[#d2c6ba] hover:text-[#f6f1e8]"
              >
                {x}
              </Link>
            ))}
          </div>
          <div>
            <p className="eyebrow mb-5 text-[#b8c9bf]">A note</p>
            <p className="text-sm leading-6 text-[#aa9e91]">
              Designed in Lahore.
              <br />
              Worn everywhere.
            </p>
            <Link
              href="/about"
              className="mt-5 inline-flex items-center gap-2 text-xs uppercase tracking-widest"
            >
              Our story <ArrowRight size={14} />
            </Link>
          </div>
        </div>
        <div className="mt-16 flex flex-col justify-between gap-4 border-t border-[#5a5048] pt-6 text-[10px] uppercase tracking-widest text-[#8f8379] md:flex-row">
          <span>© 2025 Fatima Wardrobe</span>
          <span>Made slowly, worn often.</span>
          <Link href="/admin-preview">Preview tools</Link>
        </div>
      </div>
    </footer>
  );
}

function ListingPage({
  mode,
  title,
  description,
  forcedCollection,
  forcedSubcategory,
  hideSubcategories = false,
}: {
  mode: string;
  title: string;
  description?: string;
  forcedCollection?: string;
  forcedSubcategory?: string;
  hideSubcategories?: boolean;
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
          <Link href="/">Home</Link> <span className="mx-2">›</span>
          {hideSubcategories ? (
            <>
              <Link href={`/${mode}`} className="hover:underline text-[#776b61] capitalize">{mode.replace('-', ' ')}</Link>
              <span className="mx-2">›</span>
              <span className="font-medium text-[#2f2925] capitalize">{title}</span>
            </>
          ) : (
            <span className="font-medium text-[#2f2925] capitalize">{title}</span>
          )}
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
function ProductDetail() {
  const { slug } = useParams<{ slug: string }>();
  const product = allProducts.find((p) => p.slug === slug);
  const store = useStore();
  const [image, setImage] = useState(0);
  const [size, setSize] = useState(product?.sizes[0] || "");
  const [quantity, setQuantity] = useState(1);
  const [zoom, setZoom] = useState(false);
  const [added, setAdded] = useState(false);
  if (!product)
    return (
      <NotFound
        title="This piece has moved on."
        copy="The product you’re looking for is no longer in this edit."
        link="/new-in"
      />
    );
  const add = () => {
    store.addToBag(product.id, size, quantity);
    store.openBag();
    setAdded(true);
    setTimeout(() => setAdded(false), 2200);
  };
  const related = allProducts
    .filter(
      (p) =>
        p.id !== product.id &&
        (p.collection === product.collection ||
          p.category === product.category),
    )
    .slice(0, 4);
  return (
    <div className="mx-auto max-w-[1440px] px-5 py-8 md:px-12 md:py-12">
      <p className="eyebrow mb-8 text-[#776b61]">
        <Link href="/">Home</Link>
        <span className="mx-2">/</span>
        <Link href={`/${product.category}`}>{product.category}</Link>
        <span className="mx-2">/</span>
        {product.name}
      </p>
      <div className="grid gap-10 lg:grid-cols-[1.15fr_.85fr] lg:gap-20">
        <div className="grid gap-3 md:grid-cols-[82px_1fr]">
          <div className="order-2 flex gap-2 overflow-x-auto md:order-1 md:flex-col">
            {product.images.map((src, i) => (
              <button
                key={src}
                onClick={() => setImage(i)}
                className={`shrink-0 overflow-hidden border ${i === image ? "border-[#a74636]" : "border-transparent"}`}
                data-testid={`button-thumbnail-${i}`}
              >
                <img
                  src={src}
                  alt={`${product.name} view ${i + 1}`}
                  className="h-20 w-16 object-cover md:h-24 md:w-[80px]"
                />
              </button>
            ))}
          </div>
          <div className="group relative order-1 overflow-hidden bg-[#e6ded3] md:order-2">
            <img
              src={product.images[image]}
              alt={product.name}
              className="aspect-[.82] w-full object-cover md:aspect-[.78]"
              onClick={() => setZoom(true)}
            />
            <button
              onClick={() => setZoom(true)}
              className="absolute bottom-4 right-4 flex items-center gap-2 bg-[#f6f1e8]/90 px-3 py-2 text-xs uppercase tracking-widest"
              data-testid="button-zoom"
            >
              <ZoomIn size={15} /> View
            </button>
          </div>
        </div>
        <div className="lg:pt-8">
          <div className="flex justify-between gap-4">
            <div>
              <p className="eyebrow text-[#a74636]">
                {product.collection.replaceAll("-", " ")}
              </p>
              <h1 className="mt-3 font-display text-4xl md:text-5xl">
                {product.name}
              </h1>
            </div>
            <button
              onClick={() => store.toggleWish(product.id)}
              aria-label="Toggle wishlist"
              className="h-fit rounded-full border border-[#cfc1b1] p-3"
              data-testid="button-detail-wishlist"
            >
              <Heart
                size={19}
                fill={store.wishlist.includes(product.id) ? "#a74636" : "none"}
                color={
                  store.wishlist.includes(product.id)
                    ? "#a74636"
                    : "currentColor"
                }
                strokeWidth={1.2}
              />
            </button>
          </div>
          <div className="mt-5 text-lg">
            {product.compareAt && (
              <del className="mr-2 text-sm text-[#9c8c7d]">
                {money(product.compareAt)}
              </del>
            )}
            <span className={product.compareAt ? "text-[#a74636]" : ""}>
              {money(product.price)}
            </span>
          </div>
          <p className="mt-6 text-sm leading-7 text-[#776b61]">
            {product.description}
          </p>
          <div className="mt-10 border-t border-[#ded2c4] pt-6">
            <div className="mb-4 flex justify-between">
              <span className="text-xs uppercase tracking-widest">
                Select size
              </span>
              <Link
                href="/size-guide"
                className="text-xs underline underline-offset-4"
              >
                Size guide
              </Link>
            </div>
            <div className="flex flex-wrap gap-2">
              {product.sizes.map((s) => (
                <button
                  key={s}
                  onClick={() => setSize(s)}
                  className={`min-w-14 border px-4 py-3 text-xs ${size === s ? "border-[#a74636] bg-[#a74636] text-[#f6f1e8]" : "border-[#cfc1b1]"}`}
                  data-testid={`button-size-${s}`}
                >
                  {s}
                </button>
              ))}
            </div>
          </div>
          <div className="mt-6 flex gap-3">
            <div className="flex items-center border border-[#cfc1b1]">
              <button
                onClick={() => setQuantity(Math.max(1, quantity - 1))}
                className="p-3"
                aria-label="Decrease quantity"
              >
                <Minus size={14} />
              </button>
              <span className="w-8 text-center text-sm">{quantity}</span>
              <button
                onClick={() => setQuantity(quantity + 1)}
                className="p-3"
                aria-label="Increase quantity"
              >
                <Plus size={14} />
              </button>
            </div>
            <button
              onClick={add}
              className="flex-1 bg-[#a74636] py-4 text-xs uppercase tracking-[.16em] text-[#f6f1e8] hover:bg-[#87382c]"
              data-testid="button-add-to-bag"
            >
              {added ? "Added to your bag" : "Add to bag"}
            </button>
          </div>
          <div className="mt-8 divide-y divide-[#ded2c4] border-y border-[#ded2c4]">
            {[
              ["Details", product.description],
              [
                "Fabric & care",
                `${product.fabric}. Cold wash recommended. Dry in shade.`,
              ],
              [
                "Delivery",
                "Complimentary delivery on orders over PKR 5,000. Standard delivery takes 3–5 working days.",
              ],
            ].map(([title, copy]) => (
              <details key={title} className="group py-4">
                <summary className="flex cursor-pointer list-none justify-between text-sm">
                  {title}
                  <Plus size={16} className="transition group-open:rotate-45" />
                </summary>
                <p className="max-w-lg pt-3 text-sm leading-6 text-[#776b61]">
                  {copy}
                </p>
              </details>
            ))}
          </div>
        </div>
      </div>
      <div className="mt-24 border-t border-[#ded2c4] pt-12">
        <SectionHeading eyebrow="You may also like" title="Complete the look" />
        <div className="grid grid-cols-2 gap-x-3 gap-y-10 md:grid-cols-4 md:gap-x-5">
          {related.map((p) => (
            <ProductCard key={p.id} product={p} />
          ))}
        </div>
      </div>
      {zoom && (
        <div
          className="fixed inset-0 z-50 flex items-center justify-center bg-[#2f2925]/90 p-5"
          role="dialog"
          aria-label="Product image zoom"
        >
          <button
            onClick={() => setZoom(false)}
            className="absolute right-6 top-6 text-[#f6f1e8]"
            aria-label="Close zoom"
          >
            <X size={26} />
          </button>
          <img
            src={product.images[image]}
            alt={product.name}
            className="max-h-[90vh] max-w-full object-contain"
          />
        </div>
      )}
    </div>
  );
}

function CartPage() {
  const store = useStore();
  const total = store.bag.reduce((sum, item) => {
    const p = allProducts.find((x) => x.id === item.id);
    return sum + (p?.price || 0) * item.quantity;
  }, 0);
  const shipping = total >= 5000 ? 0 : total ? 250 : 0;
  return (
    <div className="mx-auto max-w-[1200px] px-5 py-12 md:px-12 md:py-20">
      <p className="eyebrow text-[#a74636]">Your bag</p>
      <h1 className="mt-4 font-display text-6xl">Take your time.</h1>
      {!store.bag.length ? (
        <EmptyState
          title="Your bag is quiet."
          copy="Start with the pieces you cannot stop thinking about."
          link="/new-in"
          label="Explore new in"
        />
      ) : (
        <div className="mt-12 grid gap-12 lg:grid-cols-[1fr_340px]">
          <div>
            {store.bag.map((item) => {
              const p = allProducts.find((x) => x.id === item.id);
              if (!p) return null;
              return (
                <div
                  key={`${item.id}-${item.size}`}
                  className="flex gap-5 border-t border-[#ded2c4] py-5"
                >
                  <img
                    src={p.images[0]}
                    alt={p.name}
                    className="h-36 w-28 object-cover"
                  />
                  <div className="flex flex-1 flex-col">
                    <Link
                      href={`/product/${p.slug}`}
                      className="font-display text-xl"
                    >
                      {p.name}
                    </Link>
                    <p className="mt-1 text-xs text-[#776b61]">
                      Size {item.size} · {money(p.price)}
                    </p>
                    <div className="mt-auto flex items-center gap-5">
                      <div className="flex items-center border border-[#cfc1b1]">
                        <button
                          onClick={() =>
                            store.changeQuantity(item.id, item.size, -1)
                          }
                          className="p-2"
                          aria-label="Decrease quantity"
                        >
                          <Minus size={13} />
                        </button>
                        <span className="w-7 text-center text-xs">
                          {item.quantity}
                        </span>
                        <button
                          onClick={() =>
                            store.changeQuantity(item.id, item.size, 1)
                          }
                          className="p-2"
                          aria-label="Increase quantity"
                        >
                          <Plus size={13} />
                        </button>
                      </div>
                      <button
                        onClick={() => store.removeFromBag(item.id, item.size)}
                        className="text-xs underline underline-offset-4"
                      >
                        Remove
                      </button>
                    </div>
                  </div>
                  <span>{money(p.price * item.quantity)}</span>
                </div>
              );
            })}
          </div>
          <aside className="h-fit border border-[#ded2c4] p-6">
            <p className="eyebrow text-[#a74636]">Summary</p>
            <div className="mt-6 flex justify-between text-sm">
              <span>Subtotal</span>
              <span>{money(total)}</span>
            </div>
            <div className="mt-3 flex justify-between text-sm">
              <span>Delivery</span>
              <span>{shipping ? money(shipping) : "Complimentary"}</span>
            </div>
            <div className="mt-5 border-t border-[#ded2c4] pt-5 flex justify-between font-display text-xl">
              <span>Total</span>
              <span>{money(total + shipping)}</span>
            </div>
            <Link
              href="/checkout"
              className="mt-7 block bg-[#a74636] py-4 text-center text-xs uppercase tracking-widest text-[#f6f1e8]"
              data-testid="link-cart-checkout"
            >
              Continue to checkout
            </Link>
            <p className="mt-4 text-center text-[11px] leading-5 text-[#776b61]">
              {total >= 5000
                ? "You have complimentary delivery."
                : `Add ${money(5000 - total)} for complimentary delivery.`}
            </p>
          </aside>
        </div>
      )}
    </div>
  );
}

function LegacyCheckout() {
  const store = useStore();
  const total = store.bag.reduce((sum, item) => {
    const p = allProducts.find((x) => x.id === item.id);
    return sum + (p?.price || 0) * item.quantity;
  }, 0);
  const shipping = total >= 5000 ? 0 : 250;
  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState("");
  if (submitted)
    return (
      <div className="mx-auto max-w-2xl px-5 py-24 text-center md:py-36">
        <div className="mx-auto flex h-16 w-16 items-center justify-center rounded-full bg-[#b8c9bf] text-[#2d5145]">
          <Check />
        </div>
        <p className="eyebrow mt-8 text-[#a74636]">Demo confirmation</p>
        <h1 className="mt-4 font-display text-6xl">Thank you.</h1>
        <p className="mx-auto mt-5 max-w-md text-sm leading-7 text-[#776b61]">
          Your demo order <strong>FW-25-1847</strong> has been noted. No payment
          was taken and this storefront does not create real orders.
        </p>
        <Link
          href="/new-in"
          className="mt-8 inline-flex items-center gap-3 border-b border-[#a74636] pb-2 text-xs uppercase tracking-widest text-[#a74636]"
        >
          Continue browsing <ArrowRight size={15} />
        </Link>
      </div>
    );
  return (
    <div className="mx-auto max-w-[1180px] px-5 py-12 md:px-12 md:py-20">
      <p className="eyebrow text-[#a74636]">Frontend demo checkout</p>
      <h1 className="mt-4 font-display text-6xl">Almost there.</h1>
      <div className="mt-12 grid gap-12 lg:grid-cols-[1fr_360px]">
        <form
          onSubmit={(e) => {
            e.preventDefault();
            const data = new FormData(e.currentTarget);
            if (
              !data.get("name") ||
              !data.get("email") ||
              !data.get("phone") ||
              !data.get("address")
            ) {
              setError("Please complete the required fields.");
              return;
            }
            setSubmitted(true);
          }}
          className="space-y-8"
        >
          <div className="rounded-sm border border-[#cfb6a2] bg-[#f0e2d4] p-5 text-sm leading-6 text-[#674d3e]">
            <strong>Demo only.</strong> This checkout is a visual walkthrough.
            It does not process payment or place a real order.
          </div>
          <fieldset>
            <legend className="mb-5 font-display text-2xl">Your details</legend>
            <div className="grid gap-4 md:grid-cols-2">
              <input
                name="name"
                required
                placeholder="Full name *"
                className="border-b border-[#cfc1b1] bg-transparent px-1 py-3 text-sm outline-none"
                data-testid="input-checkout-name"
              />
              <input
                name="email"
                required
                type="email"
                placeholder="Email address *"
                className="border-b border-[#cfc1b1] bg-transparent px-1 py-3 text-sm outline-none"
                data-testid="input-checkout-email"
              />
              <input
                name="phone"
                required
                placeholder="Phone number *"
                className="border-b border-[#cfc1b1] bg-transparent px-1 py-3 text-sm outline-none"
                data-testid="input-checkout-phone"
              />
              <input
                name="city"
                placeholder="City"
                className="border-b border-[#cfc1b1] bg-transparent px-1 py-3 text-sm outline-none"
                data-testid="input-checkout-city"
              />
              <input
                name="address"
                required
                placeholder="Delivery address *"
                className="border-b border-[#cfc1b1] bg-transparent px-1 py-3 text-sm outline-none md:col-span-2"
                data-testid="input-checkout-address"
              />
            </div>
          </fieldset>
          <fieldset>
            <legend className="mb-4 font-display text-2xl">Payment</legend>
            <label className="flex items-center gap-3 border border-[#a74636] bg-[#f0e2d4] p-4 text-sm">
              <input type="radio" defaultChecked name="payment" /> Cash on
              Delivery{" "}
              <span className="ml-auto text-xs text-[#776b61]">Demo</span>
            </label>
          </fieldset>
          {error && (
            <p className="text-sm text-[#a74636]" role="alert">
              {error}
            </p>
          )}
          <button
            className="w-full bg-[#a74636] py-4 text-xs uppercase tracking-widest text-[#f6f1e8]"
            data-testid="button-place-demo-order"
          >
            Review demo order
          </button>
        </form>
        <aside className="h-fit border border-[#ded2c4] p-6">
          <p className="eyebrow text-[#a74636]">Order summary</p>
          {store.bag.map((item) => {
            const p = allProducts.find((x) => x.id === item.id);
            return p ? (
              <div
                key={`${item.id}-${item.size}`}
                className="mt-4 flex justify-between gap-4 text-sm"
              >
                <span>
                  {p.name}{" "}
                  <small className="text-[#776b61]">× {item.quantity}</small>
                </span>
                <span>{money(p.price * item.quantity)}</span>
              </div>
            ) : null;
          })}
          <div className="mt-6 border-t border-[#ded2c4] pt-5 text-sm">
            <div className="flex justify-between">
              <span>Delivery</span>
              <span>{shipping ? money(shipping) : "Complimentary"}</span>
            </div>
            <div className="mt-4 flex justify-between font-display text-xl">
              <span>Total</span>
              <span>{money(total + shipping)}</span>
            </div>
          </div>
        </aside>
      </div>
    </div>
  );
}

function Checkout() {
  const store = useStore();
  const total = store.bag.reduce((sum, item) => {
    const product = allProducts.find((candidate) => candidate.id === item.id);
    return sum + (product?.price || 0) * item.quantity;
  }, 0);
  const shipping = total >= 5000 ? 0 : 250;
  const [submitted, setSubmitted] = useState(false);
  const [orderNumber, setOrderNumber] = useState("");
  const [error, setError] = useState("");

  if (!store.bag.length && !submitted) {
    return (
      <div className="mx-auto max-w-2xl px-5 py-24 text-center md:py-36">
        <p className="eyebrow text-[#a74636]">Checkout</p>
        <h1 className="mt-4 font-display text-6xl">Your bag is empty.</h1>
        <p className="mt-5 text-sm leading-7 text-[#776b61]">
          Add a piece you love before you begin checkout.
        </p>
        <Link
          href="/new-in"
          className="mt-8 inline-flex items-center gap-3 border-b border-[#a74636] pb-2 text-xs uppercase tracking-widest text-[#a74636]"
        >
          Explore new in <ArrowRight size={15} />
        </Link>
      </div>
    );
  }

  if (submitted) {
    return (
      <div className="mx-auto max-w-2xl px-5 py-20 text-center md:py-24">
        <div className="mx-auto flex h-16 w-16 items-center justify-center rounded-full bg-[#e6b9c3] text-[#592f39]">
          <Check />
        </div>
        <p className="eyebrow mt-8 text-[#a74636]">Order confirmation</p>
        <h1 className="mt-4 font-display text-6xl">Thank you.</h1>
        <p className="mx-auto mt-5 max-w-md text-sm leading-7 text-[#776b61]">
          Your order reference is <strong>{orderNumber}</strong>. Thank you for
          choosing Fatima Wardrobe.
        </p>
        <Link
          href="/new-in"
          className="mt-8 inline-flex items-center gap-3 border-b border-[#a74636] pb-2 text-xs uppercase tracking-widest text-[#a74636]"
        >
          Continue browsing <ArrowRight size={15} />
        </Link>
      </div>
    );
  }

  const submit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    const required = [
      "firstName",
      "lastName",
      "email",
      "phone",
      "address",
      "city",
      "province",
      "postalCode",
    ];
    if (required.some((field) => !String(data.get(field) || "").trim())) {
      setError(
        "Please complete all required fields before placing your order.",
      );
      return;
    }
    setError("");
    setOrderNumber(
      `FW-${new Date().getFullYear()}-${Math.floor(1000 + Math.random() * 9000)}`,
    );
    setSubmitted(true);
    store.clearBag();
  };

  return (
    <div className="mx-auto max-w-[1180px] px-5 py-12 md:px-12 md:py-20">
      <p className="eyebrow text-[#a74636]">Secure checkout</p>
      <h1 className="mt-4 font-display text-6xl">Almost there.</h1>
      <div className="mt-12 grid gap-12 lg:grid-cols-[1fr_360px]">
        <form onSubmit={submit} className="space-y-8">
          <div className="rounded-sm border border-[#ded2c4] bg-[#f0e9df] p-5 text-sm leading-6 text-[#493d34]">
            <strong>Cash on Delivery.</strong> Please review your delivery
            details before placing your order.
          </div>
          <fieldset>
            <legend className="mb-5 font-display text-2xl">
              Contact information
            </legend>
            <div className="grid gap-4 md:grid-cols-2">
              <input
                name="firstName"
                required
                placeholder="First name *"
                className="checkout-field"
                data-testid="input-checkout-first-name"
              />
              <input
                name="lastName"
                required
                placeholder="Last name *"
                className="checkout-field"
                data-testid="input-checkout-last-name"
              />
              <input
                name="email"
                required
                type="email"
                placeholder="Email address *"
                className="checkout-field"
                data-testid="input-checkout-email"
              />
              <input
                name="phone"
                required
                placeholder="Phone number *"
                className="checkout-field"
                data-testid="input-checkout-phone"
              />
            </div>
          </fieldset>
          <fieldset>
            <legend className="mb-5 font-display text-2xl">
              Shipping address
            </legend>
            <div className="grid gap-4 md:grid-cols-2">
              <input
                name="address"
                required
                placeholder="Street address *"
                className="checkout-field md:col-span-2"
                data-testid="input-checkout-address"
              />
              <input
                name="apartment"
                placeholder="Apartment, suite (optional)"
                className="checkout-field md:col-span-2"
                data-testid="input-checkout-apartment"
              />
              <input
                name="city"
                required
                placeholder="City *"
                className="checkout-field"
                data-testid="input-checkout-city"
              />
              <select
                name="province"
                required
                defaultValue=""
                className="checkout-field"
                data-testid="select-checkout-province"
              >
                <option value="" disabled>
                  Province *
                </option>
                <option>Punjab</option>
                <option>Sindh</option>
                <option>Khyber Pakhtunkhwa</option>
                <option>Balochistan</option>
                <option>Islamabad Capital Territory</option>
                <option>Gilgit-Baltistan</option>
                <option>Azad Jammu & Kashmir</option>
              </select>
              <input
                name="postalCode"
                required
                placeholder="Postal code *"
                className="checkout-field"
                data-testid="input-checkout-postal-code"
              />
            </div>
          </fieldset>
          <fieldset>
            <legend className="mb-4 font-display text-2xl">
              Payment method
            </legend>
            <label className="flex items-center gap-3 border border-[#a74636] bg-[#f0e9df] p-4 text-sm">
              <input type="radio" defaultChecked name="payment" value="cod" />{" "}
              Cash on Delivery
            </label>
          </fieldset>
          {error && (
            <p className="text-sm text-[#a74636]" role="alert">
              {error}
            </p>
          )}
          <button
            className="w-full bg-[#a74636] py-4 text-xs uppercase tracking-widest text-[#f6f1e8] transition hover:bg-[#843b42]"
            data-testid="button-place-order"
          >
            Place order
          </button>
        </form>
        <aside className="h-fit border border-[#ded2c4] bg-[#fbf7f1] p-6 lg:sticky lg:top-32">
          <p className="eyebrow text-[#a74636]">Order summary</p>
          {store.bag.map((item) => {
            const product = allProducts.find(
              (candidate) => candidate.id === item.id,
            );
            return product ? (
              <div
                key={`${item.id}-${item.size}`}
                className="mt-4 flex justify-between gap-4 text-sm"
              >
                <span>
                  {product.name}
                  <small className="block text-[#776b61]">
                    Size {item.size} · Qty {item.quantity}
                  </small>
                </span>
                <span>{money(product.price * item.quantity)}</span>
              </div>
            ) : null;
          })}
          <div className="mt-6 border-t border-[#ded2c4] pt-5 text-sm">
            <div className="flex justify-between">
              <span>Delivery</span>
              <span>{shipping ? money(shipping) : "Complimentary"}</span>
            </div>
            <div className="mt-4 flex justify-between font-display text-xl">
              <span>Total</span>
              <span>{money(total + shipping)}</span>
            </div>
          </div>
        </aside>
      </div>
    </div>
  );
}

function CollectionPage() {
  const { slug } = useParams<{ slug: string }>();
  const c = collections.find((x) => x.slug === slug);
  if (!c)
    return (
      <NotFound
        title="Collection not found"
        copy="This story has not been written yet."
        link="/collections"
      />
    );
  return (
    <>
      <div className="relative min-h-[560px] overflow-hidden text-[#f8f1e7]">
        <img
          src={c.image}
          alt={c.name}
          className="absolute inset-0 h-full w-full object-cover object-top"
        />
        <div className="absolute inset-0 bg-[#2f2925]/40" />
        <div className="relative flex min-h-[560px] items-end px-5 pb-14 md:px-12 md:pb-20">
          <div>
            <p className="eyebrow">{c.kicker}</p>
            <h1 className="mt-4 font-display text-6xl md:text-8xl">{c.name}</h1>
            <p className="mt-4 max-w-md text-sm leading-6">{c.description}</p>
          </div>
        </div>
      </div>
      <ListingPage
        mode="collection"
        title="The edit"
        forcedCollection={c.slug}
      />
    </>
  );
}
function CollectionsPage() {
  return (
    <div className="mx-auto max-w-[1440px] px-5 py-12 md:px-12 md:py-20">
      <p className="eyebrow text-[#a74636]">Stories in cloth</p>
      <h1 className="mt-4 font-display text-6xl md:text-8xl">Collections</h1>
      <div className="mt-14 grid gap-x-5 gap-y-14 md:grid-cols-2">
        {collections.map((c, i) => (
          <Link
            href={`/collection/${c.slug}`}
            className={`${i % 2 ? "md:mt-20" : ""} group`}
            key={c.slug}
            data-testid={`link-collection-${c.slug}`}
          >
            <div className="overflow-hidden">
              <img
                src={c.image}
                alt={c.name}
                className="aspect-[1.15] w-full object-cover transition duration-700 group-hover:scale-105"
              />
            </div>
            <p className="eyebrow mt-5 text-[#a74636]">{c.kicker}</p>
            <h2 className="mt-2 font-display text-4xl">{c.name}</h2>
            <p className="mt-2 max-w-md text-sm leading-6 text-[#776b61]">
              {c.description}
            </p>
          </Link>
        ))}
      </div>
    </div>
  );
}
function StaticPage({ kind }: { kind: string }) {
  const content: Record<
    string,
    { eyebrow: string; title: string; body: string[] }
  > = {
    about: {
      eyebrow: "The house of Fatima",
      title: "Clothes with a life ahead of them.",
      body: [
        "Fatima Wardrobe began with a simple question: what would it mean to make a Pakistani wardrobe that feels as good on its hundredth wear as its first?",
        "We work from Lahore with a small circle of makers, printers and embroiderers. The result is clothing with a sense of place, but no fixed occasion - pieces for the full, ordinary, beautiful span of a day.",
        "We care about cloth you can feel, colour that grows richer with time, and design that leaves room for you in it.",
      ],
    },
    contact: {
      eyebrow: "Come say hello",
      title: "We are here to help.",
      body: [
        "For questions about an order, sizing, styling or simply a piece you cannot stop thinking about, write to us.",
        "hello@fatimawardrobe.pk",
        "Mon-Sat 10:00-18:00 PKT | +92 300 123 4567",
      ],
    },
    shipping: {
      eyebrow: "The practical bit",
      title: "Delivery, considered.",
      body: [
        "Orders are carefully packed in Lahore and delivered across Pakistan within 3-5 working days.",
        "Delivery is PKR 250 on orders below PKR 5,000, and complimentary above that threshold. You will receive a message when your parcel is on its way.",
      ],
    },
    returns: {
      eyebrow: "If it is not quite right",
      title: "Returns made simple.",
      body: [
        "You may request a return within 7 days of delivery, provided the piece is unworn, unwashed and has its original tags attached.",
        "Start a return by writing to hello@fatimawardrobe.pk with your order number. Sale and made-to-order pieces are final sale.",
      ],
    },
    "size-guide": {
      eyebrow: "Find your fit",
      title: "Your shape, your way.",
      body: [
        "Our ready-to-wear pieces follow a relaxed Pakistani fit. If you prefer a closer line, we recommend sizing down.",
        "For specific measurements, write to hello@fatimawardrobe.pk and our team will help you choose. Unstitched sizes are listed as fabric cuts.",
      ],
    },
  };
  const c = content[kind] || content.about;
  return (
    <div className="relative bg-[#f6f1e8] min-h-[100dvh] pb-24">
      {/* Luxurious Hero Header */}
      <div className="w-full h-[35vh] min-h-[300px] relative overflow-hidden">
        <img src="/images/lux_lawn_1_1790430964918.jpg" alt="Client services" className="absolute inset-0 w-full h-full object-cover object-[center_35%]" />
        <div className="absolute inset-0 bg-gradient-to-t from-[#2f2925]/90 to-[#2f2925]/40" />
        <div className="absolute inset-0 flex flex-col items-center justify-center text-[#f8f1e7] z-10 px-5 text-center">
           <h1 className="font-display text-5xl md:text-7xl tracking-wide mb-2 reveal">Client Services</h1>
           <p className="eyebrow tracking-[0.25em] text-[#d2c6ba] reveal" style={{ animationDelay: '0.1s' }}>We are here to assist you</p>
        </div>
      </div>

      <div className="mx-auto max-w-[1200px] px-5 py-12 md:py-20 flex flex-col md:flex-row gap-12 md:gap-20 relative">
        
        {/* Luxury Sticky Sidebar */}
        <aside className="w-full md:w-[260px] shrink-0">
          <div className="md:sticky md:top-[120px]">
            <p className="eyebrow text-[#a74636] mb-8 tracking-[0.2em] border-b border-[#ded2c4] pb-4 uppercase">Help & Info</p>
            <ul className="flex flex-row md:flex-col gap-6 md:gap-5 overflow-x-auto whitespace-nowrap scrollbar-hide pb-4 md:pb-0">
              {[
                { label: "Our Story", href: "/about", key: "about" },
                { label: "Shipping", href: "/shipping", key: "shipping" },
                { label: "Returns", href: "/returns", key: "returns" },
                { label: "Size Guide", href: "/size-guide", key: "size-guide" },
                { label: "Contact", href: "/contact", key: "contact" }
              ].map(link => (
                <li key={link.key}>
                   <Link 
                     href={link.href} 
                     className={`flex items-center gap-3 text-[12px] tracking-[0.15em] uppercase transition-all duration-300 ${kind === link.key ? "text-[#2f2925] font-semibold" : "text-[#9c8c7d] hover:text-[#a74636]"}`}
                   >
                     {kind === link.key && <span className="w-3 h-[2px] bg-[#a74636]" />}
                     {link.label}
                   </Link>
                </li>
              ))}
            </ul>
          </div>
        </aside>
        
        {/* Content Area */}
        <div className="flex-1 max-w-2xl reveal" style={{ animationDelay: '0.2s' }}>
          <p className="eyebrow text-[#9c8c7d] tracking-[0.15em] mb-4">{c.eyebrow}</p>
          <h2 className="font-display text-4xl md:text-5xl text-[#2f2925] leading-[1.1]">
            {c.title}
          </h2>
          <div className="mt-10 space-y-8">
            {c.body.map((p, i) => (
              <p
                key={p}
                className="text-[16px] leading-8 text-[#776b61] font-light"
              >
                {p}
              </p>
            ))}
          </div>
          
          <div className="mt-20 pt-16 border-t border-[#ded2c4] grid grid-cols-1 sm:grid-cols-2 gap-8 md:gap-12 items-center">
            <img
              src="/images/lux_kurta_1_1790430926797.jpg"
              alt="Fatima Wardrobe editorial"
              className="aspect-[3/4] object-cover object-top w-full shadow-soft"
            />
            <div className="flex flex-col">
               <h3 className="font-display text-2xl text-[#2f2925] mb-4">Dedicated Support</h3>
               <p className="text-[#776b61] text-[15px] leading-7 font-light mb-8">
                 Our client care team in Lahore is available to assist with styling advice, detailed product information, and delivery queries.
               </p>
               <Link href="/contact" className="text-[11px] font-medium uppercase tracking-[0.2em] text-[#a74636] border-b border-[#a74636] w-fit pb-1 hover:text-[#2f2925] hover:border-[#2f2925] transition-colors">
                 Get in touch
               </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
function WishlistPage() {
  const store = useStore();
  const list = allProducts.filter((p) => store.wishlist.includes(p.id));
  return (
    <div className="mx-auto max-w-[1440px] px-5 py-12 md:px-12 md:py-20">
      <p className="eyebrow text-[#a74636]">Saved for later</p>
      <h1 className="mt-4 font-display text-6xl">Your wishlist.</h1>
      {list.length ? (
        <div className="mt-12 grid grid-cols-2 gap-x-3 gap-y-10 md:grid-cols-4 md:gap-x-5">
          {list.map((p) => (
            <ProductCard key={p.id} product={p} />
          ))}
        </div>
      ) : (
        <EmptyState
          title="Nothing saved yet."
          copy="When something stays on your mind, save it here."
          link="/new-in"
          label="Explore new in"
        />
      )}
    </div>
  );
}
function EmptyState({
  title,
  copy,
  link,
  label,
}: {
  title: string;
  copy: string;
  link: string;
  label: string;
}) {
  return (
    <div className="col-span-full py-24 text-center">
      <p className="font-display text-3xl">{title}</p>
      <p className="mx-auto mt-3 max-w-sm text-sm leading-6 text-[#776b61]">
        {copy}
      </p>
      <Link
        href={link}
        className="mt-7 inline-flex items-center gap-3 border-b border-[#a74636] pb-2 text-xs uppercase tracking-widest text-[#a74636]"
      >
        {label}
        <ArrowRight size={15} />
      </Link>
    </div>
  );
}
function NotFound({
  title = "Page not found",
  copy = "The page you were looking for has wandered off.",
  link = "/",
}: {
  title?: string;
  copy?: string;
  link?: string;
}) {
  return (
    <div className="mx-auto max-w-xl px-5 py-32 text-center md:py-44">
      <p className="eyebrow text-[#a74636]">404</p>
      <h1 className="mt-5 font-display text-6xl">{title}</h1>
      <p className="mt-4 text-sm leading-6 text-[#776b61]">{copy}</p>
      <Link
        href={link}
        className="mt-8 inline-flex items-center gap-3 border-b border-[#a74636] pb-2 text-xs uppercase tracking-widest text-[#a74636]"
      >
        Return to the wardrobe <ArrowLeft size={15} />
      </Link>
    </div>
  );
}
function AdminPreview() {
  const [type, setType] = useState("product");
  const [output, setOutput] = useState("");
  const [copied, setCopied] = useState(false);
  const generate = () => {
    const sample =
      type === "product"
        ? {
            id: "fw-new",
            slug: "new-piece",
            name: "New piece",
            category: "ready-to-wear",
            price: 6500,
            images: ["/images/new-piece.jpg"],
          }
        : type === "banner"
          ? {
              id: "hero-new",
              title: "A new chapter",
              desktopImage: "/images/hero.jpg",
              mobileImage: "/images/hero-mobile.jpg",
              href: "/new-in",
            }
          : {
              slug: "new-story",
              name: "New story",
              image: "/images/story.jpg",
            };
    setOutput(JSON.stringify(sample, null, 2));
  };
  return (
    <div className="mx-auto max-w-[950px] px-5 py-12 md:px-12 md:py-20">
      <p className="eyebrow text-[#a74636]">Developer convenience</p>
      <h1 className="mt-4 font-display text-6xl">Admin preview.</h1>
      <p className="mt-5 max-w-xl text-sm leading-6 text-[#776b61]">
        Draft the shape of a new product, banner or collection here, then copy
        the JSON into the local data file. This tool cannot mutate deployed
        files or create real catalogue entries.
      </p>
      <div className="mt-12 grid gap-8 md:grid-cols-2">
        <div>
          <label className="eyebrow mb-3 block">Generate a template</label>
          <select
            value={type}
            onChange={(e) => setType(e.target.value)}
            className="w-full border border-[#cfc1b1] bg-transparent p-3 text-sm"
            data-testid="select-admin-type"
          >
            <option value="product">Product</option>
            <option value="banner">Banner</option>
            <option value="collection">Collection</option>
          </select>
          <button
            onClick={generate}
            className="mt-4 bg-[#a74636] px-5 py-4 text-xs uppercase tracking-widest text-[#f6f1e8]"
            data-testid="button-generate-json"
          >
            Generate JSON
          </button>
          {output && (
            <div className="mt-7 flex gap-3">
              <button
                onClick={() => {
                  navigator.clipboard?.writeText(output);
                  setCopied(true);
                }}
                className="border border-[#a74636] px-4 py-3 text-xs uppercase tracking-widest"
                data-testid="button-copy-json"
              >
                {copied ? "Copied" : "Copy JSON"}
              </button>
              <a
                href={`data:application/json;charset=utf-8,${encodeURIComponent(output)}`}
                download={`${type}.json`}
                className="border border-[#cfc1b1] px-4 py-3 text-xs uppercase tracking-widest"
                data-testid="link-download-json"
              >
                Download
              </a>
            </div>
          )}
        </div>
        <pre
          className="min-h-64 overflow-auto bg-[#2f2925] p-5 text-xs leading-6 text-[#d8cabb]"
          data-testid="text-admin-output"
        >
          {output || "// Your JSON template will appear here."}
        </pre>
      </div>
    </div>
  );
}

function NewInSubRoute() {
  const { mode, sub } = useParams<{ mode: string, sub: string }>();
  const title = sub ? sub.split('-').map(x => x.charAt(0).toUpperCase() + x.slice(1)).join(' ') : 'Subcategory';
  return <ListingPage mode={mode || 'new-in'} title={title} hideSubcategories={true} />;
}

function Router() {
  return (
    <Switch>
      <Route path="/" component={Home} />
      <Route path="/new-in">
        <ListingPage
          mode="new-in"
          title="New in"
        />
      </Route>
      <Route path="/new-in/:sub">
        <NewInSubRoute />
      </Route>
      <Route path="/ready-to-wear/:sub">
        <NewInSubRoute />
      </Route>
      <Route path="/ready-to-wear">
        <ListingPage
          mode="ready-to-wear"
          title="Ready to wear"
          description="The pieces you reach for without thinking twice — cut for movement, made for repeat wear."
        />
      </Route>
      <Route path="/unstitched">
        <ListingPage
          mode="unstitched"
          title="Unstitched"
          description="Prints, embroideries and cloth with room for your own point of view."
        />
      </Route>
      <Route path="/accessories">
        <ListingPage
          mode="accessories"
          title="Accessories"
          description="Small details with a long life."
        />
      </Route>
      <Route path="/sale">
        <ListingPage
          mode="sale"
          title="Sale"
          description="Last looks, considered prices."
        />
      </Route>
      <Route path="/collections" component={CollectionsPage} />
      <Route path="/category/:slug">
        <CategoryRoute />
      </Route>
      <Route path="/collection/:slug">
        <CollectionPage />
      </Route>
      <Route path="/product/:slug">
        <ProductDetail />
      </Route>
      <Route path="/search">
        <SearchPage />
      </Route>
      <Route path="/wishlist" component={WishlistPage} />
      <Route path="/cart" component={CartPage} />
      <Route path="/checkout" component={Checkout} />
      <Route path="/about">
        <StaticPage kind="about" />
      </Route>
      <Route path="/contact">
        <StaticPage kind="contact" />
      </Route>
      <Route path="/shipping">
        <StaticPage kind="shipping" />
      </Route>
      <Route path="/returns">
        <StaticPage kind="returns" />
      </Route>
      <Route path="/size-guide">
        <StaticPage kind="size-guide" />
      </Route>
      <Route path="/admin-preview" component={AdminPreview} />
      <Route>
        <NotFound />
      </Route>
    </Switch>
  );
}
function SubcategoryRoute() {
  const { category, subcategory } = useParams<{
    category: string;
    subcategory: string;
  }>();
  const valid = ["ready-to-wear", "unstitched", "accessories"];
  return valid.includes(category) ? (
    <ListingPage
      mode={category}
      title={subcategory.replaceAll("-", " ")}
      forcedSubcategory={subcategory}
    />
  ) : (
    <NotFound />
  );
}
function CategoryRoute() {
  const { slug } = useParams<{ slug: string }>();
  const c = categories.find((x) => x.slug === slug);
  return c ? (
    <ListingPage mode={c.slug} title={c.name} description={c.description} />
  ) : (
    <NotFound
      title="Category not found"
      copy="That edit is not in the current wardrobe."
      link="/new-in"
    />
  );
}
function SearchPage() {
  const [q, setQ] = useState("");
  const found = allProducts.filter(
    (p) =>
      `${p.name} ${p.category} ${p.collection} ${p.fabric}`
        .toLowerCase()
        .includes(q.toLowerCase()) && q,
  );
  return (
    <div className="mx-auto max-w-[1440px] px-5 py-12 md:px-12 md:py-20">
      <p className="eyebrow text-[#a74636]">Search</p>
      <h1 className="mt-4 font-display text-6xl">Find your piece.</h1>
      <div className="mt-10 flex max-w-2xl items-center border-b border-[#2f2925]">
        <Search size={20} />
        <input
          autoFocus
          value={q}
          onChange={(e) => setQ(e.target.value)}
          placeholder="Search products, fabric or collections"
          className="w-full bg-transparent px-4 py-4 outline-none"
          data-testid="input-search-page"
        />
      </div>
      {q && (
        <>
          <p className="mt-10 text-sm text-[#776b61]">{found.length} results</p>
          <div className="mt-6 grid grid-cols-2 gap-x-3 gap-y-10 md:grid-cols-4 md:gap-x-5">
            {found.map((p) => (
              <ProductCard key={p.id} product={p} />
            ))}
          </div>
        </>
      )}
    </div>
  );
}

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <TooltipProvider>
        <StoreProvider>
          <WouterRouter base={import.meta.env.BASE_URL.replace(/\/$/, "")}>
            <ErrorBoundary resetKey={window.location.pathname}>
              <Shell>
                <Router />
              </Shell>
            </ErrorBoundary>
          </WouterRouter>
          <Toaster />
        </StoreProvider>
      </TooltipProvider>
    </QueryClientProvider>
  );
}
export default App;
