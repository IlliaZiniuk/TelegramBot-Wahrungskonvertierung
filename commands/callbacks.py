from aiogram.types import CallbackQuery
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from commands.json_XML import get_exchange_rates
from commands.handlers import convert_currency
import commands.keyboards as kb

from commands.handlers import (first_con_value, second_con_value,
                               first_value)

router = Router()


@router.callback_query(F.data == "asia")
async def asia(callback: CallbackQuery):
    await callback.answer("Sie haben Asien gewählt!")
    await callback.message.edit_text(
        """<b>Asien (außer Naher Osten):</b>
        🇦🇿 AZN - Aserbaidschanischer Manat (Aserbaidschan)
        🇦🇲 AMD - Armenischer Dram (Armenien)
        🇬🇪 GEL - Georgischer Lari (Georgien)
        🇮🇳 INR - Indische Rupie (Indien)
        🇰🇬 KGS - Kirgisischer Som (Kirgisistan)
        🇨🇳 CNY - Chinesischer Yuan (China)
        🇲🇾 MYR - Malaysischer Ringgit (Malaysia)
        🇸🇬 SGD - Singapur-Dollar (Singapur)
        🇹🇯 TJS - Tadschikischer Somoni (Tadschikistan)
        🇹🇭 THB - Thailändischer Baht (Thailand)
        🇹🇷 TRY - Türkische Lira (Türkei)
        🇺🇿 UZS - Usbekischer Sum (Usbekistan)
        🇰🇷 KRW - Südkoreanischer Won (Südkorea)
        🇯🇵 JPY - Japanischer Yen (Japan)""",
        reply_markup=kb.back_regions)


@router.callback_query(F.data == "europa")
async def europa(callback: CallbackQuery):
    await callback.answer("Sie haben Europa gewählt!")
    await callback.message.edit_text(
        """<b>Europa:</b>
        🇧🇾 BYN - Weißrussischer Rubel (Weißrussland)
        🇩🇰 DKK - Dänische Krone (Dänemark)
        🇪🇺 EUR - Euro (Eurozone)
        🇲🇩 MDL - Moldauischer Leu (Moldau)
        🇳🇴 NOK - Norwegische Krone (Norwegen)
        🇵🇱 PLN - Polnischer Zloty (Polen)
        🇷🇺 RUB - Russischer Rubel (Russland)
        🇺🇦 UAH - Ukrainische Griwna (Ukraine)
        🇬🇧 GBP - Britisches Pfund Sterling (Vereinigtes Königreich)
        🇨🇿 CZK - Tschechische Krone (Tschechien)
        🇸🇪 SEK - Schwedische Krone (Schweden)
        🇨🇭 CHF - Schweizer Franken (Schweiz)
        🌐 XDR - Sonderziehungsrechte (Internationaler Währungsfonds)""",
        reply_markup=kb.back_regions)


@router.callback_query(F.data == "amerika")
async def amerika(callback: CallbackQuery):
    await callback.answer("Sie haben Amerika gewählt!")
    await callback.message.edit_text(
        """<b>Amerika:</b>
        🇧🇷 BRL - Brasilianischer Real (Brasilien)
        🇨🇦 CAD - Kanadischer Dollar (Kanada)
        🇲🇽 MXN - Mexikanischer Peso (Mexiko)
        🇺🇸 USD - US-Dollar (Vereinigte Staaten von Amerika)""",
        reply_markup=kb.back_regions)


@router.callback_query(F.data == "afrika")
async def afrika(callback: CallbackQuery):
    await callback.answer("Sie haben Afrika und den Nahen Osten gewählt!")
    await callback.message.edit_text(
        """<b>Afrika und Naher Osten:</b>
        🇦🇪 AED - VAE-Dirham (Vereinigte Arabische Emirate)
        🇸🇦 SAR - Saudi-Riyal (Saudi-Arabien)
        🇰🇼 KWD - Kuwait-Dinar (Kuwait)
        🇮🇷 IRR - Iranischer Rial (Iran)
        🇿🇦 ZAR - Südafrikanischer Rand (Südafrika)""",
        reply_markup=kb.back_regions)


@router.callback_query(F.data == "oceania")
async def oceania(callback: CallbackQuery):
    await callback.answer("Sie haben Ozeanien gewählt.")
    await callback.message.edit_text(
        """<b>Ozeanien:</b>
        🇦🇺 AUD - Australischer Dollar (Australien)
        🇳🇿 NZD - Neuseeländischer Dollar (Neuseeland)""",
        reply_markup=kb.back_regions)


