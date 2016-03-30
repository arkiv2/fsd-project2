\c postgres
DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

\c tournament;

CREATE TABLE matches (
	match_id SERIAL PRIMARY KEY,
	player_left integer,
	player_right integer,
	player_winner integer
);

INSERT INTO matches ("player_left", "player_right", "player_winner") VALUES(1, 2, 1);
INSERT INTO matches ("player_left", "player_right", "player_winner") VALUES(1, 4, 1);
INSERT INTO matches ("player_left", "player_right", "player_winner") VALUES(1, 3, 3);
INSERT INTO matches ("player_left", "player_right", "player_winner") VALUES(1, 5, 1);
INSERT INTO matches ("player_left", "player_right", "player_winner") VALUES(1, 6, 6);
INSERT INTO matches ("player_left", "player_right", "player_winner") VALUES(1, 7, 1);

CREATE TABLE players (
	player_id SERIAL PRIMARY KEY,
	player_name varchar,
	player_num_wins integer,
	player_played_matches integer
);

INSERT INTO players ("player_name", "player_num_wins", "player_played_matches") VALUES('onin1', 0, 0);
INSERT INTO players ("player_name", "player_num_wins", "player_played_matches") VALUES('onin2', 0, 0);
INSERT INTO players ("player_name", "player_num_wins", "player_played_matches") VALUES('onin3', 0, 0);
INSERT INTO players ("player_name", "player_num_wins", "player_played_matches") VALUES('onin4', 0, 0);
INSERT INTO players ("player_name", "player_num_wins", "player_played_matches") VALUES('onin5', 0, 0);
INSERT INTO players ("player_name", "player_num_wins", "player_played_matches") VALUES('onin6', 0, 0);
INSERT INTO players ("player_name", "player_num_wins", "player_played_matches") VALUES('onin7', 0, 0);