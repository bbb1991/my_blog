# coding=utf-8
from flask import Flask

app = Flask(__name__)

# Не знаю почему но если импорт находится
# наверху, крашится с ошибкой ImportError: cannot import name app
import views