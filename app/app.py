from app.crawler import crawl_to_db
from app.queue import load_url_queue
from app.dbwrite import process_row_to_db
from app.dbwrite import cleandb
from urllib.parse import urlparse


class App:
    crawl_url_queue = []

    def queue(self, url: str):
        self.crawl_url_queue.append(url)

    def queueFile(self, filename: str):
        self.crawl_url_queue += load_url_queue(filename)

    def run(self):

        if len(self.crawl_url_queue) == 0:
            raise Exception('Queue is empty')

        for url in self.crawl_url_queue:
            o = urlparse(url)
            site_domain = o.hostname

            cleandb(site_domain)

            try:
                records = crawl_to_db(site_domain, url + "/ads.txt")
                for record in records:
                    process_row_to_db(record)
            except:
                # TODO: logging
                pass

