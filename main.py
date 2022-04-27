import requests
import logging
from aiogram import Bot, Dispatcher, executor, types
# Объект бота
bot = Bot(token="5108226092:AAFfUfMtHzn1n4FNZ9IrGJz5teSHUsW4XRs")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

def jsonapi():
    print('das')
    r = requests.get('https://api.tez-shop.com.kg/prod-list/?format=json')
    data = r.json()
    
    return data[-1]

# Хэндлер на команду /test1
@dp.message_handler(commands="start")
async def cmd_test1(message: types.Message):
    print('123')
    data = dict(jsonapi())
    print(data)
    nal = data['are_available']
    if nal == True:
        nal = 'Нет в наличии'
    else:
        nal = 'Есть в наличии'
    caption = (f'''
Навзание заказа - {data['name']}
Цена - {data['price']}
{nal}

''')
    await bot.send_photo(chat_id=message.chat.id, photo=data['img'], caption=caption)


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
