import os
import logging
from time import sleep
import ta.trend
from bot.OKX import Okx

logger = logging.getLogger('varich-yt')

class Bot(Okx):
    def __init__(self):
        super(Bot, self).__init__()

        self.timeout = int(os.getenv('TIMEOUT', 60))
        self.timeframe = os.getenv('TIMEFRAME', '1m')
        self.sma_fast = int(os.getenv('SMA_FAST', '14'))
        self.sma_slow = int(os.getenv('SMA_SLOW', '28'))

    def is_cross(self) -> int:
        """
        0: no intersections
        1: fast line crosses the slow one
        -1: slow line crosses the fast one 
        """
        close = self.close_prices(self.symbol, self.timeframe)

        fast = ta.trend.sma_indicator(close, self.sma_fast).values
        slow = ta.trend.sma_indicator(close, self.sma_slow).values
        
        r = 0
        if fast[-1] > slow [-1] and fast[-2] < slow[-2]: r = 1
        elif fast[-1] < slow[-1] and fast[-2] > slow[-2]: r = -1

        return r
    
    def check(self) -> None:
        try: 
            cross = self.is_cross()

            if cross > 0:
                self.place_order('buy')
            elif cross < 0: 
                self.place_order('sell')

        except Exception as e:
            logger.error(str(e))

    def loop(self) -> None:
        while True:
            self.check()
            sleep(self.timeout)

    def run(self) -> None:
        logger.info("The bot is started!")
        self.check_permissions()
        self.loop()
