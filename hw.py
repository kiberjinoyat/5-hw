from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from keyboard import menu, nastroyka, kontakt, otmen, next_menu, instagram, otmen1, menu_uzb, nastroyka_uzb, kontakt_uzb, otmen_uzb, otmen1_uzb, next_menu_uzb, instagram_uzb

BOT_TOKEN = "6753222944:AAHU-fcNNrDPbBZ7hpTELx1Mr2UnETMAdAE"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)

photo = "https://avatars.mds.yandex.net/i?id=cb05b294b802c97b5693912b3014aa20f3ca6922-9065836-images-thumbs&n=13"


@dp.message_handler(commands=["start", "help"])
async def start_bot(message: types.Message):
    await message.answer(text="""Здравствуйте! Добро пожаловать в наш бот! Давайте для начала выберем язык обслуживания!

 Assalomu aleykum! Botimizga xush kelibsiz! Keling, avvaliga xizmat ko’rsatish tilini tanlab olaylik.

 Hello! Welcome to our Bot! Let's choose the language of service first""",
                         reply_markup=next_menu())


@dp.callback_query_handler()
async def callback_func(callback: types.CallbackQuery):
    if callback.data == "English 🇺🇸":
        await callback.message.answer(text="")
    elif callback.data == "Русский 🇷🇺":
        await callback.message.answer_photo(photo=photo,
                                            caption="""Добро пожаловать в "Let's Food" - бота по обслуживанию и доставке еды! Наш бот готов предложить Вам различные блюда каждый день в соответствии с меню. Работаем мы с 11:00 до 20:00, чтобы Ваш обед был вкусным и своевременным. 
Подробности о нашем меню можно узнать, следуя за нами в Instagram   @letsfood_tashkent (https://www.instagram.com/letsfood_tashkent) , для получения инструкции как пользоваться ботом нажмите /instruction
Мы готовы удовлетворить любой вкус и сделать Ваш обед незабываемым!

Также, мы рады сообщить, что при заказе более 5 порций, доставка осуществляется бесплатно! В нашем меню имеются два варианта порций: "Cет" и "Полусет". 
Стоимость порции:

"Cет" составляет 40 000, 

"Полусет" - 35 000. 

Мы гарантируем, что каждое блюдо будет свежим, вкусным и приготовлено с любовью. Ждем Вашего заказа!

Кушай вкусно, каждый день
@letsfood_bot""",
                                            reply_markup=menu())
        await callback.message.answer(text="instagram", reply_markup=instagram())
    elif callback.data == "Õzbek🇺🇿":
        await callback.message.answer(text="""Let's Food" - oziq-ovqat xizmati va yetkazib berish botiga xush kelibsiz! Bizning botimiz sizga har kuni menyuga ko'ra turli xil taomlarni taklif qilishga tayyor. Tushlik mazali va o'z vaqtida bo'lishi uchun soat 11:00 dan 20:00 gacha ishlaymiz.
Menyumiz haqida batafsil ma'lumotni ijtimoiy tarmog'imiz  @letsfood_tashkent (https://www.instagram.com/letsfood_tashkent) sahifasida bizni kuzatish orqali olishingiz mumkin.
Botdan foydalanish uchun qo'llanma /instruction
Biz har qanday ta'mni qondirishga va kechki ovqatingizni unutilmas qilishga tayyormiz!

Bundan tashqari, biz mamnuniyat bilan e'lon qilamizki, 5 tadan ortiq porsiyaga buyurtma berganingizda, yetkazib berish bepul! Bizning menyuda ikki turdagi qismlar mavjud: Cет va Полусет.
Xizmat narxi:

"Cет" - 40 000 so'm

"Полусет" - 35 000 so'm

Har bir taom  mazali va mehr bilan tayyorlangan bo'lishiga kafolat beramiz. Buyurtmangizni kutamiz!

Har kuni mazali ovqatlaning
@letsfood_bot""", reply_markup=menu_uzb())


@dp.message_handler(Text(equals="Заказать 🛍"))
async def start_bot(message: types.Message):
    await message.answer(text="""Извините за неудобства, но у нас закончились обеды
Попробуйте новые вкусы уже завтра!
@letsfood_bot""")

@dp.message_handler(Text(equals="Buyurtma berish 🛍"))
async def start_bot(message: types.Message):
    await message.answer(text="""Noqulaylik uchun uzr, Bugingi taomlar tugadi
Ertaga yangi ta'mlarni sinab ko'ring!
@letsfood_bot""")



