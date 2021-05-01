# to compute modular power 
  
# (x^y)%p in O(log y)  

def power(x, y, p) : 
    res = 1     # Initialize result 
  
    x = x % p  
  
    while (y > 0) : 
          
        if ((y & 1) == 1) : 
            res = (res * x) % p 
  
        # y must be even now 
        y = y >> 1      # y = y/2 
        x = (x * x) % p 
          
    return res 
