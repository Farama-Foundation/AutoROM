import requests
from bs4 import BeautifulSoup
import os

top_url = "https://www.gamulator.com/roms/atari-2600/"
r = requests.get(top_url)
soup = BeautifulSoup(r.content, "html5lib")
root_dir = os.path.expanduser("~")

links = soup.findAll("a")
links = filter(lambda x: x.get("class") == None, links)
links = filter(lambda x: x.get("href").startswith("/roms/atari-2600"), links)
links = filter(lambda x: x.find_all("picture") == [],links)
for l in links:
    sub_href = l["href"]
    sub_href = sub_href[16:]
    new_url = top_url + sub_href+"/download"
    sub_url = requests.get(new_url)
    sub_soup = BeautifulSoup(sub_url.content, "html5lib")
    sub_links = sub_soup.find_all("a")
    sub_links = filter(lambda  x: x.get("href").startswith("https://downloads"), sub_links)
    # should only be 1 link
    for s in sub_links:
        download_link = s.get("href")
        download_req = requests.get(download_link)
        file_title = root_dir + sub_href
        open(file_title,"wb").write(download_req.content)
    print("Downloaded ", sub_href[1:])

    