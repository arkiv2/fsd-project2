import psycopg2


conn = psycopg2.connect(dbname="tournamentdb",
                        user="postgres")
cursor = conn.cursor()


def disConnect():
    conn.close()


def deleteRow(table_name):
    cursor.execute("DELETE FROM {}".format(table_name,))
    conn.commit()
