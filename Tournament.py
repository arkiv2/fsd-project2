from psycopg2 import cursor, conn

"""Tournament.py: model that handles DB queries for tournaments"""

__author__ = "Archimedes Valencia II"
__version__ = "1.1.3"
__email__ = "arvalencia@gbox.adnu.edu.ph"
__status__ = "Production

def getStandings():
    cursor.execute("SELECT * FROM scores ORDER BY score desc")
    result = cursor.fetchall()
    return result
