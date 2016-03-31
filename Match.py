import db_wrapper
from db_wrapper import conn, cursor

"""Match.py: model that handles DB queries for matches"""

__author__ = "Archimedes Valencia II"
__version__ = "1.1.3"
__email__ = "arvalencia@gbox.adnu.edu.ph"
__status__ = "Production"


def add(player_id1, player_id2, draw='FALSE'):
    """ Adds a match to the database
        Args:
            player_id1 = id of player to be added to the match
            player_id2 = id of player to be added to the match
            draw = boolean value if draw; default is FALSE
    """
    query = "INSERT INTO matches(winner, loser,isDraw)\
                    VALUES(%s,%s,%s)"
    cursor.execute(query, (player_id1, player_id2, draw, ))
    conn.commit()


def existsFor(player1, player2):
    query = """SELECT winner, loser
             FROM matches
             WHERE ((winner = %s AND loser = %s)
             OR (winner = %s AND loser = %s))"""
    cursor.execute(query, (player1, player2, player2, player1,))
    matches = cursor.rowcount
    if matches > 0:
        return False
    return True
