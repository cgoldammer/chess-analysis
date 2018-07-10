
q_rating = """
SELECT 
  rating_own
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
  WHERE 
            move_number>=10 and move_number<=40
        AND game.database_id=19
        AND eval is not null
        
) values
WHERE is_white
"""
