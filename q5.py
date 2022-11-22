def check(tup): 
      
    l = len(tup) 
  
    for i in range(1, l): 
        if tup[i] != tup[i - 1]: 
            return False
    return True
tup = ('i', 'n', 'e', 'u', 'r', 'o', 'n') 
ans = check(tup) 
  
if ans: 
    print("Yes, all the elements are same") 
else: 
    print("No, all the elements are not same")