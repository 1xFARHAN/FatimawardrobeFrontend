import urllib.request
import re

url = 'https://pk.sapphireonline.pk/collections/new-in'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    # Sapphire uses Shopify, so images are on cdn.shopify.com
    images = re.findall(r'https://cdn\.shopify\.com/s/files/[^\"\'\s]+\.(?:jpg|webp)', html)
    images = list(set([img for img in images if 'width=1' not in img and 'swatch' not in img]))
    for img in images[:15]:
        print(img)
except Exception as e:
    print(e)
