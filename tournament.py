#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

from db_wrapper import *
import Player
import Score
import Match

"""tournament.py: main module that handles all the tournament logic"""

__author__ = "Archimedes Valencia II"
__version__ = "1.1.3"
__email__ = "arvalencia@gbox.adnu.edu.ph"
__status__ = "Production"


def deleteMatches():
    """Remove all the match records from the database."""

    deleteRow("matches")
    Score.reset()


def deletePlayers():
    """Remove all the player records from the database."""

    deleteRow("players")
    deleteRow("scores")


def countPlayers():
    """Returns the number of players currently registered."""

    return Player.count()


def registerPlayer(name):
    """Adds a player to the tournament database.
       Args:
        name: the player's full name (need not be unique).
    """

    Player.addPlayer(name)


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
        Returns:
          A list of tuples, each of which contains (id, name, wins, matches):
            id: the player's unique id (assigned by the database)
            name: the player's full name (as registered)
            wins: the number of matches the player has won
            matches: the number of matches the player has played
    """

    return getStandings()


def reportMatch(winner, loser, draw='FALSE'):
    """Records the outcome of a single match between two players.
        Args:
          winner:  the id number of the player who won
          loser:  the id number of the player who lost
          draw:   boolean value if draw
    """
    wPoint = 1
    lPoint = 0

    if draw == 'TRUE':
        wPoint = 1
        lPoint = 1

    Match.add(winner, loser)
    Score.add(winner, wPoint)
    Score.add(loser, lPoint)


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

        Returns:
          A list of tuples, each of which contains (id1, name1, id2, name2)
            id1: the first player's unique id
            name1: the first player's name
            id2: the second player's unique id
            name2: the second player's name
    """

    ranks = playerStandings()
    pairs = []

    numPlayers = Player.count()
    """if numPlayers % 2 != 0:
        bye = ranks.pop(checkByes(tid, ranks, -1))
        reportBye(tid, bye[0]) """

    while len(ranks) > 1:
        validMatch = checkPairs(ranks, 0, 1)
        player1 = ranks.pop(0)
        player2 = ranks.pop(validMatch - 1)
        pairs.append((player1[0], player1[1], player2[0], player2[1]))

    return pairs


def pairIsValid(player1, player2):
    return Match.existsFor(player1, player2)


def checkPairs(ranks, player, player_opponent):
    """Checks if two players have already had a match against each other.
    If they have, recursively checks through the list until a valid match is
    found.
    Args:
        tid: id of tournament
        ranks: list of current ranks from swissPairings()
        id1: player needing a match
        id2: potential matched player
    Returns id of matched player or original match if none are found.
    """
    if player_opponent >= len(ranks):
        return player + 1
    elif pairIsValid(ranks[player][0], ranks[player_opponent][0]):
        return player_opponent
    else:
        return checkPairs(ranks, player, (player_opponent + 1))
