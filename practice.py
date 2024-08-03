prices = [7,1,5,3,6,4]

def maxProfit(prices):
    open = 0
    close = 0
    diff = 0
    for i in range(len(prices)-1):
        diff = prices[i+1] - prices[i]
        if diff > 0 and 
            
            open = prices[i]
            close = prices[i+1]
        else:
            continue 

#méo

maxProfit(prices)
