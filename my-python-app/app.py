# Импортируем класс Flask из библиотеки flask
from flask import Flask
from datetime import datetime
import pytz

# Создаем экземпляр класса Flask. __name__ - это имя текущего модуля.
app = Flask(__name__)

# Декоратор @app.route('/') определяет маршрут (URL-адрес) для корневой страницы сайта.
# Когда пользователь заходит на этот адрес, вызывается функция hello_world().
@app.route('/')
def hello_world():
    # Функция возвращает строку, которую браузер пользователя отобразит на странице.
    # Vladivostok: Asia/, Новосибирск Asia/Novosibirsk, Москва Europe/Moscow
    tz = pytz.timezone('Asia/Vladivostok')
    now_utc = datetime.utcnow()
    local_dt = now_utc.replace(tzinfo=pytz.utc).astimezone(tz)
    date_str = local_dt.strftime("%Y-%m-%d")
    weekday_str = local_dt.strftime("%A")  # День недели на английском, например: Monday
    time_str = local_dt.strftime("%H:%M:%S")
    return (
        f'Hello, World from Docker!<br>'
        f'Today is {date_str}<br>'
        f'Day of the week: {weekday_str}<br>'
        f'Your local time: {time_str}'
    )
# Этот блок кода выполняется только если скрипт запущен напрямую (а не импортирован как модуль).
if __name__ == '__main__':
    # Запускаем встроенный сервер разработки Flask.
    # debug=True: включает режим отладки (не использовать в продакшене!).
    # host='0.0.0.0': сервер будет доступен не только локально, но и снаружи контейнера.
    # port=8080: сервер будет слушать на порту 8080.
    app.run(debug=True, host='0.0.0.0', port=8080)