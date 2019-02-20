from app.entry import Entry
import psycopg2
import os


def process_row_to_db(row: Entry):
    conn = psycopg2.connect(dbname=os.getenv("DB_NAME"), user=os.getenv("DB_USER"), host=os.getenv("DB_HOST"), password=os.getenv("DB_PASSWORD"))

    insert_stmt = "INSERT INTO adstxt " \
                  "(SITE_DOMAIN, EXCHANGE_DOMAIN, SELLER_ACCOUNT_ID, ACCOUNT_TYPE, TAG_ID) " \
                  "VALUES (%s, %s, %s, %s, %s);"
    args = (row.site_domain, row.exchange_domain, row.seller_account_id, row.account_type, row.tag_id)

    cur = conn.cursor()
    cur.execute(insert_stmt, args)

    conn.commit()
