LEXICON_COMMANDS: dict[str, str] = {
    '/start': 'МОЙ КАБИНЕТ',
    '/admin': 'АДМИНКА',
    '/help': 'ПОМОЩЬ',
}

LEXICON_HI = {"привет", "здорова", "хай", "приветствую", "добрый день", "здравствуйте", "здрасти", "hi", "hello",
              "good morning", "good day"}

restricted_words = {'дурак', 'осел', 'болван', 'пидор', 'сидор', 'хуй'}

LEXICON_RU: dict[str, str] = {
    '/help': 'Тебе доступны команды:\n'
             '/start - запуск бота.\n'
             '/help - список команд.\n'
             '/description - описание бота.\n'
             '/insta_links - список ссылок на каналы instagram.\n'
             '/tiktok_links - список ссылок на каналы TikTok.\n'
             'Ты можешь воспользваться основным меню!\n'
             '👇👇👇 Меню.'
    ,
    '/admin+panel': '<b>Административная панель.</b>\nТы можешь добавить/изменить/удалить услуги, баннеры, КП, заметки и документы.'
    ,
    'no_echo': 'Данный тип апдейтов не поддерживается '
               'методом send_copy',
}

LEXICON_btn_help: dict[str, str] = {
    "Инструкция для админки📄": "adm_panel_instruction",
    "Связь с администратором📞": "adm_connect",
    "Общая информация🪬": "main_information",
}

LEXICON_btn_main_admin_menu: dict[str, str] = {
    "Инструкция для админки": "instruction_admin",
    "Создать услугу": "add_product",
    "Изменить услугу": "products_list",
    "Создать КП": "add_offer",
    "Изменить КП": "offers_list",
    "Создать FAQ": "add_faq",
    "Удалить FAQ": "faq_list",
    "Создать заметку": "add_note",
    "Удалить заметку": "note_list",
    "Добавить прайс": "add_price",
    "Удалить прайсо": "price_list",
    "Добавить документ": "add_docoment",
    "Удалить документ": "documents_list",
    "Создать категрию": "add_category",
    "Удалить категрию": "category_list",
    "Баннер.Добав/измен.": "add_change_banner",

}

LEXICON_btn_menu: dict[str, str] = {
    "Мои услуги": "products_list",
    "Готовые КП": "offers_list",
    "FAQ": "faq_list",
    "Мои заметки": "note_list",
    "Мои прайсы": "price_list",
    "Мои документы": "documents_list",
}

LEXICON_btn_add_offer: dict[str, str] = {
    "Next": "next_offer",
    "ADD": "add_to_offer",
    "Back": "previos_offer",
    "Смотреть КП": "products_in_offer",
    "Сохранить КП": "generate_offer",
}

LEXICON_btn_employee_menu: dict[str, str] = {
    'tables_links': 'Рабочие таблицы',
    'work_links': 'Рабочие ссылки',
    'offer_online': 'Создать КП',
    'admin': 'Админка',
}
