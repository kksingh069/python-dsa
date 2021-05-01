"""
	This simple code is to check if a given number is a poer of two or not.
		ex: 4 --> 2^2 --> 100 --> k = 2
		
			

	NOTE:
"""		
		

def pow_of_two(n):
  return(n and (not(n&(n-1))))

for i in range(20):
  if pow_of_two(i):
    print(f"{i} is a power of 2.")
  else:
    print(f"{i} is NOT a power of 2.")
