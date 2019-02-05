class Entry:
    exchange_domain = ''
    seller_account_id = ''
    account_type = ''
    tag_id = ''

    def __init__(self, site_domain: str, data_row: list):
        self.site_domain = site_domain
        self.exchange_domain = data_row[0].strip().lower() if len(data_row) > 0 else ''
        self.seller_account_id = data_row[1].strip().lower() if len(data_row) > 1 else ''
        self.account_type = data_row[2].strip().lower() if len(data_row) > 2 else ''
        self.tag_id = data_row[3].strip().lower() if len(data_row) > 3 else ''

