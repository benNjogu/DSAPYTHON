n = 3
for i in range(0, n): # executes n times
    for j in range(0, n): # executes n times
        print('i value %d and j value %d' %(i, j)) # constant time c

# Total time = c * n * n = c(n2) = o(n2)