import matplotlib.pyplot as plt
K=1
pop=.1
pops=[]
r=2.7
for i in range(100):
	pops.append(pop)
	deltap=r*pop*(1-pop/K)
	pop+=deltap
plt.plot(pops)
plt.ylabel("Population")
plt.xlabel("Time")
plt.show()
