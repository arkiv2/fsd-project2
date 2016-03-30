import psycopg2


conn = psycopg2.connect("dbname=tournament")
cursor = conn.cursor()

def disConnect():
    conn.close()
    
def showTable(table_name):
    cursor.execute("SELECT * FROM %s" % (table_name,))
    return cursor.fetchall()

def deleteRow(table_name):
    cursor.execute("UPDATE players SET player_num_wins = 0, player_played_matches = 0;")
    cursor.execute("DELETE FROM %s" % (table_name,))
    conn.commit()

def Count(table_name):
    cursor.execute("SELECT COUNT(*) FROM %s" % (table_name,))
    result = cursor.fetchone()
    return result[0]

def addPlayer(player_name):
    name = player_name
    cmd = "INSERT INTO players \
                    (player_name, player_num_wins, player_played_matches) \
                    VALUES (%s, 0, 0)"
    cursor.execute(cmd, (name,))
    conn.commit()

def getStandings():
    #cursor.execute("SELECT players.player_id, players.player_name,\
     #               players.player_num_wins,matches.player_left \
      #              FROM players INNER JOIN matches \
       #             ON players .player_id = matches.player_left \
         #           ORDER BY player_num_wins desc;")

    cursor.execute("SELECT * FROM players")
    result = cursor.fetchall()
    return result

def addMatch(player_id1, player_id2):
    update_match = "INSERT INTO matches(player_left, player_right,player_winner)\
                    VALUES(%s,%s,%s)"
    cursor.execute(update_match, (player_id1,player_id2,player_id1,))
    conn.commit()

def addWinner(player_id):
    query = "UPDATE players \
            SET player_played_matches = player_played_matches + 1, \
                player_num_wins = player_num_wins + 1 \
            WHERE player_id = %s"
    cursor.execute(query, (player_id,))
    conn.commit()

def addLoser(player_id):
    query = "UPDATE players \
            SET player_played_matches = player_played_matches + 1 \
            WHERE player_id = %s"
    cursor.execute(query, (player_id,))
    conn.commit()
   
    
                   

#print(getStandings())
#disConnect()


