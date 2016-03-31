import db_wrapper
import Player

def addScores(player_id, point):
    query = """"UPDATE scores
                SET score = score + %s,
                    matches = matches + 1
                WHERE id = %s"""
    cursor.execute(query, (point,player_id,))
    conn.commit()

def resetScores():
    query = "UPDATE scores SET matches = 0, score = 0"
    cursor.execute(query)
    conn.commit()

def addToBoard(player_id):
    player = getPlayerInfo(player_id)
    query = "INSERT INTO scores VALUES (%s, %s, 0, 0)"
    cursor.execute(query, (player[0], player[1],))
    conn.commit()
