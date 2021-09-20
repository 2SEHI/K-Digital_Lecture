# flask 웹 서버를 만들기 위해서 필수
from flask import Flask, request
from flask import send_file
from flask import render_template

# 앱 생성
app = Flask(__name__)

# 요청 과 요청을 받으면 처리할 함수를 생성
# 포트번호까지의 요청이 오면 templates 디렉토리의 index.html을 출력
@app.route('/')
def index():
    return render_template('index.html')

import db
from flask import jsonify
@app.route('/item')
def item():
    dao = db.Dao()
    data = dao.selectall()
    # 출력의 형태 : json
    response = {'result':True, 'data':data}
    return jsonify(response)

# 파일 다운로드
@app.route('/imagedownload/<pictureurl>')
def imagedownload(pictureurl):
    file_name = 'static/img/' + pictureurl
    print(file_name)
    # file_name : 실제 파일의 경로(server쪽)
    # mimetypes : 파일의 종류
    # attachment_filename : 다운로드 되었을 때의 파일 이름(client쪽)
    return send_file(file_name, mimetype='application/octect-stream',
                     attachment_filename=pictureurl,
                     as_attachment =True)

@app.route('/insert', methods=['POST'])
def insert():
    # 전송 방식이 post일 경우
    if request.method == 'POST':
        # DAO 에 넘겨줄 매개변수
        item = {}
        # Android가 아닌 server에서 구현을 한다면
        # 클라이언트에서 넘어온 파일 가져오기
        f = request.files['pictureurl']

        if f != None:
            f.save('./static/img/' + f.filename)
            item['pictureurl'] = f.filename

        # 나머지 파라미터를 읽어서 저장
        # 앞의 이름을 Dao에게 넘겨줄 때 이름
        # 뒤의 이름은 클라이언트가 데이터를 보낼 때 이름과 같아야 하며,
        #             Android에서 보낸 이름과도 같아야 합니다.
        item['itemname'] = request.form['itemname']
        item['price'] = request.form['price']
        item['description'] = request.form['description']
        
        # 데이터베이스에 삽입
        dao = db.Dao()
        result = dao.insertitem(item)
        # 응답생성 : result는 클라이언트가 읽어야할 이름 
        # 성공하면 True, 실패하면 False
        response = {'result' : result}
    # json 형태의 데이터로 생성해서 결과를 리턴
    return jsonify(response)


# 자신의 IP로 접속할 수 있도록 서버를 구동
# 회사 내에서만 접속가능하게 하고 싶다면 host를 변경
app.run(host='0.0.0.0', debug=True)