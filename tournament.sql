DROP DATABASE IF EXISTS tournamentdb;

CREATE DATABASE tournamentdb;

\c tournamentdb;

CREATE TABLE tournaments(
	id SERIAL PRIMARY KEY,
	name varchar
);

CREATE TABLE players (
	id SERIAL PRIMARY KEY,
	name varchar
);

CREATE TABLE matches (
	id SERIAL PRIMARY KEY,
	tournament integer REFERENCES tournaments(id),
	winner integer REFERENCES players(id),
	loser integer REFERENCES players(id),
	isDraw boolean
);

CREATE TABLE scoreboard (
	id SERIAL PRIMARY KEY,
	player integer REFERENCES players(id),
	score integer,
	matches integer,
	tournament integer REFERENCES tournaments(id),
	bye integer
);