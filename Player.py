import db_wrapper

def addPlayer(player_name):
    name = player_name
    insertPlayer = "INSERT INTO players (name) VALUES (%s)"
    cursor.execute(insertPlayer, (name,))
    conn.commit()
    pID = getPlayerID(player_name)
    addToScoreboard(pID)

def getPlayerID(player_name):
    query = "SELECT id FROM players WHERE name = %s"
    cursor.execute(query, (player_name,))
    pID = cursor.fetchone()[0]
    return pID

def getPlayerInfo(player_id):
    query = "SELECT * FROM players WHERE id = %s"
    cursor.execute(query, (player_id,))
    player_info = cursor.fetchone()
    return player_info

def getPlayers():
    query = "SELECT * FROM players"
    cursor.execute(query)
    players = cursor.fetchall()
    return players

def count():
    cursor.execute("SELECT COUNT(*) FROM players")
    result = cursor.fetchone()
    return result[0]
