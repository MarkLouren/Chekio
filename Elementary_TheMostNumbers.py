def checkio(*args):
    b=sorted(args)
    try:
      x=b[-1]-b[0]
      if x == int(x):
       return (x)
      else:
       return (x.__round__(3))
    except:
       return (0)
      
