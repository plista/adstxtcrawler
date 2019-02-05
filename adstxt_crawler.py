import sys
import logging
from optparse import OptionParser
from app.app import App

arg_parser = OptionParser()
arg_parser.add_option("-f", "--file", dest="target_filename",
                      help="list of domains to crawl ads.txt from", metavar="FILE")
arg_parser.add_option("-u", "--url", dest="target_domain",
                      help="Domains to crawl ads.txt from", metavar="FILE")
arg_parser.add_option("-d", "--database", dest="target_database",
                      help="Database to dump crawled data into", metavar="FILE")
arg_parser.add_option("-v", "--verbose", dest="verbose", action='count',
                      help="Increase verbosity (specify multiple times for more)")

(options, args) = arg_parser.parse_args()

if len(sys.argv) == 1:
    arg_parser.print_help()
    exit(1)

log_level = logging.WARNING

if options.verbose == 1:
    log_level = logging.INFO
elif options.verbose == 2:
    log_level = logging.DEBUG

logging.basicConfig(filename='adstxt_crawler.log', level=log_level,
                    format='%(asctime)s %(filename)s:%(lineno)d:%(levelname)s  %(message)s')

app = App()
if options.target_domain:
    app.queue(options.target_domain)

if options.target_filename:
    app.queueFile(options.target_filename)

app.run()
