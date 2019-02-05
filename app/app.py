from app.crawler import crawl_to_db
from app.dbwrite import process_row_to_db


class App:
    crawl_url_queue = []

    def queue(self, url: str):
        self.crawl_url_queue.append(url)

    def queueFile(self, filename: str):
        self.crawl_url_queue += crawl_to_db(filename)

    def run(self):

        if len(self.crawl_url_queue) == 0:
            raise Exception('Queue is empty')

        for url in self.crawl_url_queue:
            records = crawl_to_db(url + "/ads.txt")
            for record in records:
                process_row_to_db(record)

