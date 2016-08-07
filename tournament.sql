DROP DATABASE IF EXISTS tournamentdb;

CREATE DATABASE tournamentdb;

\c tournamentdb;

CREATE TABLE matches (
	id SERIAL PRIMARY KEY,
	tournament integer,
	winner integer,
	loser integer,
	isDraw boolean
);


CREATE TABLE players (
	id SERIAL PRIMARY KEY,
	name varchar
);

CREATE TABLE scoreboard (
	id SERIAL PRIMARY KEY,
	player integer,
	score integer,
	matches integer,
	tournament integer,
	bye integer
);

CREATE TABLE tournaments(
	id SERIAL PRIMARY KEY,
	name varchar
);