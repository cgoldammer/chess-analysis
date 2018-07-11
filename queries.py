
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
