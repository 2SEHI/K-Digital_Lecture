from socket import *
try:
    # TCP 서버 소켓을 생성
    svrsock = socket(AF_INET, SOCK_STREAM)
    # 서버를 바인딩 - 서버를 실행시켜서 클라이언트가 접속할 수 있도록 하는 것
    # 포트 번호가 하나의 프로세스가 됨

    svrsock.bind(('자신의 ip', 8000))
    # 서버가 받아들일 수 있는 클라이언트 수(BackLog)를 설정
    svrsock.listen(1)
    while True:
        print('서버 대기 중...')
        # 클라이언트의 요청이 있으면 연결
        conn, addr = svrsock.accept()
        # 클라이언트 정보 출력
        print(addr)
        # 1024는 330글자 정도까지 받을 수 있음
        b = conn.recv(1024)
        # 클라이언트에게 메시지 전송
        conn.send('안녕하세요 안드로이드'.encode())
        # 보낸 메시지 확인
        print(b.decode())
        # 연결 해제
        conn.close()
except Exception as e:
    print('예외 발생 : ', e)
finally:
    print('종료되면 무조건 수행')
