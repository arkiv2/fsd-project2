from db_wrapper import *
import Score


def addPlayer(player_name, tournament):
    name = player_name
    insertPlayer = "INSERT INTO players (name) VALUES (%s) RETURNING id"
    cursor.execute(insertPlayer, (name,))
    player = cursor.fetchone()[0]
    conn.commit()
    Score.add_to_board(player, tournament)

def addBye(player, tournament):
    query = """UPDATE scoreboard
               SET score = score + 3, bye = bye + 1
               WHERE player = %s AND tournament = %s"""
    cursor.execute(query, (player, tournament,))
    conn.commit()


def hasBye(player, tournament):
    query = """SELECT bye FROM scoreboard
               WHERE player = %s AND tournament = %s"""
    cursor.execute(query, (player, tournament,))
    bye = cursor.fetchone()[0]
    if bye == 0:
        return True
    else:
        return False

def getID(player_name):
    query = "SELECT id FROM players WHERE name = %s"
    cursor.execute(query, (player_name,))
    pID = cursor.fetchone()[0]
    return pID

def getInfo(player_id):
    query = "SELECT * FROM players WHERE id = %s"
    cursor.execute(query, (player_id,))
    player_info = cursor.fetchone()
    return player_info

def getAll():
    query = "SELECT * FROM players"
    cursor.execute(query)
    players = cursor.fetchall()
    return players

def count(tID):
    query = "SELECT COUNT(player) FROM scoreboard WHERE tournament = %s"
    cursor.execute(query, (tID,))
    result = cursor.fetchone()[0]
    return result

def deleteAll():
    deleteRow("players")