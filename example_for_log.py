import logging

from logging.handlers import RotatingFileHandler

# Здесь задана глобальная конфигурация для всех логгеров
logging.basicConfig(
    level=logging.DEBUG,
    filename='program.log',
    encoding="UTF-8",
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s'
)
# А тут установлены настройки логгера для текущего файла - example_for_log.py
logger = logging.getLogger(__name__)
# Устанавливаем уровень, с которого логи будут сохраняться в файл
logger.setLevel(logging.INFO)
# Указываем обработчик логов
handler = RotatingFileHandler('my_logger.log',
                              maxBytes=50000000,
                              backupCount=5)
logger.addHandler(handler)

logging.debug('123')  # Когда нужна отладочная информация
logging.info('Сообщение отправлено')  # Когда нужна дополнительная информация
logging.warning('Большая нагрузка!')  # Когда что-то идёт не так, но работает
logging.error('Бот не смог отправить сообщение')  # Когда что-то сломалось
logging.critical('Всё упало! Зовите админа!1!111')  # Когда всё совсем плохо
