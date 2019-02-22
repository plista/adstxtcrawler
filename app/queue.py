def load_url_queue(csvfilename) -> list:
    return [("http://%s" % line).rstrip('\n') for line in open(csvfilename)]
