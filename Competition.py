from db_wrapper import *

"""Competition.py: model that handles DB queries for tournaments"""

__author__ = "Archimedes Valencia II"
__version__ = "1.1.3"
__email__ = "arvalencia@gbox.adnu.edu.ph"
__status__ = "Production"


def getStandings(tournament_id):
    """
        Get the current ranking of players in a tournament
        Args:
            tournament_id = id of the tournament to check ranks
        Returns:
            ranks = a list of tuples of players ranked by the system
    """

    query = """
            SELECT S.player, P.name, S.score, S.matches, S.bye, (
                SELECT SUM(scBoard.score)
                FROM scoreboard AS scBoard
                WHERE scBoard.player IN (
                    SELECT loser
                    FROM matches
                    WHERE winner = S.player
                    AND tournament = %s)
                OR scBoard.player IN (
                    SELECT winner
                    FROM matches
                    WHERE loser = S.player
                    AND tournament = %s))
                AS subQuery
            FROM scoreboard AS S
            INNER JOIN players AS P on P.id = S.player
            WHERE tournament = %s
            ORDER BY S.score DESC, subQuery DESC, S.matches DESC"""
    cursor.execute(query, (tournament_id, tournament_id, tournament_id,))
    ranks = []
    for row in cursor.fetchall():
        ranks.append(row)
    return ranks


def deleteAll():
    deleteRow("tournaments")


def hasBye(player, tournament):
    """ Checks if a player has a recorded bye
        Args:
            player = id of player to check
            tournament = id of the tournament where the player plays
    """

    query = """SELECT bye FROM scoreboard
               WHERE player = %s AND tournament = %s"""
    cursor.execute(query, (player, tournament,))
    bye = cursor.fetchone()[0]
    if bye == 0:
        return True
    else:
        return False


def create(name):
    """
        Creates a tournament
        Args:
            name = name of the tournament to be created
        Returns:
            tournament_id = id of the newly created tournament
    """

    query = "INSERT INTO tournaments (name) VALUES (%s) RETURNING id"
    cursor.execute(query, (name,))
    tournament_id = cursor.fetchone()[0]
    conn.commit()
    return tournament_id
