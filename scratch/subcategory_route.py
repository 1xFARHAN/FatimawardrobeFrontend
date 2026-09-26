import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update ListingPage props signature to include hideSubcategories
prop_pattern = r'forcedSubcategory,\s*\}\:\s*\{\s*mode:\s*string;\s*title:\s*string;\s*description\?:\s*string;\s*forcedCollection\?:\s*string;\s*forcedSubcategory\?:\s*string;\s*\}\)\s*\{'
prop_replacement = """forcedSubcategory,
  hideSubcategories = false,
}: {
  mode: string;
  title: string;
  description?: string;
  forcedCollection?: string;
  forcedSubcategory?: string;
  hideSubcategories?: boolean;
}) {"""
text = re.sub(prop_pattern, prop_replacement, text, flags=re.DOTALL)

# 2. Update Breadcrumbs in ListingPage
breadcrumb_pattern = r'<p className="text-xs text-\[#776b61\]">\s*<Link href="/">Home</Link> <span className="mx-2">›</span> <span className="font-medium text-\[#2f2925\]">\{title\}</span>\s*</p>'
breadcrumb_replacement = """<p className="text-xs text-[#776b61]">
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
        </p>"""
text = re.sub(breadcrumb_pattern, breadcrumb_replacement, text, flags=re.DOTALL)

# 3. Update the circular thumbnails to be conditional and wrapped in Links
circles_pattern = r'<div className="mx-auto max-w-\[1440px\] px-5 md:px-12 py-6 overflow-x-auto scrollbar-hide">\s*<div className="flex items-start justify-center gap-6 md:gap-10 min-w-max mx-auto">\s*\{subCategories\.map\(\(sub, idx\) => \(\s*<div key=\{idx\} className="flex flex-col items-center gap-3 w-20 md:w-24 cursor-pointer group">\s*<div className="w-20 h-20 md:w-24 md:h-24 rounded-full overflow-hidden border-2 border-transparent group-hover:border-\[#2f2925\] transition-colors p-\[2px\]">\s*<img src=\{sub\.img\} alt=\{sub\.name\} className="w-full h-full object-cover rounded-full" />\s*</div>\s*<span className="text-\[10px\] md:text-\[11px\] text-center leading-tight text-\[#776b61\] group-hover:text-\[#2f2925\]">\{sub\.name\}</span>\s*</div>\s*\)\}\s*</div>\s*</div>'

circles_replacement = """{!hideSubcategories && (
        <div className="mx-auto max-w-[1440px] px-5 md:px-12 py-6 overflow-x-auto scrollbar-hide">
          <div className="flex items-start justify-center gap-6 md:gap-10 min-w-max mx-auto">
            {subCategories.map((sub, idx) => (
              <Link key={idx} href={`/${mode}/${encodeURIComponent(sub.name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)+/g, ''))}`}>
                <div className="flex flex-col items-center gap-3 w-20 md:w-24 cursor-pointer group">
                  <div className="w-20 h-20 md:w-24 md:h-24 rounded-full overflow-hidden border-2 border-transparent group-hover:border-[#2f2925] transition-colors p-[2px]">
                    <img src={sub.img} alt={sub.name} className="w-full h-full object-cover rounded-full" />
                  </div>
                  <span className="text-[10px] md:text-[11px] text-center leading-tight text-[#776b61] group-hover:text-[#2f2925]">{sub.name}</span>
                </div>
              </Link>
            ))}
          </div>
        </div>
      )}"""
text = re.sub(circles_pattern, circles_replacement, text, flags=re.DOTALL)

# 4. Add Subcategory Route Component right before Router
subroute = """function SubcategoryRoute() {
  const { mode, sub } = useParams<{ mode: string, sub: string }>();
  const title = sub ? sub.split('-').map(x => x.charAt(0).toUpperCase() + x.slice(1)).join(' ') : 'Subcategory';
  return <ListingPage mode={mode || 'new-in'} title={title} hideSubcategories={true} />;
}

function Router() {"""
text = text.replace('function Router() {', subroute)

# 5. Add the new routes to Router
router_pattern = r'<Route path="/new-in">\s*<ListingPage\s*mode="new-in"\s*title="New in"\s*description="[^"]*"\s*/>\s*</Route>'
router_replacement = """<Route path="/new-in">
        <ListingPage
          mode="new-in"
          title="New in"
        />
      </Route>
      <Route path="/new-in/:sub">
        <SubcategoryRoute />
      </Route>
      <Route path="/ready-to-wear/:sub">
        <SubcategoryRoute />
      </Route>"""
text = re.sub(router_pattern, router_replacement, text, flags=re.DOTALL)


with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updates applied")
