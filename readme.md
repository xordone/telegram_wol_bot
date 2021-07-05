# Установка
```
git clone https://github.com/xordone/telegram_wol_bot.git
```
Я использую менеджер зависимостей 
[poety](https://python-poetry.org), если вы тоже его используете то выполняем
```
cd telegram_wol_bot
poetry install
```
Либо по-старинке 
```
pip install -r requirements.txt
```

# Запуск
Запускаю через systemd
создаем файл /etc/systemd/system/telegram_wol_bot.service
```
Unit]
Description=TelegramBot
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 путь до файла bot.py

[Install]
WantedBy=multi-user.target
```
и включаем сервис
```
systemctl enable telegram_wol_bot.service
```


# PS
Буду очень рад любому предложению или замечанию.