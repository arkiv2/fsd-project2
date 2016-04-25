--\c postgres
--DROP DATABASE IF EXISTS tournament;
--
--CREATE DATABASE tournament;
--
--\c tournament;

CREATE TABLE matches (
	match_id SERIAL PRIMARY KEY,
	winner integer,
	loser integer,
	isDraw boolean
);


CREATE TABLE players (
	id SERIAL PRIMARY KEY,
	name varchar
);

CREATE TABLE scores (
	id SERIAL PRIMARY KEY,
	player_id integer,
	score integer,
	matches integer
);