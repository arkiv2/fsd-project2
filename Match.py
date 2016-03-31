import db_wrapper

def addMatch(player_id1, player_id2, draw='FALSE'):
    update_match = "INSERT INTO matches(winner, loser,isDraw)\
                    VALUES(%s,%s,%s)"
    cursor.execute(update_match, (player_id1,player_id2,draw,))
    conn.commit()

def getExistingMatchesCount(player1,player2):
    sql = """SELECT winner, loser
             FROM matches
             WHERE ((winner = %s AND loser = %s)
                    OR (winner = %s AND loser = %s))"""
    cursor.execute(sql, (player1, player2, player2, player1,))
    matches = cursor.rowcount
    return matche
