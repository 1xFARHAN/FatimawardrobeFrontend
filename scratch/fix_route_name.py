import re

filepath = r'artifacts\fatima-wardrobe\src\App.tsx'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace my injected SubcategoryRoute with NewInSubRoute
text = text.replace('function SubcategoryRoute() {\n  const { mode, sub }', 'function NewInSubRoute() {\n  const { mode, sub }')
text = text.replace('<SubcategoryRoute />', '<NewInSubRoute />')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed route name")
