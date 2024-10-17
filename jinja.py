from flask import Flask, render_template

app = Flask(__name__)




@app.route('/')
def html():
    context = {
        'caption' : 'Наши в космосе',
        'link' : 'Переход на сайт'
    }

    return render_template('index.html', **context)

@app.route('/shablon/')
def html2():
    context = {
        'caption': 'Юра, мы все... живем в космосе',
        'link': 'Подробнее'
    }

    return render_template('index.html', **context)

if __name__ == '__main__':
    app.run()