from app.app import App
import argparse
import logging
import sys

parser = argparse.ArgumentParser(description='Loads adstxt from publishers and matches with filter.')
parser.add_argument('--url', help='Source file with 1 line per publisher')
parser.add_argument('--source', help='Source file with 1 line per publisher')
parser.add_argument('--target', help='Target file with 1 line per publisher')
parser.add_argument('--filter', help='e.g. appnexus.com, 3563, DIRECT', required=True, action='append')
parser.add_argument('--verbose', help="increase output verbosity", action="store_true")
args = parser.parse_args()

if args.verbose:
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

app = App(args.filter)
if args.url:
    app.queue(args.url)
if args.source:
    app.queueFile(args.source)
metrics = app.run(app.target)
print(metrics)
