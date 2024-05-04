from flask import Flask,render_template,request,url_for,jsonify

app = Flask(__name__)


@app.route('/getList')
def getMenuItem():
    data = request.json
    print(data)
    return jsonify({'ok' : '200'})

if __name__ == '__main__':
    app.run(debug=True)