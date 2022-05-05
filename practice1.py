from bs4 import BeautifulSoup
import requests
from datetime import datetime

url = 'https://music.bugs.co.kr/chart'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
rank = 1

#p태그에 class='title'인 모든 코드를 모아줘!
results = soup.find_all('p', 'title')
live_rank_file = open('practice1.txt', 'w')

live_rank_file.write(str(datetime.today()) + '의 벅스 실시간 차트 순위입니다.\n')
for result in results:
    live_rank_file.write(str(rank) + '위:' + result.get_text() + '\n')
    rank += 1
