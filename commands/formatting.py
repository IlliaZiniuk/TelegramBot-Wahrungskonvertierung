import requests


async def convert_to_usdt(amount, from_currency, rates):
    if from_currency == "USD":
        return amount
    from_rate = rates["USD"]
    to_rate = rates[from_currency]
    return (amount / from_rate) * to_rate


async def convert_currency(amount, from_currency, to_currency, rates):
    """
    Währungs- und Kryptowährungsumrechnung.
    :param amount: Betrag für die Umrechnung.
    :param from_currency: Ausgangswährung (oder Kryptowährung).
    :param to_currency: Zielwährung (oder Kryptowährung).
    :param rates: Wörterbuch mit Wechselkursen für Fiat-Währungen.
    :return: Umgerechneter Betrag.
    """
    try:
        amount = float(amount)
        if from_currency == to_currency:
            print(1)
            return amount

        if (from_currency in rates) and (to_currency in rates):
            print(2)
            # Fiat → Fiat
            from_rate = rates[to_currency]
            to_rate = rates[from_currency]
            return (amount / from_rate) * to_rate

        elif (from_currency in rates) and (to_currency not in rates):
            print(3)
            # Fiat → Kryptowährung
            amount_in_usdt = await convert_to_usdt(amount, from_currency, rates)
            return amount_in_usdt / await get_conversion_rate("USDT", to_currency)

        elif (from_currency not in rates) and (to_currency in rates):
            print(4)
            # Kryptowährung → Fiat
            usd_rate = rates["USD"]
            to_rate = rates[to_currency]
            crypto_to_usdt = await get_conversion_rate(from_currency, "USDT")  # Krypto-Preis
            amount_in_usdt = await get_conversion_rate(from_currency, "USDT") * amount
            return (amount_in_usdt / usd_rate) * to_rate

        elif (from_currency not in rates) and (to_currency not in rates):
            print(5)
            # Kryptowährung → USDT → Kryptowährung
            crypto_to_usdt = await get_conversion_rate(from_currency, "USDT")
            amount_in_usdt = crypto_to_usdt * amount
            usdt_in_crypto = await get_conversion_rate("USDT", to_currency)
            return amount_in_usdt / usdt_in_crypto

        raise ValueError(f"Unbekannte Kombination von Währungen: {from_currency} → {to_currency}")

    except ValueError:
        raise TypeError(f"Ungültiges Format für den Betrag: {amount}")


async def get_conversion_rate(from_currency, to_currency):
    try:
        # Währung in Großbuchstaben umwandeln
        pair = f"{from_currency}{to_currency}".upper()
        print(pair, from_currency, to_currency)
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={pair}"
        response = requests.get(url)

        # Anfrage und Antwort zum Debuggen ausgeben
        print(f"Anfrage: {url}")
        print(f"Antwort von Binance: {response.text}")

        # Überprüfen, ob die Antwort vom API-Status korrekt ist
        if response.status_code == 200:
            data = response.json()

            # Wenn der Preis in der Antwort enthalten ist
            if "price" in data:
                price = data["price"]
                if price == "0" or not price:
                    raise ValueError(f"Fehler: Preis für das Paar {pair} ist null oder fehlt.")
                print(f"Preis für {pair}: {price}")
                return float(price)

        # Wenn die direkte Anfrage nicht funktioniert hat, versuchen wir das umgekehrte Paar
        pair = f"{to_currency}{from_currency}".upper()
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={pair}"
        response = requests.get(url)

        # Anfrage und Antwort zum Debuggen ausgeben
        print(f"Anfrage: {url}")
        print(f"Antwort von Binance: {response.text}")

        # Überprüfen, ob wir die richtigen Daten erhalten haben
        if response.status_code == 200:
            data = response.json()
            if "price" in data:
                price = data["price"]
                if price == "0" or not price:
                    raise ValueError(f"Fehler: Preis für das Paar {pair} ist null oder fehlt.")
                print(f"Preis für {pair}: {price}")
                return float(price)  # Preis umkehren

        # Wenn das Paar nicht gefunden wurde, werfen wir einen Fehler
        raise ValueError(f"Das Paar {from_currency} → {to_currency} konnte auf Binance nicht gefunden werden")

    except requests.exceptions.RequestException as e:
        raise ValueError(f"Fehler bei der Anfrage an die Binance API: {str(e)}")
    except Exception as e:
        raise ValueError(f"Unbekannter Fehler: {str(e)}")

# Erhalten des Krypto-Wechselkurses über USDT
#    response = requests.get(BINANCE_API, params={"symbol": f"{to_currency}USDT"})
#    if response.status_code == 200 and "price" in response.json():
#        crypto_rate = float(response.json()["price"])  # USDT → Kryptowährung
#        converted_amount = amount * amount_in_usd / crypto_rate  # Benutzerbetrag in USD wird in Kryptowährung umgerechnet
#        return converted_amount
#    else:
#        raise ValueError(f"Fehler: Konnte den Kurs für {to_currency} über USDT nicht erhalten.")
