from email import message
import smtplib
import re
from email.message import EmailMessage

#0. 메일 유효성 검사 함수 정의
def is_valid(addr):
    if re.match("^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$", addr):
        smtp.send_message(message)
        print('메일이 정상적으로 발송되었습니다.')
    else:
        print('유효하지 않은 이메일 주소입니다. 다시 입력해주세요.')

#1. SMTP 메일 서버를 연결하기 
SMTP_SERVER = 'smtp.gmail.com'
smtplib.SMTP_PORT = 465
smtp = smtplib.SMTP_SSL(SMTP_SERVER, smtplib.SMTP_PORT)

#2. SMTP 메일 서버에 로그인하기
smtp.login('gpdms6420@yonsei.ac.kr', '비밀!')

#3. 이메일 만들기
message = EmailMessage()
message.set_content('본문')

message['Subject'] = '난 혜은이야'
message['From'] = 'gpdms6420@yonsei.ac.kr'
message['To'] = 'gpdms6420@naver.com'

#4. SMTP 메일 서버로 메일 보내기
is_valid('gpdms6420@naver.com')
smtp.quit()