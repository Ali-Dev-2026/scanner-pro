import requests
import sys
print("scanner-pro by Ali-Dev-2026")
def check(url):
    if not url.startswith('http'):
        url = 'https://' + url
    r = requests.get(url, timeout=10)
    print(f"Status: {r.status_code}")
    for h in r.headers:
        print(h)
if len(sys.argv) > 1:
    check(sys.argv[1])
else:
    print("Usage: python3 scanner.py example.com")
