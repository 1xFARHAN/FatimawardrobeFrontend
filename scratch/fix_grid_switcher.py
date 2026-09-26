import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add state for columns
state_pattern = r'const \[filterOpen, setFilterOpen\] = useState\(false\);'
state_repl = 'const [filterOpen, setFilterOpen] = useState(false);\n  const [columns, setColumns] = useState(4);'
if re.search(state_pattern, text):
    text = re.sub(state_pattern, state_repl, text)

# 2. Update layout switchers
switcher_pattern = r'<div className="flex items-center gap-2 md:gap-3 text-\[#cfc1b1\]">\s*<div className="hidden md:flex gap-1 h-5 cursor-pointer hover:text-\[#2f2925\]"><div className="w-2 h-full border border-current"></div><div className="w-2 h-full border border-current"></div></div>\s*<div className="hidden md:flex gap-1 h-5 cursor-pointer hover:text-\[#2f2925\]"><div className="w-1\.5 h-full border border-current"></div><div className="w-1\.5 h-full border border-current"></div><div className="w-1\.5 h-full border border-current"></div></div>\s*<div className="flex gap-\[2px\] h-5 cursor-pointer text-\[#2f2925\]"><div className="w-\[6px\] h-full border border-current"></div><div className="w-\[6px\] h-full border border-current"></div><div className="w-\[6px\] h-full border border-current"></div><div className="w-\[6px\] h-full border border-current"></div></div>\s*</div>'

switcher_repl = """<div className="flex items-center gap-2 md:gap-3 text-[#cfc1b1]">
            <div onClick={() => setColumns(2)} className={`hidden md:flex gap-1 h-5 cursor-pointer transition-colors hover:text-[#2f2925] ${columns === 2 ? 'text-[#2f2925]' : ''}`}><div className="w-2 h-full border border-current"></div><div className="w-2 h-full border border-current"></div></div>
            <div onClick={() => setColumns(3)} className={`hidden md:flex gap-1 h-5 cursor-pointer transition-colors hover:text-[#2f2925] ${columns === 3 ? 'text-[#2f2925]' : ''}`}><div className="w-1.5 h-full border border-current"></div><div className="w-1.5 h-full border border-current"></div><div className="w-1.5 h-full border border-current"></div></div>
            <div onClick={() => setColumns(4)} className={`hidden md:flex gap-[2px] h-5 cursor-pointer transition-colors hover:text-[#2f2925] ${columns === 4 ? 'text-[#2f2925]' : ''}`}><div className="w-[6px] h-full border border-current"></div><div className="w-[6px] h-full border border-current"></div><div className="w-[6px] h-full border border-current"></div><div className="w-[6px] h-full border border-current"></div></div>
          </div>"""

if re.search(switcher_pattern, text):
    text = re.sub(switcher_pattern, switcher_repl, text)

# 3. Update grid container
grid_pattern = r'<div className="grid grid-cols-2 gap-2 md:grid-cols-4 md:gap-3">'
grid_repl = '<div className={`grid grid-cols-2 gap-2 md:gap-3 ${columns === 2 ? "md:grid-cols-2" : columns === 3 ? "md:grid-cols-3" : "md:grid-cols-4"}`}>'
if re.search(grid_pattern, text):
    text = re.sub(grid_pattern, grid_repl, text)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Listing page grid layout switchers are now working!")
