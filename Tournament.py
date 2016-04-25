from db_wrapper import *

"""Tournament.py: model that handles DB queries for tournaments"""

__author__ = "Archimedes Valencia II"
__version__ = "1.1.3"
__email__ = "arvalencia@gbox.adnu.edu.ph"
__status__ = "Production"


def getStandings(tournament_id):
    query = """SELECT s.player, p.name, s.score, s.matches, s.bye,
                    (SELECT SUM(s2.score)
                     FROM scoreboard AS s2
                     WHERE s2.player IN (SELECT loser
                                     FROM matches
                                     WHERE winner = s.player
                                     AND tournament = %s)
                     OR s2.player IN (SELECT winner
                                 FROM matches
                                 WHERE loser = s.player
                                 AND tournament = %s)) AS owm
                 FROM scoreboard AS s
                 INNER JOIN players AS p on p.id = s.player
                 WHERE tournament = %s
                 ORDER BY s.score DESC, owm DESC, s.matches DESC"""
    cursor.execute(query, (tournament_id, tournament_id, tournament_id,))
    ranks = []
    for row in cursor.fetchall():
        ranks.append(row)
    return ranks


def deleteAll():
    deleteRow("tournaments")


def create(name):
    query = "INSERT INTO tournaments (name) VALUES (%s) RETURNING id"
    cursor.execute(query, (name,))
    tournament_id = cursor.fetchone()[0]
    conn.commit()
    return tournament_id
