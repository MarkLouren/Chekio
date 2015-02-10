def count_words(text, words):
 count=0
 for i in words:
    if text.lower().find(i)!= -1:
        count+=1
 return (count)