@router.callback_query(F.data == "crypto_list")
async def crypto_list(callback: CallbackQuery):
    await callback.answer("Liste der Kryptowährungen.")
    await callback.message.edit_text(
        """<b>Top 50 Kryptowährungen:</b>
        1. BTC — Bitcoin  
        2. ETH — Ethereum  
        3. USDT — Tether  
        4. XRP — XRP  
        5. BNB — Binance Coin  
        6. SOL — Solana  
        7. DOGE — Dogecoin  
        8. USDC — USD Coin  
        9. ADA — Cardano  
        10. STETH — Lido Staked Ether  
        11. TRX — Tron  
        12. AVAX — Avalanche  
        13. LINK — Chainlink  
        14. SHIB — Shiba Inu  
        15. WBTC — Wrapped Bitcoin  
        16. XLM — Stellar  
        17. DOT — Polkadot  
        18. SPX — Sp8de  
        19. BCH — Bitcoin Cash  
        20. LEO — UNUS SED LEO  
        21. LTC — Litecoin  
        22. UNI — Uniswap  
        23. NEAR — NEAR-Protokoll  
        24. DAI — DAI Stablecoin  
        25. ICP — Internet Computer  
        26. AAVE — Aave  
        27. HBAR — Hedera Hashgraph  
        28. ETC — Ethereum Classic  
        29. VET — VeChain  
        30. XMR — Monero  
        31. CRO — Crypto.com Coin  
        32. FET — Fetch.ai  
        33. FIL — Filecoin  
        34. ALGO — Algorand  
        35. OKB — OKB  
        36. STX — Stacks  
        37. THETA — Theta Network  
        38. GRT — The Graph  
        39. OM — Mantra DAO  
        40. FTM — Fantom  
        41. GT — GateToken  
        42. ATOM — Cosmos  
        43. INJ — Injective Protocol  
        44. LDO — Lido DAO  
        45. RAY — Raydium  
        46. SAND — The Sandbox  
        47. MKR — Maker  
        48. XTZ — Tezos  
        49. KCS — KuCoin Token  
        50. GALA — Gala""",
        reply_markup=kb.back_regions)


@router.callback_query(F.data == "back_reg")
async def back_reg(callback: CallbackQuery):
    await callback.answer("Sie sind zurückgekehrt.")
    await callback.message.delete()
    await callback.message.answer(
        "<b>Wählen Sie die Region des Landes aus</b>,\nfür dessen Währungscode Sie sich interessieren.",
        reply_markup=kb.regions)


