import matplotlib.pyplot as plt
intrst=0.098/12
payment=50
bal=[0.] #Initial balance
for month in range(480):
    bal.append(bal[-1]*(1+intrst)+payment)
plt.plot(bal)
title="Init Balance=%8.2f Final balance=%8.2f"%(bal[0],bal[-1])
plt.xlabel("Months")
plt.ylabel("Balance")
plt.title(title)
plt.show()