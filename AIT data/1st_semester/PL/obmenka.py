import csv 

d = {}

bek = csv.reader(open("valuta.txt", "r"))

for curr,quan,price in bek:
    if curr not in d:
        d[curr] = []
    d[curr].append((int(quan),float(price)))
        
for curr , arr in d.items():
    amount_buy = sum([curr for curr,quan in arr if curr>0])
    amount_sell = sum([curr for curr,quan in arr if curr<0])
    buy_price = sum([curr*price for curr,price in arr if curr>0])
    sell_price = sum([curr*price for curr,price in arr if curr<0])
    avg_buy = buy_price/amount_buy
    avg_sell = sell_price/amount_sell
    print("Average of buy:",avg_buy,"Average of sell:",avg_sell,"Profit:",amount_sell*(avg_buy-avg_sell),"Amount buys:",amount_buy,"Amount sells:",amount_sell)
