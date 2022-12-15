import telebot
from telebot import types


bot = telebot.TeleBot('5974623360:AAFGyCUxjqQmkfA7B9oxENIAoCFq5Z2PpUM')

@bot.message_handler(commands=["start"])
def start(m, res=False):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        std = types.KeyboardButton("Заведующие")
        std1 = types.KeyboardButton("Председатели")
        std2 = types.KeyboardButton("Информсектор")
        std3 = types.KeyboardButton("Культмассовый сектор")
        std4 = types.KeyboardButton("Спортсектор")
        std5 = types.KeyboardButton("Редколлегия")
        std6 = types.KeyboardButton("Сантройка")
        markup.add(std)
        markup.add(std1)
        markup.add(std2)
        markup.add(std3)
        markup.add(std4)
        markup.add(std5)
        markup.add(std6)
        bot.send_message(m.chat.id, 'Привет! Что тебе интересно узнать о студсовете общежития №11?',  reply_markup=markup)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == 'Заведующие' :
        bot.send_photo(message.chat.id, 'https://ibb.co/DMXjJ2Y', 'Чемезова Ольга Витальевна')
        bot.send_photo(message.chat.id, 'https://ibb.co/vZYrJcZ', 'Савченко Наталья Геннадьевна')
        bot.reply_to(message, 'Заведующей общежития является Чемезова Ольга Витальевна, а её заместителем Савченко Наталья Геннадьевна.')

    elif message.text == 'Председатели':
        bot.send_photo(message.chat.id, 'https://ibb.co/DYBsMmG', 'Ципилева Ольга  - председатель студенческого совета')
        bot.send_photo(message.chat.id, 'https://ibb.co/pJhj7FY', 'Спиридонов Евгений - председатель редколлегии')
        bot.send_photo(message.chat.id, 'https://ibb.co/pjMxxkP', 'Каминский Марк - председатель спортсектора')
        bot.send_photo(message.chat.id, 'https://ibb.co/GdyhSg0', 'Бельков Кирилл - председатель сантройки')
        bot.send_photo(message.chat.id, 'https://ibb.co/rQBXP7B', 'Дылгыров Булат - председатель культурно-массового сектора')
        bot.send_photo(message.chat.id, 'https://ibb.co/xYrjhCH', 'Григорьев Егор - председатель информационного сектора')

    elif message.text == 'Информсектор':
        bot.send_photo(message.chat.id, 'https://ibb.co/xYrjhCH', 'Григорьев Егор - председатель информационного сектора')
        bot.reply_to(message, 'Информационный сектор делает фотографии мероприятий, ведёт соц.сети общежития, печатает плакаты на стенд и занимается дизайном\n\nСостав информсектора:\nГригорьев Егор\nГегель Анастасия\nНазаров Кирилл\nТанганова Татьяна\nХонский Артём')

    elif message.text == 'Культмассовый сектор':
        bot.send_photo(message.chat.id, 'https://ibb.co/rQBXP7B', 'Дылгыров Булат - председатель культурно-массового сектора')
        bot.reply_to(message, 'Культурно-массовый сектор занимается организацией культурно-массовых мероприятий, а также подготовкой и репетициями к ним\n\nСостав культурно-массового сектора:\nДылгыров Булат\nПерменов Максим\nАртёмова Мария\nКрасников Кирилл\nЯнхаев Данил\nШевченко Кирилл\nАтласова Валерия\nХандарова Александра\nКустов Владислав')

    elif message.text == 'Спортсектор':
        bot.send_photo(message.chat.id, 'https://ibb.co/pjMxxkP', 'Каминский Марк - председатель спортсектора')
        bot.reply_to(message, 'Спортивный сектор занимается организацией спортивных мероприятий, собирает сборную общежития\n\nСостав спортсектора:\nКаминский Марк\nГончаренко Дмитрий\nЗапруто Евгений\nМанханов Мэргэн')

    elif message.text == 'Редколлегия':
        bot.send_photo(message.chat.id, 'https://ibb.co/pJhj7FY', 'Спиридонов Евгений - председатель редколлегии')
        bot.reply_to(message, 'Редакционная коллегия занимается творческими делами, создавая украшения, наряды, стенды и фотозоны для мероприятий, проводимых в общежитии\n\nСостав редколлегии:\nСпиридонов Евгений\nАлёшина Дарья\nНикитин Игорь\nСенотрусова Дарья')

    elif message.text == 'Сантройка':
        bot.send_photo(message.chat.id, 'https://ibb.co/GdyhSg0', 'Бельков Кирилл - председатель сантройки')
        bot.reply_to(message, 'Санитарный сектор следит за чистотой и порядком в общежитии, проверяя каждую неделю комнаты проживающих, а также проводя акции, связанные с гигиеной, экологией\n\nСостав сантройки:\nБельков Кирилл\nПеревалова Анна\nРоманова Мария\nЦымпилова Уржина\nСеменников Тимур\nПерелыгин Олег\nКармышев Дмитрий')
bot.polling(none_stop=True, interval=0)
