import psycopg2


conn = psycopg2.connect("dbname=tournament")
cursor = conn.cursor()

def disConnect():
    conn.close()
    
def deleteRow(table_name):
    cursor.execute("DELETE FROM %s" % (table_name,))
    conn.commit()

def Count(table_name):
    cursor.execute("SELECT COUNT(*) FROM %s" % (table_name,))
    result = cursor.fetchone()
    return result[0]








def getStandings():
    #cursor.execute("SELECT players.player_id, players.player_name,\
     #               players.player_num_wins,matches.player_left \
      #              FROM players INNER JOIN matches \
       #             ON players .player_id = matches.player_left \
         #           ORDER BY player_num_wins desc;")

    cursor.execute("SELECT * FROM scores ORDER BY score desc")
    result = cursor.fetchall()
    return result






