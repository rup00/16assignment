def swap_tuple(tup1, tup2): 
    tup1 = tup1 + tup2 
    tup2 = tup1[:len(tup1)-len(tup2)] 
    tup1 = tup1[len(tup1)-len(tup2):] 
      
    return tup1, tup2 
tup1 = (1, 2, 3) 
tup2 = (4, 5, 6) 
      
print(swap_tuple(tup1, tup2))