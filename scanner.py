#!/usr/bin/env python3
import requests
import sys
def banner():
    print("scanner-pro by Ali-Dev-2026")
    print("USDT: TVsCuv2qg929pXHQPcmQKDGUsqb3k9Maoi")
def check(url):
    if not url.startswith('http'):
        url = 'https://' + url
    r = requests.get(url, timeout=10)
    print(f"Status: {r.status_code}")
if __name__ == "__main__":
    banner()
    if len(sys.argv) > 1:
        check(sys.argv[1])
    else:
        print("Use: python3 scanner.py google.com")
