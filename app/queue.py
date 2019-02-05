def load_url_queue(csvfilename) -> list:
    return [line.rstrip('\n') for line in open(csvfilename)]
