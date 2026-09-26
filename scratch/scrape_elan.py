import urllib.request
import re

url = 'https://elan.pk/collections/unstitched'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    images = re.findall(r'https://cdn\.shopify\.com/s/files/[^\"\'\s]+\.(?:jpg|webp)', html)
    images = list(set([img for img in images if 'width=1' not in img and 'swatch' not in img]))
    for img in images[:5]:
        print(img)
except Exception as e:
    print(e)
