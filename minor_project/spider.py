# /usr/bin/env python3
import requests
from colors import GREEN, RESET
from banners import spider
import re  # module for regular expression
import urllib.parse as urlparse

print(GREEN, spider, RESET)
target_url = input("Enter URL ")
target_link = []


def extract_link_from(url):
    response = requests.get(target_url)
    return re.findall('(?:href=")(.*?)"', response.content.decode(errors="ignore"))


def crawl(url):
    href_links = extract_link_from(url)
    # print(href_links)
    for link in href_links:
        link = urlparse.urljoin(url, link)
        if "#" in link:
            link = link.split('#')[0]
        if url in link and link not in target_link:
            target_link.append(link)
            print(GREEN, link, RESET)
            crawl(link)


crawl(target_url)
