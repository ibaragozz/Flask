from flask import Flask
from datetime import datetime
app = Flask(__name__)
#Создайте новое приложение Flask, которое будет отображать текущие дату и время на главной
@app.route('/')
def time():

    return f'Current time is {datetime.now()}'


if __name__ == '__main__':
    app.run()