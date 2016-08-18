# FSD-Project3 [![Build Status](https://travis-ci.org/arkiv2/tournament-results.svg?branch=normalized)](https://travis-ci.org/arkiv2/tournament-results)
## Udacity FSD(Full Stack Developer Nanodegree) Course Requirement 
This project is a python application that emulates a swiss-style tournament

### Version
1.1.3

### Requirements
* python 2.7
* pip
* psycopg2
* postgresql-9.5

### Features
##### Supports
* Multiple tournaments
* Odd number of players
* Tournament Byes
* Zero Rematch


### Installation
Clone
```sh
$ git clone https://github.com/arkiv2/fsd-project2.git SwissTournament
$ cd SwissTournament
```
Installing Database Blueprint
```sh
$ sudo -u postgres psql
postgres=# \i tournament.sql
```
    
###### Create a new file and import from tournament.py
Add this line at the top
```sh
from tournament import *
```

## Usage
* ### Creating a tournament
    * Syntax
    ```sh
    tID = createTournament(Name)
    ```
    * Usage
    ```sh
    tID = createTournament("Olympics")
    ```	

* ### Creating a player
    * Syntax
    ```sh
    RegisterPlayer(Name, Tournament_ID)
    ```
    * Usage
    ```sh
    RegisterPlayer("Arki Valencia", tID)
    ```

* ### Applying swiss-style tournament
    * Syntax
    ```sh
    pairings = swissPairings(Tournament_ID)
    ```
    * Usage
    ```sh
    pairings = swissPairings(tID)
    ```

* ### Reporting match results
    * Syntax
    ```sh
    reportMatch(Tournament_ID, Winner, Loser, isDraw = False)
    ```
    * Usage
    ```sh
    reportMatch(tID, 1, 2)          // Player_ID 1 is the winner
    reportMatch(tID, 1, 2, True)    // Match is a draw
    ```

* ### Get Player Standings
    * Syntax
    ```sh
    standings = playerStandings(Tournament_ID)
    ```
    * Usage
    ```sh
    standings = playerStandings(tID)
    ```

* ### Reporting a bye
    * Syntax
    ```sh
    reportBye(Player_ID, Tournament_ID)
    ```
    * Usage
    ```sh
    reportBye(pID, tID)
    ```
        
* ### Deleting Records
    * Usage
    ```sh
    deleteMatches()
    deletePlayers()
    deleteTournaments()
    deleteScoreboard()
    ```

### Using the test cases
```sh
chmod +x extra_credit_test.py
./extra_credit_test.py
```
or
```sh
python extra_credit_test.py
```

### Plugins
* psycopg2 - the most popular PostgreSQL adapter for the Python programming language


**Credits**

   [BenBrandt]: <Test Suite and some tournament logics>
