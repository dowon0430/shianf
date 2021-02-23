import random
import math
money = 50000

stocks = []


#time passing function(first ==> next)
# def time_passing():
# 	def time_pass(prev_stockprice):
# 		def stocks_changing_ratio(ratio):
# 			return float_list[ratio]
# 		#generate 6 randomnumbers between 0.1 and 2
# 		list_size = 6
# 		int_list  = random.sample(range(1,20),list_size)
# 		float_list = [x/10 for x in int_list]
# 		ratio = random.randrange(0,6)
# 		real_next_stockprice = stocks_changing_ratio(ratio) * prev_stockprice
# 		next_stockprice = round(real_next_stockprice)
# 		return next_stockprice
# 	next_stockprice_list = [time_pass(x) for x in first_stockprice_list]
# 	return next_stockprice_list


# class
class Stock:
    def __init__(self, price, name, own):
        self.price = price
        self.name = name
        self.own = own

    def sell(self, quantity):
        global money
        if self.own < quantity:
            return False
        else:
            money += self.price * quantity
            self.own -= quantity
            return True

    def buy(self, quantity):
        global money
        if money < self.price * quantity:
            return False
        else:
            money -= self.price * quantity
            self.own += quantity
            return True
    def timepass(self):
        HowManyStockTypes = 4
        IntRatioList = random.sample(range(3,20),HowManyStockTypes)
        FloatRatioList = [x/10 for x in IntRatioList]
        ratio = random.randrange(0,4)
        real_ratio = FloatRatioList[ratio]
        self.price = math.ceil(self.price * real_ratio)


initialStocks = [
        Stock(500, 'apple', 0),
        Stock(400, 'samsung', 0),
        Stock(100, 'coupang', 1),
        Stock(300, 'kakao', 0)
]

stocks = initialStocks

def printStocks():
    for stock in stocks:
        print(f'Stock Name: {stock.name} Price: {stock.price} Own: {stock.own}')

def printMain():
    global money
    if money <= 1000000000:
        print('-'*50)
        print(f"Welcome to stock market")
        print(f"Money: {money}")
        print(f"Stocks:")
        print(f"(Time will pass if you trade your stocks!)")

        ans = input(f"""Menu:
    (1) show status
    (2) trade stocks
    (3) JONBER(timepass)
    (4) exit
    """)
        if ans == '1':
            printStocks()
            printMain()
        elif ans == '2':
            printTrade()
            printMain()
        elif ans == '3':
            for stock in stocks: 
                stock.timepass()
            printMain()
        elif ans == '4':
            pass
        else:
            print("invalid syntax. please try again.")
            printMain()
    else:
        print("""
        ----------------------------------------------------------------
        
        
        
        
        What the fuck? You're a Billionare?


        VENI VIDI VICI!!!!


        GAME CLEAR
        
        
        
        """)
        pass

def printTrade():
    stock_name = input("stock name you want to trade:")
    buy_or_sell = input("buy/sell? (b/s):")
    quantity = int(input("quantity?:"))

    # does stock name exist?
    # does buy_or_sell equal b or s?
    # is quantity positive integer?
    isQuantityPositiveInteger = quantity > 0
    doesStockNameExist = False
    targetStock = None

    for stock in stocks:
        if stock_name == stock.name:
            doesStockNameExist = True
            targetStock = stock
            break

    doesBuyOrSellEqualBOrS = buy_or_sell in ['b', 's']

    if not isQuantityPositiveInteger:
        print("chisahan guy fuck you")
        printTrade()
    elif not doesStockNameExist:
        print("invalid name! try again")
        printTrade()
    elif not doesBuyOrSellEqualBOrS:
        print("invalid trade opreation! try again!")
        printTrade()
    else:
        if buy_or_sell == 'b':
            did_buy_succeed = targetStock.buy(quantity) 
            if did_buy_succeed:
                print("successfully completed purchase")
                #timepass function
                for stock in stocks: 
                    stock.timepass()
            else:
                print("Not enough money!")
        else:
            did_sell_succeed = targetStock.sell(quantity)
            if did_sell_succeed:
                print("successfully completed sell")
                #timepass fucntion
                for stock in stocks: 
                    stock.timepass()
            else:
                print("Not enough stocks!")


printMain()
