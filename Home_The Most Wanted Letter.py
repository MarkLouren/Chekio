def checkio(text):
 import collections
 import re
 l=re.sub('[\W\d]', '', text.lower())
 lis=collections.Counter(l).most_common(70)
 l=lis
 l.sort(key=lambda x:(-x[1],x[0]))
 tupl=l[0]
 return tupl[0]
