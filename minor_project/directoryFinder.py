# /usr/bin/env python3
import requests
from colors import GREEN, RESET
from banners import directory

print(GREEN, directory, RESET)
target_url = input("Enter URL ")


def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


with open('/usr/share/wordlists/dirb/common.txt', 'r') as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
            print(GREEN, "[+] Discovered url ----> " + test_url, RESET)
