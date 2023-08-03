import os
import requests
from aiogram import Dispatcher, types

async def start_bot(msg: types.Message):
    if msg.from_user.id == int(os.getenv("ADMIN_ID")):
        start_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        pay_sub = types.KeyboardButton(text="Показать туннели")
        start_kb.row(pay_sub)
        await msg.answer(text='Здравствуйте!', reply_markup=start_kb)
    else:
        await msg.answer(text="Доступ запрещён!!")

async def get_tunnels(msg: types.Message):
    if msg.from_user.id == int(os.getenv("ADMIN_ID")):
        if os.getenv("API_NGROK"):
            headers = {
                'Authorization': f'Bearer {os.getenv("API_NGROK")}',
                'Ngrok-Version': '2',
            }

            response = requests.get('https://api.ngrok.com/tunnels', headers=headers)
            text_tunnel = ''
            for tunnel in response.json()['tunnels']:
                text_tunnel += f'{tunnel["proto"]}:{tunnel["public_url"]}\n'
            await msg.answer(text=text_tunnel)
        else:
            await msg.answer("Отсуствует API для Ngrok!")
    else:
        await msg.answer(text="Доступ запрещён!!")

async def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands='start')
    dp.register_message_handler(get_tunnels, lambda msg: msg.text == 'Показать туннели')
