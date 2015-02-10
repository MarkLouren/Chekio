def checkio(words):
    text=words.split()
    n=0
    for word in text:
      if word.isalpha():
        n=n+1
        if n>2:
           return True
      else:
        n=0
    return False
