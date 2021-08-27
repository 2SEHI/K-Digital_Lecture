import pymysql

class Dao:
    # 데이터베이스 접속 메소드
    def connect(self):
        self.con = pymysql.connect(host='localhost',
                                   port=3306,
                                   user='root',
                                   password='1234',
                                   db='adam',
                                   charset='utf8')
        self.cursor = self.con.cursor()

    # 데이터베이스 연결을 해제하는 메소드
    def close(self):
        self.con.cursor()


    # 테이블의 전체 데이터를 가져오는 메소드
    def selectall(self):
        # 데이터베이스 접속 연결
        self.connect()
        print(self.connect)
        # 수행할 SQL 문장을 생성
        self.cursor.execute('select * from item')
        # 실행
        data = self.cursor.fetchall()

        li = []
        # 읽어온 결과를 순회하면서
        for imsi in data:
            # 첫번째와 두번째 세번째 컬럼을 dict에 저장
            dic = {}
            dic['itemid'] = imsi[0]
            dic['itemname'] = imsi[1]
            dic['price'] = imsi[2]
            # dict를 list에 저장
            li.append(dic)
        # 데이터베이스 접속 해제
        self.close()
        
        return li

    # itemid를 받아서itemid에 해당하는 데이터를 찾아서 리턴하는 메소드
    def getitem(self, itemid):
        # 데이터베이스 연결
        self.connect()

        #itemid를 가지고 데이터를 찾아오는 sql을 생성
        self.cursor.execute('select * from item where itemid=%s',
                            itemid)
        
        # sql을 실행해서 결과를 tuple의 형태로 저장
        data = self.cursor.fetchone()

        # 찾아온 데이터를 dict로 변환
        # list와 tuple은 숫자로된 인덱스로 접근
        # dict는 키로 접근
        # 번호를 입력하는 것보단 이름(key)로 기억하는 것이 쉽습니다.
        dic = {}
        dic['itemid'] = data[0]
        dic['itemname'] = data[1]
        dic['price'] = data[2]
        dic['description'] = data[3]
        dic['pictureurl'] = data[4]
        self.close()

        return dic

    # dict형태로 데이터를 받아서 삽입하는 메소드
    def insertitem(self, item):
        self.connect()
        # 가장 큰 itemid를 가져와서 1을 더해서 itemid를 생성
        self.cursor.execute('select max(itemid) from item')
        data = self.cursor.fetchone()
        # 데이터가 없어서 예외가 발생할 경우를 대비하여 try except문으로 예외처리를 해줍니다.
        try :
            itemid = int(data[0] + 1)

        except :
            itemid = 1

        # 데이터를 삽입하는 sql을 실행
        self.cursor.execute('insert into item values(%s, %s, %s, %s, %s)',
                            (itemid, item['itemname'], item['price'],
                             item['description'], item['pictureurl']))
        # 삽입한 데이터를 데이터베이스에 반영
        self.con.commit()
        # 데이터베이스 접속 해제
        self.close()



