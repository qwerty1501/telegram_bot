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
    products = r.json()
    return products

# Хэндлер на команду /start
@dp.message_handler(commands="start")
async def cmd_test1(message: types.Message):
    products = jsonapi()
    
    for data in products[:10]:
        caption = f"""
        Навзание заказа - {data['name']}
        Цена - {data['price']}
        """
        img_url = data['img']
        
        if 'webp' in img_url:
            img_url = 'https://www.groupestate.gr/images/joomlart/demo/default.jpg'
        
        await bot.send_photo(chat_id=message.chat.id, photo=img_url, caption=caption)


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
