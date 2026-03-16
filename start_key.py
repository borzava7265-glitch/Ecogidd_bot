from aiogram import types


button_recyclable = types.KeyboardButton(text='/recyclable')
button_hazardous = types.KeyboardButton(text='/hazardous')
button_clothes = types.KeyboardButton(text='/clothes')
button_ecochem = types.KeyboardButton(text='/ecochem')
button_ecotips = types.KeyboardButton(text='/ecotips')
button_ecotour = types.KeyboardButton(text='/ecotour')
button_help = types.KeyboardButton(text='/help')

button_recyclable_ru = types.KeyboardButton(text='Вторсырье')
button_hazardous_ru = types.KeyboardButton(text='Батарейки')
button_clothes_ru = types.KeyboardButton(text='Одежда')
button_ecochem_ru = types.KeyboardButton(text='Экохимия')
button_ecotips_ru = types.KeyboardButton(text='Экосоветы')
button_ecotour_ru = types.KeyboardButton(text='Экотуризм')


kb = [
    [button_hazardous, button_recyclable],
    [button_clothes, button_ecochem],
    [button_ecotips, button_ecotour],
    [button_help]
]

kb_ru = [
    [button_hazardous_ru, button_recyclable_ru],
    [button_clothes_ru, button_ecochem_ru],
    [button_ecotips_ru, button_ecotour_ru],
    [button_help]
]
keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
keyboard_ru = types.ReplyKeyboardMarkup(keyboard=kb_ru, resize_keyboard=True)






