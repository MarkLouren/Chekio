import re
def checkio(data):
 pas=str(data)
 lens=len(data)
 if 10<=len(pas)<=64 and re.match("[a-zA-Z0-9]+",pas) and pas.isalnum():
   if  pas.isupper() or pas.islower():
    return False
   else:
    if pas.isdigit() or pas.isalpha():
     return False
    else: 
       return True
 else: 
  return False
