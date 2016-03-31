#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

from db_wrapper import *
import Player
import Score
import Match



def deleteMatches():
    """Remove all the match records from the database."""
    deleteRow("matches")
    resetScores()


def deletePlayers():
    """Remove all the player records from the database."""
    deleteRow("players")
    deleteRow("scores")


def countPlayers():
    """Returns the number of players currently registered."""
    return Count("players")


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    addPlayer(name)


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

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
        
    addMatch(winner, loser)
    addScores(winner, wPoint)
    addScores(loser, lPoint)
 
 
def swissPairings():      
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    ranks = playerStandings()
    pairs = []

    numPlayers = Count("players")
    #if numPlayers % 2 != 0:
        #bye = ranks.pop(checkByes(tid, ranks, -1))
        #reportBye(tid, bye[0])

    while len(ranks) > 1:
        validMatch = checkPairs(ranks,0,1)
        player1 = ranks.pop(0)
        player2 = ranks.pop(validMatch - 1)
        pairs.append((player1[0],player1[1],player2[0],player2[1]))

    return pairs

def pairIsValid(player1, player2):
    """Checks if two players have already played against each other
    Args:
        player1: the id number of first player to check
        player2: the id number of potentail paired player
    Return true if valid pair, false if not
    """
    matches = getExistingMatchesCount(player1, player2)
    if matches > 0:
        return False
    return True

def checkPairs(ranks, id1, id2):
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
    if id2 >= len(ranks):
        return id1 + 1
    elif pairIsValid(ranks[id1][0], ranks[id2][0]):
        return id2
    else:
        return checkPairs(ranks, id1, (id2 + 1))


print(swissPairings())
