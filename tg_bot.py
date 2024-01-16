import telebot

from config import TG_TOKEN

bot = telebot.TeleBot(TG_TOKEN)
tg_admin_id = 1286858830

fake_database = {'users': [
    {
        "id": 1,
        "name": "Anna",
        "nick": "Anny42",
        "balance": 15300
    },

    {
        "id": 2,
        "name": "Dima",
        "nick": "dimon2319",
        "balance": 160.23
    },
    {
        "id": 3,
        "name": "Vladimir",
        "nick": "Vova777",
        "balance": 200.1
    },
    {
        "id": 4,
        "name": "Anna1",
        "nick": "Anny420",
        "balance": 15300
    },

    {
        "id": 5,
        "name": "Dima15",
        "nick": "dimon2342",
        "balance": 160.23
    },
    {
        "id": 6,
        "name": "Vladimir666",
        "nick": "Vova13",
        "balance": 200.1
    },
    {
        "id": 7,
        "name": "Anna2",
        "nick": "Anny421",
        "balance": 15300
    },

    {
        "id": 8,
        "name": "Dima23",
        "nick": "dimon19",
        "balance": 160.23
    },
    {
        "id": 9,
        "name": "Vladimir0nion",
        "nick": "Vova123",
        "balance": 200.1
    },

], }


