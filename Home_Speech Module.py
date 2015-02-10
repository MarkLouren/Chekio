def checkio(number):
 digit=int(number)
 num2words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', \
            19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', \
            50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', \
            90: 'ninety', 0: ''}
 if digit in num2words:
  return (num2words[digit])
 else:
  if 20<digit<=99:
   return (num2words[digit-digit%10]+" "+num2words[digit%10])
  elif 100<=digit<1000:
   mid="hundred"
   p=digit%100
   if p==0:
    return (num2words[digit//100]+" "+mid)
   elif p in num2words:
    return (num2words[digit//100]+" "+mid+" "+num2words[p])
   else:
    return (num2words[digit//100]+" "+mid+" "+num2words[p-p%10]+" "+num2words[p%10])
