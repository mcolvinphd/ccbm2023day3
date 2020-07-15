import matplotlib.pyplot as plt
alpha=0.00218 #(person-1 day-1)
gamma=0.44    #(day-1)
S=762
I=1
R=0
S_hist=[]
I_hist=[]
R_hist=[]
for day in range(20):
    S_hist.append(S)
    I_hist.append(I)
    R_hist.append(R)
    delta_S=(-alpha*S*I)
    delta_I=alpha*S*I-gamma*I
    delta_R=gamma*I
    S+=delta_S
    I+=delta_I
    R+=delta_R
    # Ensure S,I,R > 0
    S=max(S,0)
    I=max(I,0)
    R=max(R,0)
#Plot S,I,R vs day
plt.plot(S_hist)
plt.plot(I_hist,color='red')
plt.plot(R_hist,color='green')
import matplotlib.pyplot as plt
alpha=0.00218 #(person-1 day-1)
gamma=0.44    #(day-1)
S=762
I=1
R=0
S_hist=[]
I_hist=[]
R_hist=[]
for day in range(20):
    S_hist.append(S)
    I_hist.append(I)
    R_hist.append(R)
    delta_S=(-alpha*S*I)
    delta_I=alpha*S*I-gamma*I
    delta_R=gamma*I
    S+=delta_S
    I+=delta_I
    R+=delta_R
    # Ensure S,I,R > 0
    S=max(S,0)
    I=max(I,0)
    R=max(R,0)
#Plot S,I,R vs day
plt.plot(S_hist)
plt.plot(I_hist,color='red')
plt.plot(R_hist,color='green')
import matplotlib.pyplot as plt
alpha=0.00218 #(person-1 day-1)
gamma=0.44    #(day-1)
S=762
I=1
R=0
S_hist=[]
I_hist=[]
R_hist=[]
for day in range(20):
    S_hist.append(S)
    I_hist.append(I)
    R_hist.append(R)
    delta_S=(-alpha*S*I)
    delta_I=alpha*S*I-gamma*I
    delta_R=gamma*I
    S+=delta_S
    I+=delta_I
    R+=delta_R
    # Ensure S,I,R > 0
    S=max(S,0)
    I=max(I,0)
    R=max(R,0)
#Plot S, I, and R