@bot.message_handler(commands=['start'])
def start_message(message):
    # создаем объект для работы с кнопками (row_width - определяет количество кнопок по ширине)
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    # создаем каждую кнопку таким образом
    btn1 = telebot.types.KeyboardButton('Кошелек')
    btn2 = telebot.types.KeyboardButton('Перевести')
    btn3 = telebot.types.KeyboardButton('История')

    markup.add(btn1, btn2, btn3)

    text = f'Привет {message.from_user.full_name}, я твой бот-криптокошелек, \n' \
           'у меня ты можешь хранить и отправлять биткоины'

    # теперь добавляем объект с кнопками к отправляемому пользователю сообщению в аргумент "reply_markup"
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(regexp='Кошелек')
def wallet(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton(
        'Меню')  # мы создали ещё одну кнопку, которую надо обработать
    markup.add(btn1)
    balance = 0  # сюда мы будем получать баланс через наш API
    text = f'Ваш баланс: {balance}'
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(regexp='Перевести')
def transaction(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Меню')
    markup.add(btn1)
    text = f'Введите адрес кошелька куда хотите перевести: '
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(regexp='История')
def history(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Меню')
    markup.add(btn1)
    transactions = ['1', '2', '3']  # сюда мы загрузим транзакции
    text = f'Ваши транзакции{transactions}'
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(regexp='Меню')
def menu(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Кошелек')
    btn2 = telebot.types.KeyboardButton('Перевести')
    btn3 = telebot.types.KeyboardButton('История')
    markup.add(btn1, btn2, btn3)

    text = f'Главное меню'
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(regexp='Я в консоли')
def print_me(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Меню')
    markup.add(btn1)
    print(message.from_user.to_dict())
    text = f'Ты: {message.from_user.to_dict()}'
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(
    func=lambda message: message.from_user.id == tg_admin_id and message.text == "Админка")
def admin_panel(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Общий баланс')
    btn2 = telebot.types.KeyboardButton('Все юзеры')
    btn3 = telebot.types.KeyboardButton('Меню')
    markup.add(btn1, btn2, btn3)
    text = f'Админ-панель'
    bot.send_message(message.chat.id, text, reply_markup=markup)


users = fake_database['users']


# делаем проверку на админ ли боту пишет проверяем текст сообщения
# @bot.message_handler(
#     func=lambda message: message.from_user.id == tg_admin_id and message.text == "Все юзеры")
# def all_users(message):
#     text = f'Юзеры:'
#     inline_markup = telebot.types.InlineKeyboardMarkup()  # создаем объект с инлайн-разметкой
#     for user in users:  # в цикле создаем 3 кнопки и добавляем их поочередно в нашу разметку
#         inline_markup.add(telebot.types.InlineKeyboardButton(text=f'Юзер: {user["name"]}',
#                                                              callback_data=f"user_{user['id']}"))
#         # так как мы добавляем кнопки по одной, то у нас юзеры будут в 3 строчки
#         # в коллбеке у нас будет текст, который содержит айди юзеров
#     bot.send_message(message.chat.id, text,
#                      reply_markup=inline_markup)  # прикрепляем нашу разметку к ответному сообщению


@bot.message_handler(
    func=lambda message: message.from_user.id == tg_admin_id and message.text == "Все юзеры")
def all_users_paginated(message):
    current_page = 1  # начальная страница
    users_per_page = 4  # количество юзеров на одной странице

    show_users_page(message.chat.id, current_page, users_per_page,
                    None)  # отобразить первую страницу


def show_users_page(chat_id, page, users_per_page, sent_message):
    start_index = (page - 1) * users_per_page
    end_index = start_index + users_per_page

    users_to_show = users[start_index:end_index]

    inline_markup = telebot.types.InlineKeyboardMarkup()

    for user in users_to_show:
        inline_markup.add(telebot.types.InlineKeyboardButton(text=f'Юзер: {user["name"]}',
                                                             callback_data=f"user_{user['id']}"))

    navigation_markup = create_navigation_markup(page, users_per_page)

    # Создаем новую разметку, объединяя существующую и навигацию
    combined_markup = telebot.types.InlineKeyboardMarkup()
    combined_markup.keyboard = [*inline_markup.keyboard, *navigation_markup.keyboard]

    if sent_message:
        bot.edit_message_reply_markup(chat_id=chat_id, message_id=sent_message.message_id,
                                      reply_markup=combined_markup)
    else:
        sent_message = bot.send_message(chat_id, text="Юзеры и навигация:",
                                        reply_markup=combined_markup)

    return sent_message


def create_navigation_markup(current_page, users_per_page):
    total_pages = (
                          len(users) + users_per_page - 1) // users_per_page  # округленное вверх количество страниц

    navigation_markup = telebot.types.InlineKeyboardMarkup()

    back_button = telebot.types.InlineKeyboardButton(text="Назад",
                                                     callback_data=f"users_{current_page - 1}")
    page_indicator = telebot.types.InlineKeyboardButton(text=f"{current_page}/{total_pages}",
                                                        callback_data="page_indicator")
    forward_button = telebot.types.InlineKeyboardButton(text="Вперед",
                                                        callback_data=f"users_{current_page + 1}")

    if current_page > 1:
        navigation_markup.add(back_button)

    navigation_markup.add(page_indicator)

    if current_page < total_pages:
        navigation_markup.add(forward_button)

    return navigation_markup


@bot.callback_query_handler(func=lambda call: call.data.startswith("users"))
def handle_users_callback(call):
    print(call.data)
    action, page = call.data.split("_")
    page = int(page)

    if action == "users":
        sent_message = show_users_page(call.message.chat.id, page, 4, call.message)
        # сохраняем отправленное сообщение, чтобы можно было редактировать
        # если потребуется какие-то дополнительные действия с этим сообщением
        # (например, удаление кнопок после выбора юзера)
        bot.register_next_step_handler(sent_message, lambda m: None)
    elif action == "page_indicator":
        pass  # добавьте обработку, если нужно, когда пользователь нажимает на индикатор страницы


# в качестве условия для обработки принимает только лямбда-функции
@bot.callback_query_handler(func=lambda call: True)  # хендлер принимает объект Call
def callback_query(call):
    query_type = call.data.split('_')[0]  # получаем тип запроса
    if query_type == 'user':
        user_id = call.data.split('_')[1]  # получаем айди юзера из нашей строки
        inline_markup = telebot.types.InlineKeyboardMarkup()
        for user in users:
            if str(user['id']) == user_id:
                inline_markup.add(
                    telebot.types.InlineKeyboardButton(text="Назад", callback_data=f'users'),
                    telebot.types.InlineKeyboardButton(text="Удалить юзера",
                                                       callback_data=f'delete_user_{user_id}'))

                bot.edit_message_text(text=f'Данные по юзеру:\n'
                                           f'ID: {user["id"]}\n'
                                           f'Имя: {user["name"]}\n'
                                           f'Ник: {user["nick"]}\n'
                                           f'Баланс: {user["balance"]}',
                                      chat_id=call.message.chat.id,
                                      message_id=call.message.message_id,
                                      reply_markup=inline_markup)
                print(f"Запрошен {user}")
                break

    if query_type == 'users':
        inline_markup = telebot.types.InlineKeyboardMarkup()
        for user in users:
            # к каждой кнопке прикручиваем в callback_data айди юзера, чтобы можно было идентифицировать нажатую кнопку
            inline_markup.add(telebot.types.InlineKeyboardButton(text=f'Юзер: {user["name"]}',
                                                                 callback_data=f"user_{user['id']}"))
        bot.edit_message_text(text="Юзеры:",
                              chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              reply_markup=inline_markup)  # прикрепляем нашу разметку к ответному сообщению

    if query_type == 'delete' and call.data.split('_')[1] == 'user':
        user_id = int(call.data.split('_')[2])  # получаем и превращаем наш айди в число
        for i, user in enumerate(users):
            if user['id'] == user_id:
                print(f'Удален Юзер: {users[i]}')
                users.pop(i)
        inline_markup = telebot.types.InlineKeyboardMarkup()
        for user in users:
            inline_markup.add(telebot.types.InlineKeyboardButton(text=f'Юзер: {user["name"]}',
                                                                 callback_data=f"user_{user['id']}"))
        bot.edit_message_text(text="Юзеры:",
                              chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              reply_markup=inline_markup)  # прикрепляем нашу разметку к ответному сообщению


@bot.message_handler(
    func=lambda message: message.from_user.id == tg_admin_id and message.text == "Общий баланс")
def total_balance(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Меню')
    btn2 = telebot.types.KeyboardButton('Админка')
    markup.add(btn1, btn2)
    balance = 0
    for user in users:
        balance += user['balance']
    text = f'Общий баланс: {balance}'
    bot.send_message(message.chat.id, text, reply_markup=markup)


# запускаем бота этой командой:
bot.infinity_polling()
