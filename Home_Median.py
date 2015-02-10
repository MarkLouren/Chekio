def checkio(data):
  value=sorted(data)
  b= int(len(value)/2)
  if len(value)%2==0:
   med=float((value[b]+value[b-1])/2)
   return med
  else:
   med=float(value[b])
   return med
