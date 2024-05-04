from flask import Flask, render_template,jsonify
from database import get_items
from suffle import make_menu


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/makeMenu')
def get_menu():
    items = get_items()
    week_end = [item[1] for item in items if item[2] == 'WE']
    week_day = [item[1] for item in items if item[2] == 'WD']
    
    menu = make_menu(week_end,week_day)

    return render_template('menu.html',menu = menu)

if __name__ == '__main__':
    app.run(debug=True)
