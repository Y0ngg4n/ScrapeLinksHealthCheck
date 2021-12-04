from scrapy.crawler import CrawlerProcess, Settings
from crawler import Crawler
import json
import os
import progressbar
import requests
import time


def crawl(cfg):
    process = CrawlerProcess(Settings())
    print(cfg["start_urls"])
    process.crawl(Crawler, name=cfg["name"], allowed_domains=cfg["allowed_domains"], start_urls=cfg["start_urls"])
    process.start()
    print("Starting crawling for " + cfg["name"])


def check_online():
    files = os.listdir("links")
    links = []
    online = 0
    online_size = 0
    offline = 0
    offline_size = 0
    print("Getting all links")
    for f in files:
        read_file = open(os.path.join("links", f), "r")
        lines = read_file.readlines()
        for line in lines:
            links.append(line.replace("\n", ""))
    widgets = [' [',
               progressbar.Timer(format='elapsed time: %(elapsed)s'),
               '] ',
               progressbar.Bar('*'), ' (',
               progressbar.ETA(), ') ',
               ]
    bar = progressbar.ProgressBar(widgets=widgets, maxval=len(links)).start()
    print("Requesting links")
    for i in range(0, len(links)):
        bar.update(i)
        r = requests.head(links[i])
        print()
        if r.status_code == 200:
            online = online + 1
            try:
                online_size = online_size + int(r.headers.get('Content-Length'))
            except:
                pass
        else:
            offline = offline + 1
            try:
                offline_size = offline_size + int(r.headers.get('Content-Length'))
            except:
                pass
    print("\nOnline: " + str(online))
    print("Offline: " + str(offline))
    print("Online Size: " + str(online_size))
    print("Offline Size: " + str(offline_size))
    print("Total: " + str(len(links)))


if __name__ == '__main__':
    os.makedirs("links", exist_ok=True)
    with (open("config.json", "r")) as cf:
        metadata = json.load(cf)
        for cfg in metadata:
            crawl(cfg)
    print("Crawled all Websites")
    print("########################")
    print("Checking availability now")
    while True:
        print("########################")
        check_online()
        print("Check again in 10 sec ...")
        time.sleep(10)
