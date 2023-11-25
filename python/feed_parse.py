#!/usr/bin/python3

import os
import sys
import requests
import xml.etree.ElementTree as ET


def main():
    # grab the first argument passed in on the command line after the script
    url = sys.argv[1]

    r = requests.get(url, verify=False)
    if not r.ok:
        print(f"Request was invalid and returned a non-200 response code of {r.status_code}")
        return

    # the content from requests comes back as raw bytes, decode that to a string first
    xml_string = r.content.decode()

    # the root of the XML (rss part only)
    root = ET.fromstring(xml_string)

    # the first element in root has all the actual feed data. this searchs for "title"
    show_title = root[0].find("title").text

    # get the length/count of the list of the number of "item" (episodes)
    episodes = len(list(root.iter("item")))

    # clear the terminal again
    os.system("clear")

    print(f"Show: {show_title}")
    print(f"Episode Count: {episodes}")

    print("Episodes:")

    for ep_title in list(root.iter("item")):
        print("   -", ep_title.find("title").text)


if __name__ == "__main__":
    main()
