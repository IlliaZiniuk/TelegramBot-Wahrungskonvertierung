from aiogram.filters import CommandStart
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
# from commands.formatting import get_conversion_rate
import commands.keyboards as kb
from info.middlewares import TestMiddleware
from commands.json_XML import get_exchange_rates
from commands.formatting import convert_currency

router = Router()
router.message.outer_middleware(TestMiddleware())
first_value = {}
second_value = {}
first_con_value = {}
second_con_value = {}


class ConversionStates(StatesGroup):
    input_number = State()


# Funktion zum Abrufen der Währungsliste
@router.message(CommandStart())
async def start_command(message: Message):
    await message.reply(f"Dein Nickname: {message.from_user.first_name} Deine ID: {message.from_user.id}",
                        reply_markup=kb.main)


@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer("Dies ist der Hilfe-Befehl.")


@router.message(F.text == "Wie geht's?")
async def ef_command(message: Message):
    await message.answer("Mir geht's gut, danke der Nachfrage! :)")


@router.message(F.text == "Währungsliste")
async def currency_list(message: Message):
    await message.answer(
        "<b>Wählen Sie die Region des Landes</b>,\nderen Währungscode Sie sehen möchten.\n"
        "Oder Sie können <b>Beliebte Währungen</b> und <b>Kryptowährungen</b> auswählen.",
        reply_markup=kb.regions
    )


@router.message(Command("con"))
async def convert_crypto(message: Message):
    try:
        args = message.text.split(maxsplit=3)
        if len(args) != 4:
            await message.answer("Bitte verwenden Sie das Befehlsformat:\n/con <Betrag> <Von_Währung> <Zu_Währung>")
            return

        amount = float(args[1])
        from_currency = args[2].upper()
        to_currency = args[3].upper()

        rates = get_exchange_rates()

        converted_amount = convert_currency(amount, from_currency, to_currency, rates)
        await message.answer(f"{amount} {from_currency} = {converted_amount:.6f} {to_currency}")

    except ValueError as e:
        await message.answer(f"Fehler: {str(e)}")
    except Exception as e:
        await message.answer(f"Ein unerwarteter Fehler ist aufgetreten: {str(e)}")


@router.message(F.text == "Konvertierung")
async def input_numbers(message: Message, state: FSMContext):
    first_con_value[message.from_user.id] = None
    await state.set_state(ConversionStates.input_number)  # Status setzen
    await message.answer(f"Geben Sie die Menge der Währung ein, die Sie umrechnen möchten:")


@router.message(ConversionStates.input_number)
async def input_values(message: Message, state: FSMContext):
    first_value[message.from_user.id] = message.text
    f_value = first_value.get(message.from_user.id)
    await state.clear()
    await message.answer(f"Sie haben gewählt: {f_value}."
                         f"\nWählen Sie die Währung, von der umgerechnet werden soll⬇️",
                         reply_markup=kb.popular_values())
