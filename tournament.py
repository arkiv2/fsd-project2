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
    """Removes all match records from the database."""

    Match.deleteAll()
    Score.reset()


def deleteTournaments():
    """Removes all match records from the database."""

    Tournament.deleteAll()


def deletePlayers():
    """Removes all player records from the database."""

    Player.deleteAll()
    Score.deleteAll()


def deleteScoreboard():
    """Removes all score records from the database."""

    Score.deleteAll()


def createTournament(name):
    """
        Creates a tournament and returns the created tournament id
        Args:
            name: name of new tournament
        Returns:
            id: the tournament id of newly created tournament
    """

    return Tournament.create(name)


def countPlayers(tID):
    """Returns the number of players currently registered in a tournament"""

    return Player.count(tID)


def registerPlayer(name, tournament_id):
    """
        Adds a player to the tournament database.
        Args:
            name =  the player's full name (need not be unique).
            tournament =  tournament id where player is to be added to
    """

    Player.addPlayer(name, tournament_id)


def playerStandings(tournament_id):
    """
        Queries tournament data for current ranking of players
        Args:
            tournament_id =  id of tournament to be queried
        Returns:
          A list of tuples, each of which contains (id, name, wins, matches):
            id = the player's unique id (assigned by the database)
            name =  the player's full name (as registered)
            wins =  the number of matches the player has won
            matches = the number of matches the player has played
    """

    return Tournament.getStandings(tournament_id)


def checkBye(player_id, tournament):
    """
        Checks if a player has bye in a tournament
        Args:
            player_id = id of the player to check
            tournament: id of tournament to be queried
        Returns:
            boolean value; True if player has bye
    """

    return Player.hasBye(player_id, tournament)


def reportMatch(tournament, winner, loser, draw='FALSE'):
    """
        Reports a match's result to the database and assigns
        corresponding points to a player
        Args:
            tournament =  id of tournament where the match took place
            winner = id of the winner
            loser =  id of the loser
            draw =  true if the match is  a draw
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
    """
        Gives a player a bye
        Args:
            player = id of player awarded by a bye
            tournament =  id of tournament where the match took place
    """

    Player.addBye(player, tournament)


def checkByes(tournament, ranks, index):
    """
        Logic to handle tournament checking of byes
        Args:
            tournament =  id of tournament to query
            ranks = a list of tuples of rankings of players  from tournament
                standing
        Returns:
    """

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

    ranks = playerStandings(tournament)  # Queries the database for
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
    """
        Checks if a two players have already played with each other
        Args:
            player1 = id of player finding match
            player2 =  id of player to be cross checked
        Returns:
            boolean value: True if a match already exists
    """

    return Match.existsFor(player1, player2)


def checkPairs(ranks, player, player_opponent):
    """
        Main logic for checking players matches
            If a player is to be matched with another
            player, this checks if a match already exists
            between them. If a match exists, player will
            be recursively matched against other players
            in the tournament
    Args:
        ranks = list of current ranks from swissPairings()
        player = player needing a match
        player_opponent = player to be matched
    Returns:
        id of matched player

    """
    if player_opponent >= len(ranks):
        return player + 1
    elif pairIsValid(ranks[player][0], ranks[player_opponent][0]):
        return player_opponent
    else:
        return checkPairs(ranks, player, (player_opponent + 1))
