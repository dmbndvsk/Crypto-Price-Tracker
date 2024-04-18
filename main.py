from aiohttp import web
import logging
from controllers.controllers import (
    get_crypto_price,
    save_price,
    get_history,
    delete_history,
)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def get_price(request):
    currency_symbol = request.match_info.get("currency", "USD")
    logger.info(f"Attempting to fetch price for {currency_symbol}")

    price = await get_crypto_price(currency_symbol)
    if price is not None:
        logger.info(f"Price fetched for {currency_symbol}: {price}")
        await save_price(currency_symbol, price)
        logger.info(f"Price for {currency_symbol} successfully saved")
        return web.json_response({"currency": currency_symbol, "price": price})
    else:
        logger.error(f"Failed to fetch price for {currency_symbol}")
        return web.HTTPBadRequest(reason=f"Cannot get price for {currency_symbol}")


async def get_price_history(request):
    page = request.rel_url.query.get("page", 1)
    try:
        page = int(page)
        logger.info(f"Fetching price history for page {page}")
    except ValueError:
        logger.error("Invalid page number provided, must be an integer")
        return web.HTTPBadRequest(reason="Page must be an integer")

    history = await get_history(page)
    if history:
        logger.info("Price history fetched successfully")
    else:
        logger.warning("No history found for the requested page")
    return web.json_response({"history": history})


async def delete_price_history(request):
    logger.info("Attempting to delete all price history")
    await delete_history()
    logger.info("All price history deleted successfully")
    return web.HTTPNoContent()


def create_app():
    app = web.Application()
    app.add_routes(
        [
            web.get("/price/history", get_price_history),
            web.delete("/price/history", delete_price_history),
            web.get("/price/{currency}", get_price),
        ]
    )
    return app


app = create_app()
if __name__ == "__main__":
    logger.info("Starting server on http://127.0.0.1:8080")
    web.run_app(app, host="127.0.0.1", port=8080)
