#ScrapeLinksHealthCheck
This Project aims to collect bad links (e.g. from Forums) and collect them into files.
After it scraped the links, it checks the health of them every 10 sec

Idea from Strg_F https://www.youtube.com/watch?v=iItLpwkQMUQ&t=9s

It is mainly made for reporting link lists to clearnet hosters of darknet forums.

## Installation
- [Install Python](https://realpython.com/installing-python/)
- Clone the repository: ```bash git clone https://github.com/Y0ngg4n/ScrapeLinksHealthCheck.git```
- Change the directory: ```bash cd ScrapeLinksHealthCheck```
- Install dependencies: ```bash pip install -r requirements.txt```
- Configure the script:
  - Add all websites to scrape into `config.json`
  - `name`: Just give it a random name
  - `allowed_domains`: If you want to restrict the links to domains to crawl (recommended: Leave as empty array: [] )
  - `start_urls`: The link where to start the scraping

## Usage
```bash python main.py```
The script will make a directory called `links`.
There will be all links scraped ordered by the different domain names.

## Onion Sites
To use with the Tor network for onion sites just route all your traffic of the system throught the Tor Network.
[Learn how to do that](https://www.wikihow.com/Route-All-Network-Traffic-Through-the-Tor-Network)

## Features
- [x] Crawl all pages
- [x] Scrape links
- [x] Check health of links
- [] Scrape links written as text
- [] Add login/authentication
- [] Add automatically report to the hosters
