"""
	This simple code is to check if a given number is a poer of two or not.
		ex: 4 --> 2^2 --> 100 --> k = 2
		
			
	Conclusion:

	NOTE:
		- BUT If n = 0, the result will be zero indicating that 0 is a power of 2, wich is not true.
"""		
		

def pow_of_two(n):
  return(n and (not(n&(n-1))))

for i in range(20):
  if pow_of_two(i):
    print(f"{i} is a power of 2.")
  else:
    print(f"{i} is NOT a power of 2.")
