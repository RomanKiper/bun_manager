from aiogram import types, Router, F, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import CallbackQuery, InlineKeyboardButton, Message
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.models import Banner
from database.orm_query import orm_get_faqs, orm_get_faq, orm_add_user, orm_increment_handler_counter
from bun_manager_bot.filters.chat_types import ChatTypeFilter
from bun_manager_bot.lexicon.lexicon import LEXICON_HI, LEXICON_btn_menu
from bun_manager_bot.keyboards.inline.inline_btns import get_callback_btns

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))



@user_private_router.message(F.text.lower().in_({'старт', 'начать', "start"}))
@user_private_router.message(CommandStart())
@user_private_router.callback_query(lambda c: c.data.startswith("main_menu"))
async def start_cmd(message_or_callback: types.Union[types.Message, CallbackQuery], session: AsyncSession):
    if isinstance(message_or_callback, types.Message):
        message = message_or_callback
        await orm_add_user(session,
                           user_id=message.from_user.id,
                           username=message.from_user.username,
                           first_name=message.from_user.first_name,
                           last_name=message.from_user.last_name,
                           )
        await orm_increment_handler_counter(session,
                                            user_id=message.from_user.id,
                                            handler_name='start',
                                            username=message.from_user.username,
                                            first_name=message.from_user.first_name,
                                            last_name=message.from_user.last_name,
                                            )
        query = select(Banner).where(Banner.name == 'main')
        result = await session.execute(query)
        banner = result.scalar()
        await message.answer_photo(photo=banner.image,
                                   caption=banner.description,
                                   reply_markup=get_callback_btns(btns=LEXICON_btn_menu, sizes=(1,)))
        await message.delete()
    elif isinstance(message_or_callback, CallbackQuery):
        # Если это колбэк-запрос
        callback = message_or_callback
        await orm_add_user(session,
                           user_id=callback.message.from_user.id,
                           username=callback.message.from_user.username,
                           first_name=callback.message.from_user.first_name,
                           last_name=callback.message.from_user.last_name,
                           )
        query = select(Banner).where(Banner.name == 'main')
        result = await session.execute(query)
        banner = result.scalar()
        await callback.message.answer_photo(photo=banner.image,
                                   caption=banner.description,
                                   reply_markup=get_callback_btns(btns=LEXICON_btn_menu, sizes=(1,)))
        await callback.message.delete()


@user_private_router.message(F.text.lower().in_({'помощь', "help"}))
@user_private_router.message(Command('help'))
async def help_cmd(message: types.Message):
    await message.answer(text="Сделайте выбор:", reply_markup=get_callback_btns(btns=LEXICON_btn_help, sizes=(1,)))


@user_private_router.message(F.text.lower().in_(LEXICON_HI))
async def hi_cmd(message: types.Message):
    await message.answer("И тебя приветствую!")

# @user_private_router.message()
# async def send_echo(message: Message):
#     try:
#         if message.photo:
#             await message.send_copy(chat_id=message.chat.id)
#             photo_id = message.photo[0].file_id
#             await message.answer(f"ID фотографии: {photo_id}")
#         elif message.video:
#             await message.send_copy(chat_id=message.chat.id)
#             video_id = message.video.file_id
#             await message.answer(f"ID видео: {video_id}")
#     except TypeError:
#         await message.reply(text=LEXICON_RU['no_echo'])
