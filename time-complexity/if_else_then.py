n = 1
if n == 1: # constant time
    print('Wrong value') # constant time
    print(n) # constant time
else:
    for i in range(0, n): # executes n times
        print('Current number: ', i) #constant time

# You select the part that adds up to the most o(n)