import pymysql

class Dao:
    #  데이터베이스 연결 메소드
    def connect(self):
        # 연결
        self.con = pymysql.connect(host='localhost',
                                   port=3306,
                                   user='sehi',
                                   passwd='1234',
                                   db='sehidb',
                                   charset='utf8')
        # 데이터베이스 사용 객체 생성
        self.cursor = self.con.cursor()

    # 데이터베이스 연결 해제 메소드
    def close(self):
        self.con.close()
    
    # 전체 데이터 가져오기
    def selectall(self):
        # 데이터베이스 연결
        self.connect()

        # sql 문 실행
        self.cursor.execute("select * from item")

        data = self.cursor.fetchall()

        # 데이터를 저장할 list
        li = []

        for temp in data:
            dic = {}
            dic['item'] = temp[0]
            dic['itemname'] = temp[1]
            dic['price'] = temp[2]
            dic['description'] = temp[3]
            dic['pictureurl'] = temp[4]
            li.append(dic)
        self.close()
        return li

    # 데이터 삽입을 위한 메소드
    # item은 dict
    def insertitem(self, item):
        # itemid를 생성
        self.connect()
        # item테이블에서 가장 큰 itemid를 가져옴
        self.cursor.execute('select max(itemid) from item')
        data = self.cursor.fetchone()
        # 데이터가 존재하는 경우, 가장 큰 itemid에 +1 증가
        if data[0] != None:
            itemid = int(data[0]) + 1

        # 결과를 저장할 변수
        result = False

        try:
            self.cursor.execute('insert into item values(%s, %s, %s, %s, %s)',
                                (itemid, item['itemname'], item['price'],
                                 item['description'], item['pictureurl']))

            # 성공 여부를 확인 - rowcount는 영향받은 행의 개수
            if self.cursor.rowcount >= 1:
                result = True
        except Exception as e:
            # insert 실패시 False 반환
            result = False
        self.con.commit()
        self.close()
        return result
            
            
        