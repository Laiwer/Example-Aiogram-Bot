<h1 align=center>Шаблон для телеграм бота на Aiogram версии 2.x</h1>
Этот репозиторий - шаблон, который я взял у одного ютубера очень давно, даже не помню у кого и перезалил себе на гитхаб. В последнем комите я переработал шаблон под себя, чтобы мне было удобно писать код. Со временем я буду дополнять этот репозиторий. 

## Содержание
* Папки
  * config
  * database
  * handlers
  * keyboards
  * states
  * utils
* Файлы
  * app.py
  * loader.py

## Папки
### config
Папка с данными, которые использует бот, например токен бота и айди админа или словарь с данными, которые использует бот в разных частях кода, как у бота [Mini-Games Bot](https://github.com/Laiwer/Mini-Games_Bot/tree/main/data). Токен бота хранится в файле **.env**, но **.gitignore** специально сделан для того, чтобы этот файл не попал на гитхаб, поэтому в репозитории хранится файл **.env.dist**. С помощью библиотеки [envirions](https://pypi.org/project/environs/) в **data_config.py** мы получаем данные из **.env** и в дальнейшем их используем. Кстати, вы можете ввести не только один айди админа, а несколько, то есть админов бота может быть много.
### database
Здесь должны хранится все файлы связанные с базой данных. Для примера здесь уже создан пустой файл **base.py**. Я пока что работал только с SQL через [sqlite3](https://docs.python.org/3/library/sqlite3.html). Но в дальнейшем я поработаю с другими базами данных. Обещаю.
### handlers
Здесь хранятся четыре основных папки, которые обрабатывают все входящие события от TelegramAPI.

Папка **errors** нужна для обработки ошибок, которые прилетают от TelegramAPI.

Папка **channel** нужна для функций, которые будут отправлять сообщения в телеграм каналы или как-то с ними взаимодействовать.

Папка **groups** нужна для работы с группами.

Папка **users** используется чаще всего. Эта папка в которой хранятся функции, которые должны работать в личных сообщениях с ботом. Также здесь должны хранится файлы для работы бота в [Inline mode](https://core.telegram.org/bots/features#inline-requests).
### keyboards
Папка **default** хранит клавиатуры вида [ReplyKeyboardMarkup](https://docs.aiogram.dev/en/v2.25.1/telegram/types/reply_keyboard.html?highlight=ReplyKeyboardMarkup) и все их кнопки.

Папка **inline** хранит клавиатуры вида [InlineKeyboardMarkup](https://docs.aiogram.dev/en/v2.25.1/telegram/types/inline_keyboard.html?highlight=InlineKeyboardMarkup) и все их кнопки.

Папка **callback** хранит [callback_query](https://core.telegram.org/bots/api#callbackquery) клавиатур вида [InlineKeyboardMarkup](https://docs.aiogram.dev/en/v2.25.1/telegram/types/inline_keyboard.html?highlight=InlineKeyboardMarkup).

### states
Здесь хранятся файлы, которые связанны с машиной состояний FSM ([пример](https://docs.aiogram.dev/en/v2.25.1/examples/finite_state_machine_example.html?highlight=state)).

### utils
Здесь хранятся файлы, которые не использует телеграм бот, но они важны, например логирование. В файле **notify_admins.py** нужен для уведомления админа бота о том, что бот либо запустился, либо отключился. В файле **set_bot_commands.py** хранятся меню кнопок, то есть команды, которые будут отображаться при вводе "/" ([пример](https://core.telegram.org/file/464001555/10fbd/jvTuV2Ke7WQ.1916669.mp4/a056de323645db409d)). В папке **misc** хранятся файлы связанные с логированием.

## Файлы
### app.py
Это основной файл бота. Его нужно запускать для начала работы бота. В нём хранятся две интересные функции. Первая функция (**on_startup**) срабатывает, когда бот запускается, а вторая (**on_shutdown**) - когда выключается. На этом и основано уведомление админу о запуске/выключении бота из файла **utils/notify_admins.py**.
В
### loader.py
Название этого файла указывается на его предназначение. Этот файл загружает объект **Bot**, импортируя токен бота. Также загружает объект **Dispatcher** ([Что это такое?](https://docs.aiogram.dev/en/v2.25.1/dispatcher/index.html?highlight=dispatcher#dispatcher-class))