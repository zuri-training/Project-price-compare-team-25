import sqlite3
from products import scraper as wb


conn = sqlite3.connect("db.sqlite3")
conn.row_factory = lambda c, row: row
c = conn.cursor()
c.execute("""SELECT url_jumia, url_konga, url_kara
             FROM products_product""")
database_urls = c.fetchall()


for rows in database_urls:
    for url in rows:
        if "jumia.com" in url:
            jumia_price = wb.jumia(url)
            print(jumia_price)
            c.execute("""UPDATE products_product
                         SET price_jumia=?
                         WHERE url_jumia=?""", (jumia_price, url))

        elif "konga.com" in url:
            konga_price = wb.konga(url)
            print(konga_price)
            c.execute("""UPDATE products_product
                         SET price_konga = ?
                         WHERE url_konga=?""", (konga_price, url))

        elif "kara.com" in url:
            # kara_price = wb.kara(url)
            # print(kara_price)
            c.execute("""UPDATE products_product
                         SET price_kara=?
                         WHERE url_kara=?""", (konga_price, url))

        else:
            print("FLAG: Is the following url correct? {}".format(url))

conn.commit()
c.close()
conn.close()
