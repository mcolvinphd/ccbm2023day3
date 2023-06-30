import matplotlib.pyplot as plt
intrst=0.03/12
bal=[1000.]
for month in range(480):
    bal.append(bal[-1]*(1+intrst))
plt.plot(bal)
plt.show()