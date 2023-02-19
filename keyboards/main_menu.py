from aiogram import Dispatcher, types


# Функция для настройки кнопки Menu бота
async def set_main_menu(dp: Dispatcher):
    main_menu_commands = [
        types.BotCommand(command='/restart', description='Перезапуск бота'),
        types.BotCommand(command='/help', description='Справка по работе бота')
    ]
    await dp.bot.set_my_commands(main_menu_commands)
