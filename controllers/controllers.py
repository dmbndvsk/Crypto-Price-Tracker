import ccxt.async_support as ccxt
from models.models import Session, Currency
from datetime import datetime
import logging
import asyncio

logger = logging.getLogger(__name__)

exchange = ccxt.kucoin(
    {
        "enableRateLimit": True,
    }
)


async def get_crypto_price(currency_symbol):
    market_symbol = f"{currency_symbol}/USDT"

    try:
        ticker = await exchange.fetch_ticker(market_symbol)
        return ticker["bid"]
    except ccxt.NetworkError as e:
        logger.error(f"NetworkError: {e}")
        return None
    except ccxt.ExchangeError as e:
        logger.error(f"ExchangeError: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        return None


def rounded_datetime():
    now = datetime.now()
    return now.replace(microsecond=0)


async def save_price(currency, price):
    if price is not None:
        session = Session()
        new_price = Currency(currency=currency, date_=rounded_datetime(), price=price)
        session.add(new_price)
        try:
            session.commit()
        except Exception as e:
            logger.error(f"Error saving price: {e}")
        finally:
            session.close()
    else:
        logger.warning(f"Received None price for {currency}, not saving to DB.")


async def get_history(page):
    session = Session()
    offset = (page - 1) * 10
    history = (
        session.query(Currency)
        .order_by(Currency.date_.desc())
        .offset(offset)
        .limit(10)
        .all()
    )
    session.close()
    return [
        {"currency": item.currency, "price": item.price, "date": item.date_.isoformat()}
        for item in history
    ]


async def delete_history():
    session = Session()
    session.query(Currency).delete()
    session.commit()
    session.close()
