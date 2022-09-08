from loader import dp

from utils.database import MongoDB


@dp.message_handler()
async def test(message):
    await message.answer('test')
    info = await MongoDB.add_some_data()
    await message.answer(f"<code>{info}</code>")
