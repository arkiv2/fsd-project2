import db_wrapper
import Player
from db_wrapper import cursor, conn

"""Score.py: model that handles DB queries for scores"""

__author__ = "Archimedes Valencia II"
__version__ = "1.1.3"
__email__ = "arvalencia@gbox.adnu.edu.ph"
__status__ = "Production"


def add(player_id, point):
    """ Add scores to the database
        Args:
            player_id = id of player to add the score
            point = score to add to the player
    """

    query = """UPDATE scores
                SET score = score + %s,
                    matches = matches + 1
                WHERE id = %s"""
    cursor.execute(query, (point, player_id, ))
    conn.commit()


def reset():
    """ Resets the scores table """

    query = "UPDATE scores SET matches = 0, score = 0"
    cursor.execute(query)
    conn.commit()


def addToBoard(player_id):
    """ Add a player to the scoreboard
        Args:
            player_id = id of player to be added
    """
    player = Player.getInfo(player_id)
    query = "INSERT INTO scores VALUES (%s, %s, 0, 0)"
    cursor.execute(query, (player[0], player[1],))
    conn.commit()
