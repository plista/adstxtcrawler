from app.crawler import crawl_to_db, line_to_entry
from app.queue import load_url_queue


class App:
    crawl_url_queue = []

    def __init__(self, txt_filter: list):
        self.filters = txt_filter

    def queue(self, url: str):
        self.crawl_url_queue.append(url)

    def queueFile(self, filename: str):
        self.crawl_url_queue += load_url_queue(filename)

    def is_match(self, compares, site_domain):
        try:
            url = "http://%s" % site_domain
            records = crawl_to_db(site_domain, url + "/ads.txt")
            for compare in compares:
                for record in records:
                    if record.match(compare):
                        return True
        except Exception as e:
            print("Something went wrong %s" % e.args)
        return False

    def get_compare_objects(self):
        compares = []
        for filter in self.filters:
            matches = line_to_entry(filter)
            if len(matches) != 1:
                raise Exception("invalid rule: %s" % filter)
            compares.append(matches[0])
        return compares

    def run(self, target):
        if len(self.crawl_url_queue) == 0:
            raise Exception('Queue is empty')

        compares = self.get_compare_objects()

        matches = 0
        misses = 0
        with open(target, "a") as myfile:
            for site_domain in self.crawl_url_queue:
                is_match = self.is_match(compares, site_domain)
                myfile.write("%s,%s\n" % (site_domain, is_match))

                if is_match:
                    matches = matches + 1
                else:
                    misses = misses + 1

        return {
            "matches": matches,
            "misses": misses
        }

