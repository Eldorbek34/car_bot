from aiogram.utils.keyboard import ReplyKeyboardBuilder


def reply_send_phone_number():
    reply_keyboard = ReplyKeyboardBuilder()

    reply_keyboard.button(text="Send phone", request_contact=True)

    return reply_keyboard.as_markup(resize_keyboard=True)


def reply_main_menu():
    reply_keyboard = ReplyKeyboardBuilder()

    reply_keyboard.button(text="Yangi detektsiya yaratish")
    reply_keyboard.button(text="Faol detektsiyalar")
    reply_keyboard.button(text="Sozlamalar")

    reply_keyboard.adjust(2)

    return reply_keyboard.as_markup(resize_keyboard=True)


def reply_new_detections():
    reply_keyboard = ReplyKeyboardBuilder()

    reply_keyboard.button(text="Deteksiya yaratish")
    reply_keyboard.button(text="Filter qo'shish")
    reply_keyboard.button(text="Bosh menuga qaytish")

    reply_keyboard.adjust(2)

    return reply_keyboard.as_markup(resize_keyboard=True)