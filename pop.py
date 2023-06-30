import matplotlib.pyplot as plt
pop=100
pops=[]
r=0.05
for i in range(150):
	pops.append(pop)
	deltap=r*pop
	pop+=deltap
plt.plot(pops)
plt.ylabel("Population")
plt.xlabel("Time")
plt.show()
