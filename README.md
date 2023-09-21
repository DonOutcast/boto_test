# Simple aiogram bot

<h4>Реализованная функциональность</h4>
<ul>
   <li>Бот должен быть реализован на языке Python с использованием библиотеки aiogram.</li>
    <li>Бот должен быть оформлен в виде отдельного модуля или пакета.</li>
    <li>Бот должен быть устойчив к ошибкам пользователя и корректно обрабатывать исключительные ситуации</li>
    <li>Код бота должен быть чистым, асинхронным, хорошо организованным и содержать комментарии, объясняющие логику работы.</li>
    <li>Бот должен успешно выполнять все описанные функции.</li>
</ul> 
<h4>Особенность проекта в следующем:</h4>
<ul>
 <li>Написан на языке Python3.10</li>
 <li>При помоши фраймворка aiogrm3.x</li>
</ul>
<h4>Основной стек технологий:</h4>
<ul>
    <li>Python, Aiogram, Asyncio</li>
	<li>HTML, CSS</li>
    <li>Github, Docker</li>

</ul>




СРЕДА ЗАПУСКА
------------

1) Наличие файла .env.
2) Получить токен у BotFather.
4) Получть токен у OpenWeather.
5) требуется установленная python 3.8+.

# Запуск

Контейнеризация
------------

1) Убедитесь что у вас установлен Docker.
2) Убедитесь что у вас имеется утилта Makefile.

~~~
make
...
~~~

Вручную
------------

1) Переиминовать env_exmaple в.env.
2) Получить токен у BotFather.
3) Добавить в .env в BOT_TOKEN = токен из BotFather.
4) Получить токен у OpenWeather.
5) Добавить в .env в OPENWEATHER_TOKEN = токен из OpenWeather.
5) Требуется установленная python 3.8+.
6) После чего перейдите в дирикторию src/telegram_bot/ и выполните комманду ниже

Unix

~~~
python3 __main__.py
...
~~~

Windows

~~~
python __main__.py
...
~~~

Также вы можите написать свой ID в поле ADMINS для того чтобы бот отправлял вам уведомление

РАЗРАБОТЧИКИ

<h4>Айдин Шамиль fullstack https://t.me/Hard_Wolf_l </h4>