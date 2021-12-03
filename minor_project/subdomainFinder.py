#!usr/bin/env python3
import requests
from colors import GREEN, RESET, RED
from banners import subdomain

print(GREEN, subdomain, RESET)

target_url = input("enter url ")


def request(url):
    try:
        return requests.get("http://" + url)

    except requests.exceptions.ConnectionError:
        pass


with open("/home/kali/minor_project/sub.txt", "r") as wordlist_file:
    for line in wordlist_file:
        # print(line)
        word = line.strip()
        test_url = word + '.' + target_url
        # print(test_url)
        try:
            response = request(test_url)
        except KeyboardInterrupt:
            print(RED, "[-] Exiting program..........", RESET)
            break

        if response:
            print(GREEN, "[+] Discovered subdomain ----> " + test_url, RESET)
