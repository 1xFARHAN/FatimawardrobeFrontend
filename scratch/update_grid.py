import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Update ListingPage grid
grid_pattern = r'<div className="grid grid-cols-2 gap-x-2 gap-y-12 md:grid-cols-3 md:gap-x-10 md:gap-y-24">'
grid_replacement = '<div className="grid grid-cols-2 gap-x-2 gap-y-12 md:grid-cols-4 md:gap-x-8 md:gap-y-20">'
new_text = text.replace(grid_pattern, grid_replacement)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Done")
