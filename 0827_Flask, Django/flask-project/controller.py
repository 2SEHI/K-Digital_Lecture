from flask import Flask, request, render_template, redirect
# model.py 임포트
import model

app = Flask(__name__)

from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureConvas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

@app.route('/')
def index():
    dao = model.Dao()
    data = dao.selectall()

    # 읽어온 데이터를 가지고 데이터프레임을 생성
    df = pd.DataFrame(data)
    # matplotlib은 반드시 별도의 스레드로 실행되어야 합니다.
    # 이 구문을 삽입하면 matplotlob이 별도의 스레드로 실행됩니다.
    matplotlib.use('agg')

    fig = plt.figure(figsize=(8, 6))
    sns.set()
    sns.set_style('whitegrid')
    sns.set_color_codes()
    sns.barplot(x='itemname', y='price', data=df)
    fig.savefig('static/img/graph.png')

    return render_template('index.html', data=data)


@app.route('/detail/<itemid>')
def detail(itemid):
    dao = model.Dao()
    data = dao.getitem(itemid)
    # detail.html 파일에 item이라는 이름으로 data를 넘겨줍니다.
    return render_template('detail.html', item=data)


# @app.route('/insert')
# def insert():
#     return render_template('insert.html')

@app.route('/insert', methods=['POST', 'GET'])
def insert():
    if request.method == 'GET':
        return render_template('insert.html')
    else :
        f = request.files['pictureurl']
        f.save('./static/img/' + f.filename)

        item = {}
        item['itemname'] = request.form['itemname']
        item['price'] = request.form['price']
        item['description'] = request.form['description']
        item['pictureurl'] = f.filename
        dao = model.Dao()
        dao.insertitem(item)
    return redirect('/')

from flask import send_file
@app.route('/plot')
def plot():
    dao = model.Dao()
    data = dao.selectall()
    df = pd.DataFrame(data)

    matplotlib.use('agg')
    fig, axis = plt.subplots(1)
    sns.set()
    sns.set_style('whitegrid')
    sns.set_color_codes()
    sns.barplot(x='itemname', y='price', data=df)
    # 그려진 img 파일 내용을 html 랜더링 쪽에 전송합니다
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')

import json
@app.route("/data")
def data():
    # 그래프를 그릴 데이터를 지정
    x = ['2018-02-10', '2018-02-11', '2018-02-12', '2018-02-13', '2018-02-14']
    y = [15000, 23000, 20000, 22000, 25000]
    # 리스트를 json 데이터로 변환
    return json.dumps([{"date": x[i], "close": y[i]} for i in range(5)])

# d3를 호출했을 때의 탬플릿을 설정
@app.route("/d3")
def showsample():
    return render_template("d3.html")

app.run(host='0.0.0.0', debug=True)