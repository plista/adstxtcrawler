import requests
import re
from app.entry import Entry


def crawl_to_db(hostname: str, url: str):
    r = requests.get(url, headers={
        'User-Agent': 'AdsTxtCrawler/1.0; +https://github.com/InteractiveAdvertisingBureau/adstxtcrawler',
        'Accept': 'text/plain',
        "Upgrade-Insecure-Requests": "1"
    }, timeout=5.0, allow_redirects=True)

    if r.status_code != 200:
        raise Exception("Error crawling %s, status code = %s" % (url, r.status_code))

    if not re.search(r"ads\.txt$", r.url):
        raise Exception("invalid redirect to %s" % url)

    return line_to_entry(r.text, hostname)


def line_to_entry(lines, hostname=""):
    return [Entry(hostname, line.split("#", 1)[0].rstrip('\n').split(",")) for line in lines.splitlines() if
            not line.startswith('#') and not len(line) == 0]
