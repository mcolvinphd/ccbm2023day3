import matplotlib.pyplot as plt
K=1000
pop=100
pops=[]
r=0.05
for i in range(150):
	pops.append(pop)
	deltap=r*pop*(1-pop/K)
	pop+=deltap
plt.plot(pops)
plt.ylabel("Population")
plt.xlabel("Time")
plt.show()
