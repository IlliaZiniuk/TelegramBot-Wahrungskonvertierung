from aiogram.enums.parse_mode import ParseMode
from aiogram.client.bot import DefaultBotProperties

TOKEN = ""
BOT_PROPERTIES = DefaultBotProperties(parse_mode=ParseMode.HTML)

NBK_API = "https://nationalbank.kz/rss/rates_all.xml"
BINANCE_API: str = "https://api.binance.com/api/v3/ticker/price"