## Simulation to test Stock buying strategies
from random import gauss, choice
import matplotlib.pyplot as plt
import numpy as np

## Set parameters
trials=10000
initial_balance=100 ## Initial cash balance
duration=100        ## How many days in each trial
sd=0.1              ## Standard deviation of price change (mean=0)
start_trade=10      ## Needs to be large enough to include any past averaging of prices
delist_value=0.01   ## Stock value where company is bankrupt

## Pick strategy:
strategy=1
## Strategy 0: Buy or sell randomly
## Strategy 1: Buy if today's price is lower than yesterday, otherwise sell
## Strategy 2: Buy if today's price is lower than the average of the last window days, otherwise sell
window=5
## Strategy 3: Buy if today's price is delta lower than the average of the last window days
##             sell if delta higher than average, otherwise don't buy or sell
delta=0.05

profit_loss=[]
for trial in range(trials):
    balance=[initial_balance]  ## Bank balance
    stocks=[0]     ## Stock holdings
    buy_fraction=0.75  ## Maximum fraction of balance to spend
    sell_fraction=0.75  ## Maximum fraction of stocks to sell
    price=[1]  ## Stock price

    for day in range(1,duration+1):
        ## Update stock price
        newprice=price[day-1]+gauss(0,sd)
        if newprice<=delist_value:
            #print("Company is bankrupt!")
            break
        price.append(newprice)

        if day>=start_trade:
            ## Are you solvent?
            if stocks[-1]==0 and balance[-1]<=0.0:
                #print("You are bankrupt!")
                break

            ## Do some trades
            ## Strategy 0: Flip coin to decide whether to buy or sell each day
            if strategy==0:
                if choice((0,1))==0:  ## buy
                    stock_buy=int(buy_fraction*balance[-1]//price[-1])
                    ##print("Balance=",balance[-1],"Stocks=",stocks[-1],"Price=",price[-1],"Stock buy=",stock_buy)
                    stocks.append(stocks[-1]+stock_buy)
                    balance.append(balance[-1]-stock_buy*price[-1])
                else: #Sell
                    stock_sell=int(stocks[-1]*sell_fraction)  ## Might be zero
                    ##print("Balance=",balance[-1],"Stocks=",stocks[-1],"Price=",price[-1],"Stock sell",stock_sell)
                    stocks.append(stocks[-1]-stock_sell)
                    balance.append(balance[-1]+stock_sell*price[-1])

            ## Strategy 1: Buy if stock is cheaper than yesterday, sell if more expensive
            if strategy==1:
                if price[-1]<price[-2]:  ## Buy stocks
                    stock_buy=int(buy_fraction*balance[-1]//price[-1])
                    stocks.append(stocks[-1]+stock_buy)
                    balance.append(balance[-1]-stock_buy*price[-1])
                else: ## Sell stocks
                    stock_sell=int(stocks[-1]*sell_fraction)  ## Might be zero
                    stocks.append(stocks[-1]-stock_sell)
                    balance.append(balance[-1]+stock_sell*price[-1])

            ## Strategy 2: Buy if stock is cheaper than running average, sell if more expensive
            if strategy==2:  ## Buy stocks
                average_price=sum(price[(-window-1):-1])/window
                if price[-1]<average_price:
                    stock_buy=int(buy_fraction*balance[-1]//price[-1])
                    stocks.append(stocks[-1]+stock_buy)
                    balance.append(balance[-1]-stock_buy*price[-1])
                else: ## Sell stocks
                    stock_sell=int(stocks[-1]*sell_fraction)
                    stocks.append(stocks[-1]-stock_sell)
                    balance.append(balance[-1]+stock_sell*price[-1])

            ## Strategy 3: Same as strategy 2, but with a minimum price shift, delta
            if strategy==3:  ## Buy stocks
                average_price=sum(price[(-window-1):-1])/window
                if price[-1]<average_price-delta:
                    stock_buy=int(buy_fraction*balance[-1]//price[-1])
                    stocks.append(stocks[-1]+stock_buy)
                    balance.append(balance[-1]-stock_buy*price[-1])
                elif price[-1]>average_price+delta:
                    stock_sell=int(stocks[-1]*sell_fraction)
                    stocks.append(stocks[-1]-stock_sell)
                    balance.append(balance[-1]+stock_sell*price[-1])
                else:
                    stocks.append(stocks[-1])
                    balance.append(balance[-1])

    ## Calculate bottom line
    stock_value=max(0,stocks[-1]*price[-1])
    assets=balance[-1]+stock_value
    profit=assets-balance[0]
    #print("Balance: %6.2f Stock value=%6.2f Assets=%6.2f Profit/loss=%6.2f"%(balance[-1],stock_value,assets,profit))
    profit_loss.append(profit)

plt.hist(profit_loss, range=[-100,+500])
pl=np.array(profit_loss)
median_pl=np.median(pl)
mean_pl=np.mean(pl)
outliers=sum(pl>500)
title="Strategy %d Median profit=%6.2f Mean profit=%6.2f (%d outliers)"%(strategy, median_pl, mean_pl, outliers)
plt.title(title)
plt.xlabel("Final profit/loss (cash and stock value)")
plt.ylabel("Count")
plt.show()

#days=list(range(101))
#plt.plot(days,price)
#plt.scatter(days,price)
#plt.show()