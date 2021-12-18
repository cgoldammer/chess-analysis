CONNSTRING_PROD = "host=localhost port=5434 user=postgres dbname=chess_prod"
CONNSTRING_DEV = "host=localhost port=5434 user=postgres dbname=chess_dev"

names = {
   0: "number_moves_own"
,  1: "number_moves_opp"
,  2: "number_checks_own"
,  3: "number_checks_opp"
,  4: "number_takes_own"
,  5: "number_takes_opp"
,  6: "number_takes_pawn_own"
,  7: "number_takes_pawn_opp"
,  8: "opp_kings"
,  9: "piece_values_own"
, 10: "piece_values_opp"
, 11: "kings_pawn_own"
, 12: "kings_pawn_opp"
, 13: "king_row_own"
, 14: "king_row_opp"
, 15: "queens_own"
, 16: "queens_opp"
, 17: "rooks_own"
, 18: "rooks_opp"
, 19: "in_check"
}

# data StatType = NumberMovesOwn                                                            
#               | NumberMovesOpp                                                            
#               | NumberChecksOwn                                                           
#               | NumberChecksOpp                                                           
#               | NumberTakesOwn                                                            
#               | NumberTakesOpp                                                            
#               | NumberTakesPawnOwn                                                        
#               | NumberTakesPawnOpp                                                        
#               | OppKings                                                                  
#               | PieceValuesOwn                                                            
#               | PieceValuesOpp                                                            
#               | KingPawnsOwn                                                              
#               | KingPawnsOpp                                                              
#               | KingRowOwn                                                                
#               | KingRowOpp                                                                
#               | QueensOwn                                                                 
#               | QueensOpp                                                                 
#               | RooksOwn                                                                  
#               | RooksOpp deriving (Eq, Enum)

def top_code(x, val):
  x[x > val] = val
  return x

def bottom_code(x, val):
  x[x < val] = val
  return x

def top_and_bottom(x, bottom, top):
  return top_code(bottom_code(x, bottom), top)

