from random import random,choice
from math import exp
Temp=2.3              # Temperature
n=20                  # Sites per edge for n x n system
n2=n*n                # Precalculate n*n
nlist=list(range(n))  # List of sites 
ntrials=200000        # Number Trials 
nequil=100000         # Equilibration steps

# Initialize sums for averages
## Insert lines from lecture notes here

# Create initial matrix of spins all spin up
spins=[[1 for i in range(n)] for j in range(n)]

# Run simulation
## Insert lines from lecture notes here
    
    #Calculate the change in energy if we flip this spin
    deltaE=2.*(spins[i][j]*\
       (spins[i][(j+1)%n]+spins[i][(j-1+n)%n]+\
         spins[(i+1)%n][j]+spins[(i+-1+n)%n][j]))

    #Flip the spin using Metropolis MC
    ## Insert lines from lecture notes here

    # Calculate system energy ONCE 
    ## Insert line from lecture notes here
        energy=0.0  
        for i in range(n):
            for j in range(n):
                energy-=(spins[i][j]*
                         (spins[i][(j+1)%n]+spins[i][(j-1+n)%n]+\
                          spins[(i+1)%n][j]+spins[(i+-1+n)%n][j]))
        ## Insert line from lecture notes here

    # Update energy based on deltaE per spin
    ## Insert lines from lecture notes here

## Insert lines from lecture notes here

print('%8.4f %10.6f %10.6f'%(Temp, E_ave, Cv))
