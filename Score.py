import db_wrapper
import Player
from db_wrapper import *

"""Score.py: model that handles DB queries for scores"""

__author__ = "Archimedes Valencia II"
__version__ = "1.1.3"
__email__ = "arvalencia@gbox.adnu.edu.ph"
__status__ = "Production"


def add(tournament, player_id, point):
    """ Add scores to the database
        Args:
            tournament = id of the tournament where the scoreboard
                                    updates to
            player_id = id of player to add the score to
            point = score to add to the player
    """

    query = """UPDATE scoreboard
                SET score = score + %s,
                    matches = matches + 1
                WHERE player = %s AND tournament = %s"""
    cursor.execute(query, (point, player_id, tournament,))
    conn.commit()


def reset():
    """ Resets the scores table """

    query = "UPDATE scoreboard SET matches = 0, score = 0"
    cursor.execute(query)
    conn.commit()


def add_to_board(player_id, tournament_id):
    """ Adds a player to the scoreboard
        Args:
            player_id = id of player to be added
            tournament_id = id of the tournament where the player will play
    """

    query = """INSERT INTO scoreboard (tournament, player, score, matches, bye)
                                VALUES (%s, %s, %s, %s, %s)"""
    cursor.execute(query, (tournament_id, player_id, 0, 0, 0,))
    conn.commit()


def deleteAll():
    """ Deletes all the scoreboard records """

    deleteRow("scoreboard")