@dp.message_handler(Text(equals="Информация ℹ️"))
async def start_bot(message: types.Message):
    await message.answer(text="""📌 Здесь вы можете найти информацию о нашем ресторане    
📞 Номер телефона: +998(90) 177-73-37
🕐 Время работы: 10:00 - 20:00
⚡️Contact: @letsfood_bot_admin 
📲 Следите за нами в социальных сетях::""",
                         reply_markup=instagram())

@dp.message_handler(Text(equals="Ma'lumot ℹ️"))
async def start_bot(message: types.Message):
    await message.answer(text="""📌 Bu yerda siz bizning restoranimiz haqida ma'lumot olishingiz mumkin    
📞 Phone number: +998(90) 177-73-37
🕐 Ish vaqti: 10:00 - 20:00
⚡️Contact: @letsfood_bot_admin
📲 Bizning ijtimoiy tarmoqlarda kuzating:""",
                         reply_markup=instagram_uzb())



@dp.message_handler(Text(equals="Настройки⚙️"))
async def start_bot(message: types.Message):
    await message.answer(text="Изменить настройки", reply_markup=nastroyka())

@dp.message_handler(Text(equals="Sozlamalar⚙️"))
async def start_bot(message: types.Message):
    await message.answer(text="Sozlamalarni o'zgartirish", reply_markup=nastroyka_uzb())



@dp.message_handler(Text(equals="Отзыв/комментарий  📩"))
async def start_bot(message: types.Message):
    await message.answer(text="Отправьте свой отзыв", reply_markup=otmen())

@dp.message_handler(Text(equals="Feedback 📩"))
async def start_bot(message: types.Message):
    await message.answer(text="Servisimiz uchun o'z fikrlaringizni yuboring", reply_markup=otmen_uzb())



@dp.message_handler(Text(equals="Отменить ❌"))
async def start_bot(message: types.Message):
    await message.answer(text="Отправьте свой отзыв", reply_markup=menu())

@dp.message_handler(Text(equals="Bekor qilish ❌"))
async def start_bot(message: types.Message):
    await message.answer(text="Bekor qilindi", reply_markup=menu_uzb())



@dp.message_handler(Text(equals="Изменить язык🇷🇺"))
async def start_bot(message: types.Message):
    await message.answer(text="Выберите свой язык:", reply_markup=next_menu())

@dp.message_handler(Text(equals="Tilni o'zgartirish  🇺🇿"))
async def start_bot(message: types.Message):
    await message.answer(text="Выберите свой язык:", reply_markup=next_menu_uzb())


@dp.message_handler(Text(equals="Ismni o'zgartirish  ✏️"))
async def start_bot(message: types.Message):
    await message.answer(text="Ismingizni kiriting:", reply_markup=otmen1_uzb())


@dp.message_handler(Text(equals="Отменит"))
async def start_bot(message: types.Message):
    await message.answer(text="Оrtga", reply_markup=nastroyka())

@dp.message_handler(Text(equals="Ortga ⬅️"))
async def start_bot(message: types.Message):
    await message.answer(text="Оrtga", reply_markup=nastroyka_uzb())


@dp.message_handler(Text(equals="Изменить номер телефона 📱"))
async def start_bot(message: types.Message):
    await message.answer(text="""Введите свой номер телефона:
\n
Ваш текущий телефон:   998910181159""", reply_markup=kontakt())

@dp.message_handler(Text(equals="Telefon raqamni o'zgartirish  📱"))
async def start_bot(message: types.Message):
    await message.answer(text="""Telefon raqamingizni kiriting yoki kontanktingizni ulashing:
\n
Sizning hozirgi raqamingiz:""", reply_markup=kontakt_uzb())




@dp.message_handler(Text(equals="Назад ⬅️"))
async def start_bot(message: types.Message):
    await message.answer(text="Отправьте свой имя:", reply_markup=nastroyka())

@dp.message_handler(Text(equals="Ortga ⬅️"))
async def start_bot(message: types.Message):
    await message.answer(text="Sozlamalarni o'zgartirish", reply_markup=nastroyka_uzb())



@dp.message_handler(Text(equals="Ortga ⬅️"))
async def start_bot(message: types.Message):
    await message.answer(text="Buyurtma berishni boshlash uchun 🛍 Buyurtma berish tugmasini bosing", reply_markup=menu_uzb())







if __name__ == '__main__':
    executor.start_polling(dp)