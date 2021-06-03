PRODUCTION = [
  {"CODE" : "S"},
  {"VDECL CODE" : "CODE"},
  {"FDECL CODE" : "CODE"},
  {"CDECL CODE" : "CODE"},
  {"" : "CODE"},
  {"vtype id semi" : "VDECL"},
  {"vtype ASSIGN semi" : "VDECL"},
  {"id assign RHS" : "ASSIGN"},
  {"EXPR" : "RHS"},
  {"literal" : "RHS"},
  {"character" : "RHS"},
  {"boolstr" : "RHS"},
  {"T addsub EXPR" : "EXPR"},
  {"T" : "EXPR"},
  {"F multdiv T" : "T"},
  {"F" : "T"},
  {"lparen EXPR rparen" : "F"},
  {"id" : "F"},
  {"num" : "F"},
  {"vtype id laparen ARG rparen lbrace BLOCK RETURN rbrace" : "FDECL"},
  {"vtype id MOREARGS" : "ARG"},
  {"" : "ARG"},
  {"comma vtype id MOREARGS" : "MOREARGS"},
  {"" : "MOREARGS"},
  {"STMT BLOCK" : "BLOCK"},
  {"" : "BLOCK"},
  {"VDECL" : "STMT"},
  {"ASSIGN semi" : "STMT"},
  {"if lparen COND rparen lbrace BLOCK rbrace ELSE" : "STMT"},
  {"while lparen COND rparen lbrace BLOCK rbrace" : "STMT"},
  {"B comp COND" : "COND"},
  {"B" : "COND"},
  {"boolstr" : "B"},
  {"else lbrace BLOCK rbrace" : "ELSE"},
  {"" : "ELSE"},
  {"return RHS semi" : "RETURN"},
  {"class id lbrace ODECL rbrace" : "CDECL"},
  {"VDECL ODECL" : "ODECL"},
  {"FDECL ODECL" : "ODECL"},
  {"" : "ODECL"}
]