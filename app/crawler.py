import requests
from app.entry import Entry
from urllib.parse import urlparse


def crawl_to_db(url: str):
    r = requests.get(url, headers={
        'User-Agent': 'AdsTxtCrawler/1.0; +https://github.com/InteractiveAdvertisingBureau/adstxtcrawler',
        'Accept': 'text/plain',
    })

    if r.status_code != 200:
        raise Exception("Error crawling %s, status code = %s" % (url, r.status_code))

    o = urlparse(url)
    return [Entry(o.hostname, line.rstrip('\n').split(",")) for line in r.text.splitlines() if not line.startswith('#')]
