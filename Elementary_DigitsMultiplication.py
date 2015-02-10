def checkio(number):
 number=str(number)
 b=number.replace('0','')
 lis=[int(char) for char in str(b)]
 k=1
 for i in lis:
    k=k*i
 return(k)