@router.callback_query(F.data == "clbk_otherlist_value")
async def other_list_values(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(f"Unten finden Sie die vollständige Liste der Währungen", reply_markup=kb.full_list())


@router.callback_query(F.data.startswith("add_popular_value_"))
async def input_numbers(callback: CallbackQuery, state: FSMContext):
    action = callback.data.split('_')[-1]  # Extrahiere Daten aus callback_data
    value, answer_, text = await check_popular_list(action)  # Überprüfen und die benötigten Daten erhalten

    await callback.answer(answer_)

    if not first_con_value.get(callback.from_user.id):
        # Speichern der ersten Währung

        first_con_value[callback.from_user.id] = value
        await callback.message.edit_text(
            f"{text}\nGeben Sie die Währung an, in die Sie umrechnen möchten:",
            reply_markup=kb.popular_values()
        )
    else:
        # Abrufen der Daten für die Umrechnung
        f_value = first_value.get(callback.from_user.id)  # Betrag für die Umrechnung
        f_con_value = first_con_value.get(callback.from_user.id)  # Ausgangswährung
        second_con_value[callback.from_user.id] = value  # Zielwährung

        # Überprüfen, ob ein Betrag angegeben wurde
        if not f_value:
            await callback.message.answer("Geben Sie die Menge der Währung ein, die umgerechnet werden soll, mithilfe des Befehls.")
            return

        # Durchführung der Umrechnung
        rates = await get_exchange_rates()  # Abrufen der aktuellen Wechselkurse
        converted_amount = await convert_currency(f_value, f_con_value, value, rates)
        print(converted_amount)

        # Ausgabe des Ergebnisses
        await callback.message.answer(
            f"Umrechnung: {f_value} {f_con_value} = {converted_amount:.4f} {value}"
        )


@router.callback_query(F.data.startswith("add_fulllist_value_"))
async def input_numbers(callback: CallbackQuery, state: FSMContext):
    action = callback.data.split('_')[-1]  # Extrahiere Daten aus callback_data
    value, answer_, text = await check_fulllist_values(action)  # Überprüfen und die benötigten Daten erhalten

    await callback.answer(answer_)

    if first_con_value.get(callback.from_user.id):
        # Abrufen der Daten für die Umrechnung
        f_value = first_value.get(callback.from_user.id)  # Betrag für die Umrechnung
        f_con_value = first_con_value.get(callback.from_user.id)  # Ausgangswährung
        second_con_value[callback.from_user.id] = value  # Zielwährung

        # Überprüfen, ob ein Betrag angegeben wurde
        if not f_value:
            await callback.message.answer("Geben Sie die Menge der Währung ein, die umgerechnet werden soll, mithilfe des Befehls.")
            return

        # Durchführung der Umrechnung
        rates = get_exchange_rates()  # Abrufen der aktuellen Wechselkurse
        converted_amount = convert_currency(f_value, f_con_value, value, rates)

        # Ausgabe des Ergebnisses
        await callback.message.answer(
            f"Umrechnung: {f_value} {f_con_value} = {converted_amount:.4f} {value}"
        )
    else:
        # Speichern der ersten Währung
        first_con_value[callback.from_user.id] = value
        await callback.message.edit_text(
            f"{text}\nGeben Sie die Menge der Währung ein, die Sie umrechnen möchten:",
            reply_markup=kb.popular_values()
        )

async def check_popular_list(action):
    value = action
    currency_descriptions = {
        "USD": "🇺🇸 US-Dollar",
        "EUR": "🇪🇺 Euro"        ,
        "RUB": "🇷🇺 Russischer Rubel",
        "AED": "🇦🇪 VAE-Dirham",
        "BYN": "🇧🇾 Weißrussischer Rubel",
        "UAH": "🇺🇦 Ukrainische Griwna",
        "KZT": "🇰🇿 Kasachischer Tenge",
        "GEL": "🇬🇪 Georgischer Lari",
        "CNY": "🇨🇳 Chinesischer Yuan",
        "JPY": "🇯🇵 Japanischer Yen",
        "TRY": "🇹🇷 Türkische Lira",
        "GBP": "🇬🇧 Britisches Pfund Sterling",
        "BTC": "₿ Bitcoin",
        "ETH": "Ξ Ethereum",
        "SOL": "SOL (Solana)",
        "TON": "TON (The Open Network)"
    }
    answer_ = f"Sie haben gewählt: {currency_descriptions[action]} ({value})"
    text = f"Sie haben gewählt: <b>{currency_descriptions[action]}</b> (<b>{value}</b>)"
    return value, answer_, text


async def check_fulllist_values(action):
    value = action
    currency_descriptions = {
        "AUD": "🇦🇺 Australischer Dollar",
        "AZN": "🇦🇿 Aserbaidschanischer Manat",
        "BRL": "🇧🇷 Brasilianischer Real",
        "BYN": "🇧🇾 Weißrussischer Rubel",
        "CAD": "🇨🇦 Kanadischer Dollar",
        "CHF": "🇨🇭 Schweizer Franken",
        "CNY": "🇨🇳 Chinesischer Yuan",
        "CZK": "🇨🇿 Tschechische Krone",
        "DKK": "🇩🇰 Dänische Krone",
        "EUR": "🇪🇺 Euro",
        "GBP": "🇬🇧 Britisches Pfund Sterling",
        "GEL": "🇬🇪 Georgischer Lari",
        "IRR": "🇮🇷 Iranischer Rial",
        "INR": "🇮🇳 Indische Rupie",
        "JPY": "🇯🇵 Japanischer Yen",
        "KWD": "🇰🇼 Kuwait-Dinar",
        "KGS": "🇰🇬 Kirgisischer Som",
        "KRW": "🇰🇷 Südkoreanischer Won",
        "MYR": "🇲🇾 Malaysischer Ringgit",
        "MDL": "🇲🇩 Moldauischer Leu",
        "MXN": "🇲🇽 Mexikanischer Peso",
        "NOK": "🇳🇴 Norwegische Krone",
        "NZD": "🇳🇿 Neuseeländischer Dollar",
        "PLN": "🇵🇱 Polnischer Zloty",
        "RUB": "🇷🇺 Russischer Rubel",
        "SAR": "🇸🇦 Saudi-Riyal",
        "SGD": "🇸🇬 Singapur-Dollar",
        "SEK": "🇸🇪 Schwedische Krone",
        "THB": "🇹🇭 Thailändischer Baht",
        "TJS": "🇹🇯 Tadschikischer Somoni",
        "TRY": "🇹🇷 Türkische Lira",
        "UAH": "🇺🇦 Ukrainische Griwna",
        "UZS": "🇺🇿 Usbekischer Sum",
        "VND": "🇻🇳 Vietnamesischer Dong",
        "ZAR": "🇿🇦 Südafrikanischer Rand"
    }
    answer_ = f"Sie haben gewählt: {currency_descriptions[action]} ({value})"
    text = f"Sie haben gewählt: <b>{currency_descriptions[action]}</b> (<b>{value}</b>)"
    return value, answer_, text
