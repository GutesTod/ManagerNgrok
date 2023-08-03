from aiogram import Dispatcher, types

async def start_bot(msg: types.Message):
    
    await msg.answer(text='Здравствуйте!')

async def get_tunnels():
    pass

async def register_handlers(dp: Dispatcher):
    pass