def checkio(data):
    mylist=data[:]
    for item in data:
       if (data.count(item)==1):
            mylist.remove(item)
    return  mylist
