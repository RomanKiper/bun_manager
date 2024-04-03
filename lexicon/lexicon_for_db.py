from aiogram.utils.formatting import Bold, as_list, as_marked_section


categories = ['Инстаграм', 'Тикток', 'Сайт', 'Телеграм']

#
# main_advertising = ['Сайт/реклама', 'Сайт/акция', 'Instagram', 'Telegram', 'TikTok',
#                     'Приложение', 'Регионы/сайт', 'Регионы/сети' 'Обзоры/примеры']



description_for_info_pages = {
    "main": 'Я Bun_bot😎! Ты в главном меню.\n',
    "about": "Пиццерия Такая-то.\nРежим работы - круглосуточно.",
    "contacts_main": 'Контакты организации.',
    "shipping": as_list(
        as_marked_section(
            Bold("Варианты доставки/заказа:"),
            "Курьер",
            "Самовынос (сейчас прибегу заберу)",
            "Покушаю у Вас (сейчас прибегу)",
            marker="✅ ",
        ),
        as_marked_section(Bold("Нельзя:"), "Почта", "Голуби", marker="❌ "),
        sep="\n----------------------\n",
    ).as_html(),
    'catalog': 'Категории:',
    'cart': 'В корзине ничего нет!'
}