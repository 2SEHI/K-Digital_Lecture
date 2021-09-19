from socket import *

try:
    # TCP 서버 소켓을 생성
    sock = socket(AF_INET, SOCK_STREAM)
    # 서버를 바인딩 - 서버를 실행시켜서 클라이언트가 접속할 수 있도록 하는 것
    # 포트 번호가 하나의 프로세스가 됨
    # TODO Server쪽 IP로 수정할 것
    sock.connect(('Server쪽 IP', 8000))

    msg = input("보낼 메시지:")
    # 서버가 받아들일 수 있는 클라이언트 수(BackLog)를 설정
    # send대신에 input으로 설정하면 메시지를 주고 받을 수 있습니다.
    sock.send(msg.encode())

    b = sock.recv(1024)
    print(b.decode())
    sock.close()
except Exception as e:
    print("에러", e)

finally:
    print('종료되면 무조건 실행')

