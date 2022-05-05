from email import message
import smtplib
from email.message import EmailMessage

#1. SMTP 메일 서버를 연결하기 
SMTP_SERVER = 'smtp.gmail.com'
smtplib.SMTP_PORT = 465
smtp = smtplib.SMTP_SSL(SMTP_SERVER, smtplib.SMTP_PORT)

#2. SMTP 메일 서버에 로그인하기
smtp.login('gpdms6420@yonsei.ac.kr', 'hyeeun3427!@y1')

#3. 이메일 만들기
message = EmailMessage()
message.set_content('본문')

message['Subject'] = '난 혜은이야'
message['From'] = 'gpdms6420@yonsei.ac.kr'
message['To'] = 'ksjoon28@naver.com'

#4. SMTP 메일 서버로 메일 보내기
smtp.send_message(message)
smtp.quit()