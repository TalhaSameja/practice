def buyAndSellStock (stock):
    buy = 0
    max_profit = 0
    for sell in range(1,len(stock)):
        if stock[sell] < stock[buy]:
            buy = sell
        else:
            profit = stock[sell]-stock[buy]
            if profit > max_profit:
                max_profit = profit
        sell += 1
    return max_profit
stock = [10,1,1,5,0,6,7,1]
print(buyAndSellStock(stock))