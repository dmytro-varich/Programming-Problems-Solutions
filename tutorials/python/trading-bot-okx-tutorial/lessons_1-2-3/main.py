from okx.PublicData import PublicAPI
from okx.MarketData import MarketAPI
from okx.Account import AccountAPI
from okx.Trade import TradeAPI

domain = "https://www.okx.com"
flag = "1"


pub_api = PublicAPI(flag=flag, domain=domain, debug=False)
instruments = pub_api.get_instruments("SPOT")
print(instruments.get('data'))


market_api = MarketAPI(flag=flag, domain=domain, debug=False)
candlesticks = market_api.get_candlesticks("BTC-USDT")
print(candlesticks)


from config import API_KEY, SECRET, PASSPHRASE
acc_api = AccountAPI(API_KEY, SECRET, PASSPHRASE, flag=flag, domain=domain)
acc_balance = acc_api.get_account_balance()
print(acc_balance)

SYMBOL="BTC-USDT"
QTY = 0.00001

trade_api = TradeAPI(API_KEY, SECRET, PASSPHRASE, flag=flag, domain=domain)
place_order = trade_api.place_order(
    instId=SYMBOL,
    tdMode='cash',
    side='buy', 
    ordType='market', 
    sz=QTY, 
    tgtCcy='base_ccy'
)
print(place_order)

orders_history = trade_api.get_orders_history('SPOT')
current_order = trade_api.get_order(SYMBOL, None)
print(orders_history)


ticker = market_api.get_ticker(SYMBOL)
print(ticker)
print(ticker.get('data')[0].get('last'))
