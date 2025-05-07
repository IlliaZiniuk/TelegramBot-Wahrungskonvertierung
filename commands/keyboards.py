from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Konvertierung"), KeyboardButton(text="")],
],
 #    Währungsliste
 resize_keyboard=True,
 input_field_placeholder="Wie geht's dir?")

regions = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🌍 Europa", callback_data="europa"),
         InlineKeyboardButton(text="🌎 Amerika", callback_data="amerika"),
         InlineKeyboardButton(text="🌏 Asien", callback_data="asia")],
         [InlineKeyboardButton(text="🌍 Afrika und Naher Osten", callback_data="afrika"),
         InlineKeyboardButton(text="🌊 Ozeanien", callback_data="oceania")],
         [InlineKeyboardButton(text="💱 Beliebte Währungen", callback_data="popular_currency"),
          InlineKeyboardButton(text="📉 Kryptowährungen", callback_data="crypto_list")]
    ])

back_regions = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Zurück", callback_data="back_reg")]])

def popular_values():
    buttons = [
        [InlineKeyboardButton(text='🇺🇸USD', callback_data="add_popular_value_USD"),
         InlineKeyboardButton(text='🇪🇺EUR', callback_data="add_popular_value_EUR"),
         InlineKeyboardButton(text='🇷🇺RUB', callback_data="add_popular_value_RUB"),
         InlineKeyboardButton(text='🇦🇪AED', callback_data="add_popular_value_AED")],
        [InlineKeyboardButton(text='🇧🇾BYN', callback_data="add_popular_value_BYN"),
         InlineKeyboardButton(text='🇺🇦UAH', callback_data="add_popular_value_UAH"),
         InlineKeyboardButton(text='🇰🇿KZT', callback_data="add_popular_value_KZT"),
         InlineKeyboardButton(text='🇬🇪GEL', callback_data="add_popular_value_GEL")],
        [InlineKeyboardButton(text='🇨🇳CNY', callback_data="add_popular_value_CNY"),
         InlineKeyboardButton(text='🇯🇵JPY', callback_data="add_popular_value_JPY"),
         InlineKeyboardButton(text='🇹🇷TRY', callback_data="add_popular_value_TRY"),
         InlineKeyboardButton(text='🇬🇧GBP', callback_data="add_popular_value_GBP")],
        [InlineKeyboardButton(text='₿BTC', callback_data="add_popular_value_BTC"),
         InlineKeyboardButton(text='ΞETH', callback_data="add_popular_value_ETH"),
         InlineKeyboardButton(text='SOL', callback_data="add_popular_value_SOL"),
         InlineKeyboardButton(text='TON', callback_data="add_popular_value_TON")],
        [InlineKeyboardButton(text="", callback_data="clbk_otherlist_value")]
    ]
    # Andere Währungen
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def full_list():
    buttons = [
        [InlineKeyboardButton(text="🇦🇺 AUD - Dollar", callback_data="add_fulllist_value_AUD"),
         InlineKeyboardButton(text="🇦🇿 AZN - Manat", callback_data="add_fulllist_value_AZN")],
        [InlineKeyboardButton(text="🇧🇷 BRL - Real", callback_data="add_fulllist_value_BRL"),
         InlineKeyboardButton(text="🇧🇾 BYN - Rubel", callback_data="add_fulllist_value_BYN")],
        [InlineKeyboardButton(text="🇨🇦 CAD - Dollar", callback_data="add_fulllist_value_CAD"),
         InlineKeyboardButton(text="🇨🇭 CHF - Franken", callback_data="add_fulllist_value_CHF")],
        [InlineKeyboardButton(text="🇨🇳 CNY - Yuan", callback_data="add_fulllist_value_CNY"),
         InlineKeyboardButton(text="🇨🇿 CZK - Krone", callback_data="add_fulllist_value_CZK")],
        [InlineKeyboardButton(text="🇩🇰 DKK - Krone", callback_data="add_fulllist_value_DKK"),
         InlineKeyboardButton(text="🇪🇺 EUR - Euro", callback_data="add_fulllist_value_EUR")],
        [InlineKeyboardButton(text="🇬🇧 GBP - Pfund Sterling", callback_data="add_fulllist_value_GBP"),
         InlineKeyboardButton(text="🇬🇪 GEL - Lari", callback_data="add_fulllist_value_GEL")],
        [InlineKeyboardButton(text="🇮🇷 IRR - Rial", callback_data="add_fulllist_value_IRR"),
         InlineKeyboardButton(text="🇮🇳 INR - Rupie", callback_data="add_fulllist_value_INR")],
        [InlineKeyboardButton(text="🇯🇵 JPY - Yen", callback_data="add_fulllist_value_JPY"),
         InlineKeyboardButton(text="🇰🇼 KWD - Dinar", callback_data="add_fulllist_value_KWD")],
        [InlineKeyboardButton(text="🇰🇬 KGS - Som", callback_data="add_fulllist_value_KGS"),
         InlineKeyboardButton(text="🇰🇷 KRW - Won", callback_data="add_fulllist_value_KRW")],
        [InlineKeyboardButton(text="🇲🇾 MYR - Ringgit", callback_data="add_fulllist_value_MYR"),
         InlineKeyboardButton(text="🇲🇩 MDL - Leu", callback_data="add_fulllist_value_MDL")],
        [InlineKeyboardButton(text="🇲🇽 MXN - Peso", callback_data="add_fulllist_value_MXN"),
         InlineKeyboardButton(text="🇳🇴 NOK - Krone", callback_data="add_fulllist_value_NOK")],
        [InlineKeyboardButton(text="🇳🇿 NZD - Dollar", callback_data="add_fulllist_value_NZD"),
         InlineKeyboardButton(text="🇵🇱 PLN - Zloty", callback_data="add_fulllist_value_PLN")],
        [InlineKeyboardButton(text="🇷🇺 RUB - Rubel", callback_data="add_fulllist_value_RUB"),
         InlineKeyboardButton(text="🇸🇦 SAR - Riyal", callback_data="add_fulllist_value_SAR")],
        [InlineKeyboardButton(text="🇸🇬 SGD - Dollar", callback_data="add_fulllist_value_SGD"),
         InlineKeyboardButton(text="🇸🇪 SEK - Krone", callback_data="add_fulllist_value_SEK")],
        [InlineKeyboardButton(text="🇹🇭 THB - Baht", callback_data="add_fulllist_value_THB"),
         InlineKeyboardButton(text="🇹🇯 TJS - Somoni", callback_data="add_fulllist_value_TJS")],
        [InlineKeyboardButton(text="🇹🇷 TRY - Lira", callback_data="add_fulllist_value_TRY"),
         InlineKeyboardButton(text="🇺🇸 USD - Dollar", callback_data="add_fulllist_value_USD")],
        [InlineKeyboardButton(text="🇺🇦 UAH - Griwna", callback_data="add_fulllist_value_UAH"),
         InlineKeyboardButton(text="🇺🇿 UZS - Sum", callback_data="add_fulllist_value_UZS")],
        [InlineKeyboardButton(text="🇿🇦 ZAR - Rand (Südafrika)", callback_data="add_fulllist_value_ZAR")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
