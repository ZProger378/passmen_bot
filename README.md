# passmen_bot

Это просто, но безопасный парольный менеджер прямо в телеграмм, выполненный в виде бота.

Для доступа ко всем своим паролям нужен мастер-пароль, который хранится в виде хеша, созданным алгоритмом sha512 с длинной солью.
Алгоритм соли для каждого пользователя генерируется отдельно их хранится в config.json
Бот не хранит своих пользователей, для отличия одних пользователей от других используется также алгоритм хеширования.

База данных и файл конфига, который для каждого пользователя индивидуальный, зашифрован симметричным алгоритмом AES, в качестве ключа шифрования используется тот самый мастер-пароль.
А в момент открытия сессия база расшифровывается, но даже в расшифрованном виде, основные данные (логин и пароль) зашифрованы.
После работы с базой сессию нужно закрыть, тогда база данных снова зашифровывается.

Бот соответвует изначальным требованиям, однако есть придирка. Я не знаю, вина ли это алгоритма AES или самой библиотеки pyAesCrypt, но шифрование и расшифровка файлов довольно долгое, это видно по задержке между открытием или закрытием сессию и сообщения, в котором говорится, сессия открыта или закрыта.


Рабочий пример бота: https://t.me/passmen_bot

ВНИМАНИЕ!!! Во избежание кражи данных, используйте только этого бота или поднятого вами из этого исходного кода