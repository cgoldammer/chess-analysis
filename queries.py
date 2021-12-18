q_rating = """
SELECT 
  db_name
, rating_own
, rating_opponent
, eval as ev
, (result=1) :: Int as win
, (result=0) :: Int as draw
FROM (
  SELECT 
    game_result as result
  , is_white
  , rating1.rating as rating_own
  , rating2.rating as rating_opponent
  , eval
  , move_number
  , database.name as db_name
  FROM game
  JOIN player_rating as rating1 ON 
        game.player_white_id=rating1.player_id
    AND extract(year from game.date)=rating1.year
    AND extract(month from game.date)=rating1.month
  JOIN player_rating as rating2 ON 
        game.player_black_id=rating2.player_id
    AND extract(year from game.date)=rating2.year
    AND extract(month from game.date)=rating2.month
  JOIN move_eval on game.id=move_eval.game_id
  JOIN database on game.database_id=database.id
  WHERE 
        move_number>=%(move_number_start)s and move_number<=%(move_number_end)s
    AND eval is not null
    AND database.is_public
) values
WHERE is_white
"""

q_games = """SELECT * from game"""
q_db = """SELECT * from database WHERE is_public OR name='kingbase_random'"""
q_players = """SELECT * from player"""
q_tournaments = """SELECT * from tournament"""

q_positions = """
SELECT
  g.id as game_id
, me.move_number, me.is_white
, me.fen, me.eval as eval_played, me.eval_best
, g.game_result as result
, pa.typ, pa.value
FROM move_eval me
JOIN game g on me.game_id = g.id
JOIN position p on me.fen = p.fen
JOIN position_attribute pa on pa.position_id = p.id
WHERE eval_best is not null
LIMIT {limit}
"""
