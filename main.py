from flask import Flask, render_template

app = Flask(__name__)

    #Ввод переменной в URL с выводом на экран
# @app.route('/')
# @app.route('/<name>/')
# def hello_world(name='Незнакомец'):
#     return f'Привет, {name}!'


    #Переход на новую страницу по разным URL
# @app.route('/newpage/')
# @app.route('/new/')
# @app.route('/новаястраница/')
# def new():
#     return 'New page'

    #Проверка паролей
# @app.route('/')
# @app.route('/<password>/')
# def check_pass(password=None):
#     if password == '1234':
#         return 'Password is correct'
#     else:
#         return 'Password is not correct'


    #Вывод на экран с помощью HTML
# @app.route('/')
# def html():
#     html = """
#     <h1>Добро пожаловать</h1>
#     <p>на сайт</p>
#     """
#     return html

@app.route('/')
def html():

    return render_template('home.html')



if __name__ == '__main__':
    app.run()