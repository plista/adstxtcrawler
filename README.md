A crawler for ads.txt files given a list of URLs or domains etc and saves them to a SQLite DB table.

## Usage
```
usage: adstxt_crawler.py [-h] [--url URL] [--source SOURCE] [--target TARGET]
                         --filter FILTER [--verbose]

Loads adstxt from publishers and matches with filter.

optional arguments:
  -h, --help       show this help message and exit
  --url URL        single hostname to test
  --source SOURCE  Source file with 1 line per publisher
  --target TARGET  Target file with 1 line per publisher
  --filter FILTER  e.g. appnexus.com, 3563, DIRECT
  --verbose        increase output verbosity
```

## License
The open source license used is the 2-clause BSD license

