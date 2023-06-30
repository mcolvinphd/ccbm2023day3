import matplotlib.pyplot as plt
intrst=0.06/12
payment=2500
bal=[300000.] #Initial balance
for month in range(1000):
    bal.append(bal[-1]*(1+intrst)-payment)
    if bal[-1]<=0: break
plt.plot(bal)
title="Initial Balance=%8.2f Total paid=%8.2f Months=%3d"%(bal[0],month*payment,month)
plt.xlabel("Months")
plt.ylabel("Balance")
plt.title(title)
plt.show()