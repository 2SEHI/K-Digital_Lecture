from flask import Flask, request, render_template, jsonify
# 플라스트 애플리케이션 생성
app = Flask(__name__)

# @app.route('/')
# def main():
#     return 'Hello Flask!'

# / 요청이 오면 처리하는 코드
# / 요청은 도메인과 포트 번호까지만 입력된 경우
@app.route('/')
def main():
    # templates 디렉토리에 있는 파일을 출력
    return render_template('index.html')
#
# @app.route('/sports')
# def sports():
#     return '스포츠 페이지'
#
# # <변수>값 가져오기
# @app.route('/bloter/<title>')
# def bloter(title):
#     return title
#
# @app.route('/tistory/<int:num>')
# def tistory(num):
#     return str(num)

# @app.route('/search')
# def search():
#     # get방식으로 전송된 데이터가 form에 있더라도 request.form[]이 아닌 request.args[]라고 써줘야 합니다.
#     keyword = request.args['keyword']
#     return keyword


# get방식의 요청과 post방식의 요청을 모두 처리
@app.route('/search', methods=['GET', 'POST'])
def search():
    # get방식의 요청을 처리
    if request.method == 'GET':
        keyword = request.args['keyword']
        return keyword
    else :
        # post방식의 요청을 처리
        keyword = request.form['keyword']
        return keyword

# 파일 업로드
@app.route('/upload', methods=['GET', 'POSt'])
def upload():
    # 업로드 파일 가져오기
    f = request.files['file']
    # 업로드 파일 저장
    # 받은 파일을 저장하고 싶으면 save안에 파일이름 설정
    f.save(f.filename)
    return f.filename + '업로드 성공'

@app.route('/json')
def json():
    data = [{'name':'adam', 'age':23}, {'name':'rusia', 'age':22}]
    return jsonify(data)

@app.route('/xml')
def xml():
    data = '<persons>'
    data += '<person><name>adam</name><age>23</age></person>'
    data += '<person><name>rusia</name><age>22</age></person>'
    data += '</persons>'
    return data, {'Content-Type':'text/xml'}


# 서버에서 html에 데이터 넘기기
@app.route('/script')
def script():
    msg = 'Hello Flask'
    dict1 = {'name':'태연', 'age':30}
    dict2 = {'name': '수지', 'age': 25}
    li = [dict1, dict2]
    return render_template('script.html', msg = msg, data=li)


# 서버를 테스트 용으로 실행
# host를 127.0.0.1로 작성하면 로컬에서만 접속이 가능
# 0.0.0.0 으로 작성하면 모든 곳에서 접속이 가능합니다.
# port를 생략하면 5000번 포트를 할당합니다.
# Threaded 를 True로 설정하면 스레드로 요청을 처리합니다.(스레드는 동시에 여러 클라이언트 처리가능)
# 개발을 할 때는 debug를 True로 설정하지만 운영을 할 때는 반드시 False로 변경합니다.
app.run(host = '0.0.0.0', debug=True)
