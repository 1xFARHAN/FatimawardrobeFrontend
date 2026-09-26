import urllib.request
import re

url = 'https://pk.khaadi.com/ready-to-wear/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    images = re.findall(r'https://pk\.khaadi\.com/dw/image/v2/[a-zA-Z0-9_]+/[a-zA-Z0-9_]+/[a-zA-Z0-9_]+/[^\"\'\s]+\.(?:jpg|png)', html)
    if not images:
        images = re.findall(r'https://[^\"\'\s]+\.jpg', html)
    images = list(set([img for img in images if 'swatch' not in img.lower() and 'category' not in img.lower()]))
    for img in images[:25]:
        print(img)
except Exception as e:
    print(e)
