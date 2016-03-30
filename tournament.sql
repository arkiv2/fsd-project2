\c postgres
DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

\c tournament;

CREATE TABLE matches (
	match_id integer PRIMARY KEY,
	player_left integer,
	player_right integer,
	player_winner integer
);

INSERT INTO matches VALUES(1, 1, 2, 1);
INSERT INTO matches VALUES(2, 1, 4, 1);
INSERT INTO matches VALUES(3, 1, 3, 3);
INSERT INTO matches VALUES(4, 1, 5, 1);
INSERT INTO matches VALUES(5, 1, 6, 6);
INSERT INTO matches VALUES(6, 1, 7, 1);

CREATE TABLE players (
	player_id integer PRIMARY KEY,
	player_name string,
	player_num_wins integer,
);

INSERT INTO players VALUES(1, "onin1", 0);
INSERT INTO players VALUES(2, "onin2", 0);
INSERT INTO players VALUES(3, "onin3", 0);
INSERT INTO players VALUES(4, "onin4", 0);
INSERT INTO players VALUES(5, "onin5", 0);
INSERT INTO players VALUES(6, "onin6", 0);
INSERT INTO players VALUES(7, "onin7", 0);