import psycopg2


conn = psycopg2.connect("dbname=tourney")
cursor = conn.cursor()

def disConnect():
    conn.close()
    
def deleteRow(table_name):
    cursor.execute("DELETE FROM %s" % (table_name,))
    conn.commit()

def getStandings():
    cursor.execute("SELECT * FROM scores ORDER BY score desc")
    result = cursor.fetchall()
    return result






