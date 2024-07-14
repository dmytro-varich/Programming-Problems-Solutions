import traceback
from bot.Logger import setup_logger
logger = setup_logger()

from okx.exceptions import OkxAPIException
from bot.Bot import Bot
from dotenv import load_dotenv
load_dotenv() 

if __name__ == '__main__':
    try: 
        Bot().run()
    except KeyboardInterrupt as e:
        logger.debug("Bot was stopped!")
    except OkxAPIException as e: 
        logger.debug(str(e))
    except Exception as e:
        logger.error("Ошибка: %s", e)
        logger.error("Traceback: %s", traceback.format_exc())