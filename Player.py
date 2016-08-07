from db_wrapper import *
import Score


def addPlayer(player_name, tournament):
    """ Adds a player to the database and initializes the
        player's scoreboard

        Args:
            player_name = name of player to be added to the database
            tournament = id of tournament where the player will play
    """

    name = player_name
    insertPlayer = "INSERT INTO players (name) VALUES (%s) RETURNING id"
    cursor.execute(insertPlayer, (name,))
    player = cursor.fetchone()[0]
    conn.commit()
    Score.add_to_board(player, tournament)


def addBye(player, tournament):
    """ Adds a bye to a certain player in a tournament
        Args:
            player = id of player to receive the bye
            tournament = id of the tournament where the player plays
    """

    query = """UPDATE scoreboard
               SET score = score + 3, bye = bye + 1
               WHERE player = %s AND tournament = %s"""
    cursor.execute(query, (player, tournament,))
    conn.commit()


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
    if bye == 1:
        return True
    else:
        return False


def count(tID):
    """ Counts the number of players in a given tournament
        Args:
            tID = id of the tournament
        Returns:
            result = integer count of the players
    """

    query = "SELECT COUNT(player) FROM scoreboard WHERE tournament = %s"
    cursor.execute(query, (tID,))
    result = cursor.fetchone()[0]
    return result


def deleteAll():
    """  Deletes all matches from the database """

    deleteRow("players")
