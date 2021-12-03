#!usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import urlparse

def request(url):
    try:
        return requests.get(url)

    except requests.exceptions.ConnectionError:
        pass

target_url = raw_input("Enter the URL---->")
response = request(target_url)
#print(response.content)
parsed_html = BeautifulSoup(response.content)
forms_list = parsed_html.findAll("form")
for form in forms_list:
    #print(form)
    action = form.get("action")
    post_url = urlparse.urljoin(target_url,action)
    print(post_url)
    #print(action)
    method = form.get("method")
    #print(method)

    input_lists = form.findAll("input")
    post_data = {}
    for input in input_lists:
        input_name = input.get("name")
        #print(input_name)
        input_type = input.get("type")
        input_value = input.get("value")
        if input_type == "text":
            input_value = "test"
        post_data[input_name] = input_value
    result = requests.post(post_url, data=post_data)
    print(result.content)
