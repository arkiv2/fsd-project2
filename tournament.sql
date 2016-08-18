\c postgres;

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
	tournament integer REFERENCES tournaments(id) ON DELETE CASCADE
);

-- Pivot table for players and tournaments
-- Registered players in a tournament
CREATE TABLE player_tournament (
	player INTEGER REFERENCES players(id) ON DELETE CASCADE,
	tournament INTEGER REFERENCES tournaments(id) ON DELETE CASCADE,
	PRIMARY KEY (player, tournament)
);

-- To be used in match results
CREATE TYPE game_result AS ENUM ('win', 'loss', 'draw');

-- Holds records for player's game result
CREATE TABLE scoreboard (
	player INTEGER REFERENCES players(id) ON DELETE CASCADE,
	match INTEGER REFERENCES matches(id) ON DELETE CASCADE,
	result game_result
);

-- Count all participants in a tournament
CREATE VIEW players_in_tournament AS
	SELECT tournaments.id as tourID, tournaments.name as tournamentName,
		 count(player_tournament.player) as Participants
	FROM player_tournament, tournaments
	WHERE tournaments.id = player_tournament.tournament
	GROUP BY tournaments.id;

-- Get results of matches played by players in a tournament
CREATE VIEW player_match_result AS
	SELECT player, matches.tournament, scoreboard.match, result
	FROM scoreboard, matches
	WHERE scoreboard.match = matches.id;

-- Show number of wins per player on all tournaments
CREATE VIEW player_wins AS
	SELECT player_tournament.player, player_tournament.tournament, count(result) as Wins
	FROM player_tournament LEFT JOIN player_match_result
		ON player_tournament.player = player_match_result.player
		AND player_tournament.tournament = player_match_result.tournament
		AND result = 'win'
	GROUP BY player_tournament.player, player_tournament.tournament
	ORDER BY player_tournament.tournament, player_tournament.player;

-- Show number of losses per player on all tournaments
CREATE VIEW player_losses AS
	SELECT player_tournament.player, player_tournament.tournament, count(result) as Losses
	FROM player_tournament LEFT JOIN player_match_result
		ON player_tournament.player = player_match_result.player
		AND player_tournament.tournament = player_match_result.tournament
		AND result = 'loss'
	GROUP BY player_tournament.player, player_tournament.tournament
	ORDER BY player_tournament.tournament, player_tournament.player;

-- Show number of draws per player on all tournaments
CREATE VIEW player_draws AS
	SELECT player_tournament.player, player_tournament.tournament, count(result) as Draws
	FROM player_tournament LEFT JOIN player_match_result
		ON player_tournament.player = player_match_result.player
		AND player_tournament.tournament = player_match_result.tournament
		AND result = 'draw'
	GROUP BY player_tournament.player, player_tournament.tournament
	ORDER BY player_tournament.tournament, player_tournament.player;

CREATE VIEW player_standings AS
	SELECT player_wins.player, player_wins.tournament, 
		 player_wins.Wins, player_losses.Losses, player_draws.Draws,
		 player_wins.Wins + player_losses.Losses + player_draws.Draws AS matchesPlayed
	FROM player_wins JOIN player_losses
		ON player_wins.player = player_losses.player AND player_wins.tournament = player_losses.tournament
		JOIN player_draws
			ON player_wins.player = player_draws.player AND player_wins.tournament = player_draws.tournament; 



