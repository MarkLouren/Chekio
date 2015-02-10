def checkio(number):
  new=int(number)
  if new%3==0 and new%5==0:
    return "Fizz Buzz"
  elif new%3==0 and not new%5==0:
    return "Fizz"
  elif new%5==0 and not new%3==0:
    return "Buzz"
  else:
    return str(new)
