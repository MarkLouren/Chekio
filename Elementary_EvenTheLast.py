def checkio(array):
   try: return(sum(array[::2])*array[-1])
   except: return (0)
   
"""
    You are given an array of integers. You should find the sum of the elements with even indexes (0th, 2nd, 4th...)
    then multiply this summed number and the final element of the array together. Don't forget that the first element 
    has an index of 0.
    For an empty array, the result will always be 0 (zero). 
"""
