#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

from db_wrapper import *
import Player
import Score
import Match
import Tournament

"""tournament.py: main module that handles all the tournament logic"""

__author__ = "Archimedes Valencia II"
__version__ = "1.1.3"
__email__ = "arvalencia@gbox.adnu.edu.ph"
__status__ = "Production"


def deleteMatches():
    """Remove all match records from the database."""

    Match.deleteAll()
    Score.reset()


def deleteTournaments():
    """Remove all match records from the database."""

    Tournament.deleteAll()


def deletePlayers():
    """Remove all player records from the database."""

    Player.deleteAll()
    Score.deleteAll()


def deleteScoreboard():
    """Removes all score records from the database."""

    Score.deleteAll()


def createTournament(name):

    return Tournament.create(name)



def countPlayers(tID):
    """Returns the number of players currently registered."""

    return Player.count(tID)


def registerPlayer(name, tournament_id):
    """Adds a player to the tournament database.
       Args:
        name: the player's full name (need not be unique).
        tournament: tournament id where player is to be added to
    """


    Player.addPlayer(name, tournament_id)


def playerStandings(tournament_id):
    """Returns a list of the players and their win records, sorted by wins.
        Args:
            tournament_id: id of tournament to be queried
        Returns:
          A list of tuples, each of which contains (id, name, wins, matches):
            id: the player's unique id (assigned by the database)
            name: the player's full name (as registered)
            wins: the number of matches the player has won
            matches: the number of matches the player has played
    """

    return Tournament.getStandings(tournament_id)


def reportMatch(tournament, winner, loser, draw='FALSE'):
    """Records the outcome of a single match between two players.
        Args:
          tournament: id of tournament
          winner:  the id number of the player who won
          loser:  the id number of the player who lost
          draw:   boolean value if draw
    """
    if draw == 'TRUE':
        wPoint = 1
        lPoint = 1
    else:
        wPoint = 3
        lPoint = 0

    Match.add(tournament, winner, loser)
    Score.add(tournament, winner, wPoint)
    Score.add(tournament, loser, lPoint)

def reportBye(player, tournament):
    Player.addBye(player, tournament)


def checkByes(tournament, ranks, index):
    if abs(index) > len(ranks):
        return -1
    elif not Player.hasBye(ranks[index][0], tournament):
        return index
    else:
        return checkByes(tournament, ranks, (index - 1))


def swissPairings(tournament):
    """Returns a list of pairs of players for the next round of a match.

        Returns:
          A list of tuples, each of which contains (id1, name1, id2, name2)
            id1: the first player's unique id
            name1: the first player's name
            id2: the second player's unique id
            name2: the second player's name
    """

    ranks = playerStandings(tournament)
    pairs = []

    numPlayers = Player.count(tournament)
    if numPlayers % 2 != 0:
        bye = ranks.pop(checkByes(tournament, ranks, -1))
        reportBye(tournament, bye[0])

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
