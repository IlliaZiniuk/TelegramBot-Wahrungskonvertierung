import xmltodict
import json
import httpx
from secret.config import NBK_API
import os

print(os.path.exists('json_XML.py'))  # Gibt True/False aus (ob die Datei existiert)


async def fetch_exchange_rates():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(NBK_API)
            response.raise_for_status()

            xml_data = response.text
            data_dict = xmltodict.parse(xml_data)

            json_data = json.dumps(data_dict, indent=4, ensure_ascii=False)

            return json_data

    except httpx.HTTPStatusError as e:
        print(f"HTTP-Fehler bei der Anfrage an {NBK_API}: {e}")
    except httpx.RequestError as e:
        print(f"Anfragefehler bei {NBK_API}: {e}")

    return {}


async def get_exchange_rates():
    try:
        # Konvertieren von JSON-String in ein Python-Dictionary
        json_data = await fetch_exchange_rates()
        data_dict = json.loads(json_data)

        # Extrahieren der Wechselkurse
        rates = {}
        for item in data_dict['rss']['channel']['item']:
            currency_code = item['title']
            rate = float(item['description'].replace(",", "."))  # Komma durch Punkt für die Zahl ersetzen
            rates[currency_code] = rate

        # Hinzufügen des Wechselkurses von KZT zu sich selbst
        rates['KZT'] = 1

        return rates

    except json.JSONDecodeError as e:
        raise ValueError(f"Fehler beim Dekodieren von JSON: {e}")
