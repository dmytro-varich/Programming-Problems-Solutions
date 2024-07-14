import logging 
import os

import pandas as pd
from okx.Account import AccountAPI
from okx.MarketData import MarketAPI
from okx.Trade import TradeAPI

logger = logging.getLogger('varich-yt')

class Okx:
    def __init__(self):
        logger.info(f"{os.getenv('NAME', 'Anon')} OKX Auth loaded")

        self.position_id = 'Varich'
        self.symbol = os.getenv('SYMBOL')
        self.qty = float(os.getenv("QTY"))

        self.params = dict(
            domain="https://www.okx.com", 
            flag=os.getenv("IS_DEMO", '1'),
            api_key=os.getenv('API_KEY', '1'),
            api_secret_key=os.getenv("SECRET", '1'),
            passphrase=os.getenv('PASSPHRASE', '1'), 
            debug=False
        )
    
    def check_permissions(self) -> None:
        account = AccountAPI(**self.params).get_account_balance()

    def close_prices(self, instId, timeframe='1m', limit=100) -> pd.Series:
        klines = MarketAPI(**self.params).get_candlesticks(instId, limit=limit, bar=timeframe).get('data', []) 
        klines.reverse()
        return pd.Series([float(e[4]) for e in klines])

    def place_order(self, side) -> TradeAPI:
        trade_api = TradeAPI(**self.params).place_order(
            instId=self.symbol, 
            tdMode='cash', 
            side=side, 
            ordType='market', 
            sz=self.qty, 
            tgtCcy='base_ccy', 
            clOrdId=self.position_id
        )
        order_id = None
        if trade_api.get('code') == '0':
            order_id = trade_api.get('data', [])[0].get('ordId')
            logger.info(f"{side} {order_id}")
        else: logger.error(trade_api)

        return trade_api

    def is_position(self) -> bool:
        orders = TradeAPI(**self.params).get_orders_history(
            instType='SPOT',
            instId=self.symbol,
            ordType="market",
            state='filled'
        ).get('data', [])

        for o in orders:
            if o.get('clOrdId') != self.position_id: continue
            logger.debug(f"Order_id:{o.get('ordId')} {o.get('side')}")
            return o.get('side') == 'buy'
        
        return False