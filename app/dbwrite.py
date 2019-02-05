from app.entry import Entry
import psycopg2


def process_row_to_db(row: Entry):
    conn = psycopg2.connect("dbname='template1' user='dbuser' host='localhost' password='dbpass'")

    insert_stmt = "INSERT OR IGNORE INTO adstxt " \
                  "(SITE_DOMAIN, EXCHANGE_DOMAIN, SELLER_ACCOUNT_ID, ACCOUNT_TYPE, TAG_ID, ENTRY_COMMENT) " \
                  "VALUES (?, ?, ?, ?, ?, ? );"

    print("%s %s %s %s %s" % (row.site_domain, row.exchange_domain, row.seller_account_id, row.account_type, row.tag_id))
