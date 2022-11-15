from telnetlib import XASCII
try:
  print( XASCII )
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")